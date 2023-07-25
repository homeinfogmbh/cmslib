"""Charts for forms."""

from __future__ import annotations
from enum import Enum
from typing import Iterator, Union

from peewee import ForeignKeyField, IntegerField, Select

from peeweeplus import EnumField, HTMLTextField, Transaction

from cmslib import dom
from cmslib.orm.charts.api import ChartMode, Chart
from cmslib.orm.common import UNCHANGED, DSCMS4Model


__all__ = ["Mode", "Form"]


DomModel = Union[dom.BriefChart, dom.Form]


class Mode(Enum):
    """Form type."""

    REPAIR = "repair"
    TENANT_TO_TENANT = "tenant2tenant"
    TENANT_TO_LANDLORD = "tenant2landlord"


class Form(Chart):
    """A form chart."""

    class Meta:
        table_name = "chart_form"

    mode = EnumField(Mode)
    text = HTMLTextField(null=True)

    @classmethod
    def from_json(cls, json: dict, **kwargs) -> Transaction:
        """Creates the chart from a JSON-ish dict."""
        choices = json.pop("choices", None) or ()
        transaction = super().from_json(json, **kwargs)

        for choice in choices:
            choice = Choice.from_json(choice, form=transaction.primary)
            transaction.add(choice)

        return transaction

    @classmethod
    def subqueries(cls) -> Iterator[Select]:
        """Yields sub-queries"""
        yield from super().subqueries()
        yield Choice.select()

    def patch_json(self, json: dict, **kwargs) -> Transaction:
        """Patches the chart from a JSON-ish dict."""
        choices = json.pop("choices", UNCHANGED) or ()
        transaction = super().patch_json(json, **kwargs)

        if choices is not UNCHANGED:
            for choice in self.choices:
                transaction.delete(choice)

            for choice in choices:
                choice = Choice.from_json(choice, form=transaction.primary)
                transaction.add(choice)

        return transaction

    def to_json(self, mode: ChartMode = ChartMode.FULL, **kwargs) -> dict:
        """Returns a JSON-ish dict."""
        json = super().to_json(mode=mode, **kwargs)

        if mode == ChartMode.FULL:
            json["choices"] = [choice.to_json() for choice in self.choices]

        return json

    def to_dom(self, brief: bool = False) -> DomModel:
        """Returns an XML DOM of this chart."""
        if brief:
            return super().to_dom(dom.BriefChart)

        xml = super().to_dom(dom.Form)
        xml.mode = self.mode.value
        xml.text = self.text
        xml.choice = [choice.to_dom() for choice in self.choices]
        return xml


class Choice(DSCMS4Model):
    """Choice options for forms."""

    class Meta:
        table_name = "chart_form_choice"

    form = ForeignKeyField(
        Form,
        column_name="form",
        backref="choices",
        on_delete="CASCADE",
        lazy_load=False,
    )
    text = HTMLTextField()
    index = IntegerField(default=0)

    @classmethod
    def from_json(cls, json: dict, form: Form = None, **kwargs) -> Choice:
        """Creates a choice from a JSON-ish dict for the given form."""
        record = super().from_json(json, **kwargs)
        record.form = form
        return record

    def to_dom(self) -> dom.Choice:
        """Returns an XML DOM of this chart."""
        return dom.Choice(self.text, index=self.index)
