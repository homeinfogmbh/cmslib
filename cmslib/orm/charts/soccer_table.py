"""Chart for German first league soccer / football table."""

from typing import Union

from peewee import IntegerField, SmallIntegerField

from cmslib import dom
from cmslib.orm.charts.api import Chart


__all__ = ['SoccerTable']


DomModel = Union[dom.BriefChart, dom.SoccerTable]


class SoccerTable(Chart):
    """Chart to display news."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'chart_soccer_table'

    font_size_title = SmallIntegerField(default=8)
    title_color = IntegerField(default=0x000000)
    font_size_text = SmallIntegerField(default=8)
    text_color = IntegerField(default=0x000000)

    def to_dom(self, brief: bool = False) -> DomModel:
        """Returns an XML DOM of this chart."""
        if brief:
            return super().to_dom(dom.BriefChart)

        xml = super().to_dom(dom.SoccerTable)
        xml.font_size_title = self.font_size_title
        xml.title_color = self.title_color
        xml.font_size_text = self.font_size_text
        xml.text_color = self.text_color
        return xml
