"""Basic abstract chart type."""

from peewee import ForeignKeyField

from his.messages.data import MISSING_DATA

from cmslib import dom  # pylint: disable=E0611
from cmslib.orm.charts.api.base_chart import BaseChart
from cmslib.orm.charts.api.common import CHARTS, ChartMode
from cmslib.orm.common import DSCMS4Model


__all__ = ['Chart']


class Chart(DSCMS4Model):
    """Abstract basic chart."""

    base = ForeignKeyField(BaseChart, column_name='base', on_delete='CASCADE')

    def __init_subclass__(cls):
        """Registers the subclass as new chart."""
        CHARTS[cls.__name__] = cls

    @classmethod
    def from_json(cls, json, **kwargs):
        """Creates a chart from a JSON-ish dictionary."""
        try:
            base_dict = json.pop('base')
        except KeyError:
            raise MISSING_DATA.update(key='base') from None

        chart = super().from_json(json, **kwargs)
        transaction = BaseChart.from_json(base_dict)
        chart.base = transaction.primary
        transaction.add(chart, primary=True)
        return transaction

    def patch_json(self, json, **kwargs):
        """Pathes the chart with the provided dictionary."""
        transaction = self.base.patch_json(json.pop('base', {}))
        super().patch_json(json, **kwargs)
        transaction.add(self, primary=True)
        return transaction

    def to_json(self, mode=ChartMode.FULL, fk_fields=True, **kwargs):
        """Returns a JSON-ish dictionary."""
        if mode == ChartMode.FULL:
            json = super().to_json(**kwargs)
            json['base'] = self.base.to_json(
                autofields=False, fk_fields=fk_fields)
        elif mode == ChartMode.BRIEF:
            json = {'id': self.id}
        elif mode == ChartMode.ANON:
            json = super().to_json(skip={'id'}, **kwargs)
            json['base'] = self.base.to_json(
                autofields=False, fk_fields=fk_fields)
            return json

        json['type'] = type(self).__name__
        return json

    def to_dom(self, model):
        """Returns an XML DOM of this chart."""
        xml = model()
        xml.id = self.id
        xml.type = type(self).__name__

        if model is not dom.BriefChart:
            xml.base = self.base.to_dom()

        return xml

    def delete_instance(self):
        """Deletes the base chart and thus (CASCADE) this chart."""
        return self.base.delete_instance()
