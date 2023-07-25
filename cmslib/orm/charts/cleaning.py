"""Cleaning chart."""

from enum import Enum
from typing import Union

from peewee import CharField, SmallIntegerField, IntegerField
from peeweeplus import EnumField, HTMLTextField

from cmslib import dom
from cmslib.orm.charts.api import Chart


__all__ = ["Mode", "Cleaning"]


DomModel = Union[dom.BriefChart, dom.Cleaning]


class Mode(Enum):
    """Possible displaying modes."""

    SHOW = "show"
    INPUT = "input"


class Cleaning(Chart):
    """Cleaning chart."""

    class Meta:
        table_name = "chart_cleaning"

    title = CharField(255, null=True)
    mode = EnumField(Mode)
    text = HTMLTextField(null=True)
    font_size = SmallIntegerField(default=8)
    text_color = IntegerField(default=0x000000)

    def to_dom(self, brief: bool = False) -> DomModel:
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
