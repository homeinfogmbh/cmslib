"""Charts for forms."""

from enum import Enum

from peewee import ForeignKeyField, IntegerField, TextField

from peeweeplus import EnumField

from cmslib import dom
from cmslib.orm.charts.common import ChartMode, Chart
from cmslib.orm.common import UNCHANGED, DSCMS4Model


__all__ = ['Mode', 'Form']


class Mode(Enum):
    """Form type."""

    REPAIR = 'repair'
    TENANT_TO_TENANT = 'tenant2tenant'
    TENANT_TO_LANDLORD = 'tenant2landlord'


class Form(Chart):
    """A form chart."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'chart_form'

    mode = EnumField(Mode, column_name='mode')
    text = TextField(null=True)

    @classmethod
    def from_json(cls, json, **kwargs):
        """Creates the chart from a JSON-ish dict."""
        choices = json.pop('choices', None) or ()
        transaction = super().from_json(json, **kwargs)

        for choice in choices:
            choice = Choice.from_json(choice, form=transaction.primary)
            transaction.add(choice)

        return transaction

    def patch_json(self, json, **kwargs):
        """Patches the chart from a JSON-ish dict."""
        choices = json.pop('choices', UNCHANGED) or ()
        transaction = super().patch_json(json, **kwargs)

        if choices is not UNCHANGED:
            for choice in self.choices:
                transaction.delete(choice)

            for choice in choices:
                choice = Choice.from_json(choice, form=transaction.primary)
                transaction.add(choice)

        return transaction

    def to_json(self, mode=ChartMode.FULL, **kwargs):
        """Returns a JSON-ish dict."""
        json = super().to_json(mode=mode, **kwargs)

        if mode == ChartMode.FULL:
            json['choices'] = [choice.to_json() for choice in self.choices]

        return json

    def to_dom(self, brief=False):
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

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'chart_form_choice'

    form = ForeignKeyField(
        Form, column_name='form', backref='choices', on_delete='CASCADE')
    text = TextField()
    index = IntegerField(default=0)

    @classmethod
    def from_json(cls, json, form=None, **kwargs):
        """Creates a choice from a JSON-ish dict for the given form."""
        record = super().from_json(json, **kwargs)
        record.form = form
        return record

    def to_dom(self):
        """Returns an XML DOM of this chart."""
        return dom.Choice(self.text, index=self.index)
