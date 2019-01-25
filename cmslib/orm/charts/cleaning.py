"""Cleaning chart."""

from enum import Enum

from peewee import CharField, TextField, SmallIntegerField, IntegerField
from peeweeplus import EnumField

from cmslib import dom
from cmslib.orm.charts.common import Chart


__all__ = ['Mode', 'Cleaning']


class Mode(Enum):
    """Possible displaying modes."""

    SHOW = 'show'
    INPUT = 'input'


class Cleaning(Chart):
    """Cleaning chart."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'chart_cleaning'

    title = CharField(255, null=True)
    mode = EnumField(Mode)
    text = TextField(null=True)
    font_size = SmallIntegerField(default=8)
    text_color = IntegerField(default=0x000000)

    def to_dom(self, brief=False):
        """Returns an XML DOM of this chart."""
        if brief:
            return super().to_dom(dom.BriefChart)

        xml = super().to_dom(dom.Cleaning)
        xml.title = self.title
        xml.mode = self.mode.value
        xml.text = self.text
        xml.font_size = self.font_size
        xml.text_color = self.text_color
        return xml
