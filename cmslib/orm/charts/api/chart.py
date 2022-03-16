"""Basic abstract chart type."""

from __future__ import annotations
from typing import Iterator, Optional, Union

from peewee import JOIN, Expression, ForeignKeyField, Select, prefetch

from filedb import File
from mdb import Company, Customer
from peeweeplus import Transaction

from cmslib import dom
from cmslib.orm.charts.api.base_chart import BaseChart, ChartPIN
from cmslib.orm.charts.api.common import CHARTS, ChartMode
from cmslib.orm.common import DSCMS4Model
from cmslib.orm.schedule import Schedule


__all__ = ['Chart']


class Chart(DSCMS4Model):
    """Abstract basic chart."""

    base = ForeignKeyField(
        BaseChart, column_name='base', on_delete='CASCADE', lazy_load=False
    )

    def __init_subclass__(cls, *args, **kwargs):
        """Registers the subclass as new chart."""
        super().__init_subclass__(*args, **kwargs)
        CHARTS[cls.__name__] = cls

    @classmethod
    def fetch(
            cls,
            customer: Union[Customer, int],
            ident: Optional[int] = None,
            trashed: Union[Expression, bool] = True
    ) -> Union[list[Chart], Chart]:
        """Selects blackboard charts."""
        charts = cls.select(cascade=True).where(
            (BaseChart.customer == customer)
            & trashed
        )

        if ident is None:
            return prefetch(charts, *cls.subqueries())

        charts = prefetch(charts.where(cls.id == ident), *cls.subqueries())

        try:
            return charts[0]
        except IndexError:
            raise cls.DoesNotExist(customer, ident) from None

    @classmethod
    def from_json(cls, json: dict, **kwargs) -> Transaction:
        """Creates a chart from a JSON-ish dict."""
        transaction = BaseChart.from_json(json.pop('base'), typ=cls.__name__)
        chart = super().from_json(json, **kwargs)
        chart.base = transaction.primary
        transaction.add(chart, primary=True)
        return transaction

    @classmethod
    def select(cls, *args, cascade: bool = False) -> Select:
        """Selects records."""
        if not cascade:
            return super().select(*args)

        return super().select(
            cls, BaseChart, Customer, Company, Schedule, *args).join(
            BaseChart).join(Customer).join(Company).join_from(
            BaseChart, Schedule, join_type=JOIN.LEFT_OUTER
        )

    @classmethod
    def subqueries(cls) -> Iterator[Select]:
        """Yields sub-queries"""
        yield BaseChart.select(cascade=True)
        yield ChartPIN.select()

    @property
    def files(self) -> set[File]:
        """Returns a set of files this chart uses."""
        return set()

    def patch_json(self, json: dict, **kwargs) -> Transaction:
        """Patches the chart from a JSON-ish dict."""
        transaction = self.base.patch_json(json.pop('base', {}))
        super().patch_json(json, **kwargs)
        transaction.add(self, primary=True)
        return transaction

    def to_json(
            self,
            mode: ChartMode = ChartMode.FULL,
            fk_fields: bool = True,
            **kwargs
    ) -> dict:
        """Returns a JSON-ish dictionary."""
        if mode == ChartMode.FULL:
            json = super().to_json(**kwargs)
            json['base'] = self.base.to_json(fk_fields=fk_fields, **kwargs)
        elif mode == ChartMode.BRIEF:
            json = {'id': self.id}
        elif mode == ChartMode.ANON:
            json = super().to_json(autofields=False, **kwargs)
            json['base'] = self.base.to_json(
                autofields=False, fk_fields=fk_fields, **kwargs)
            return json

        json['type'] = type(self).__name__
        return json

    def to_dom(self, model: type) -> dom.Chart:
        """Returns an XML DOM of this chart."""
        xml = model()
        xml.id = self.id
        xml.type = type(self).__name__

        if model is not dom.BriefChart:
            xml.base = self.base.to_dom()

        return xml

    def delete_instance(self) -> int:
        """Deletes the base chart and thus (CASCADE) this chart."""
        return self.base.delete_instance()
