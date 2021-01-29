"""RSS feed charts."""

from enum import Enum
from typing import Union

from peewee import CharField, IntegerField, SmallIntegerField

from peeweeplus import EnumField

from cmslib import dom
from cmslib.orm.charts.api import Chart


__all__ = ['Mode', 'URL']


DomModel = Union[dom.BriefChart, dom.URL]


class Mode(Enum):
    """The type of the URL."""

    RSS = 'RSS'
    HTML = 'HTML'


class URL(Chart):
    """A chart for with configurable URLs."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'chart_url'

    url = CharField()
    mode = EnumField(Mode)
    title_color = IntegerField(default=0x000000)
    font_size_title = SmallIntegerField(default=26)
    text_color = IntegerField(default=0x000000)
    font_size_text = SmallIntegerField(default=26)

    def to_dom(self, brief: bool = False) -> DomModel:
        """Returns an XML DOM of this chart."""
        if brief:
            return super().to_dom(dom.BriefChart)

        xml = super().to_dom(dom.URL)
        xml.title_color = self.title_color
        xml.font_size_title = self.font_size_title
        xml.text_color = self.text_color
        xml.font_size_text = self.font_size_text
        xml.url = self.url
        xml.mode = self.mode.value
        return xml
