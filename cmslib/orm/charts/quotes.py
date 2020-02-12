"""Quotes charts."""

from peewee import IntegerField, SmallIntegerField

from cmslib import dom  # pylint: disable=E0611
from cmslib.orm.charts.api import Chart


__all__ = ['Quotes']


class Quotes(Chart):
    """Chart for quotations."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'chart_quotes'

    font_color = IntegerField(0x000000)
    background_color = IntegerField(0x000000)
    font_size_quote = SmallIntegerField(default=26)
    font_size_author = SmallIntegerField(default=26)

    def to_dom(self, brief=False):  # pylint: disable=W0221
        """Returns an XML DOM of this chart."""
        if brief:
            return super().to_dom(dom.BriefChart)

        xml = super().to_dom(dom.Quotes)
        xml.font_color = self.font_color
        xml.background_color = self.background_color
        xml.font_size_quote = self.font_size_quote
        xml.font_size_author = self.font_size_author
        return xml
