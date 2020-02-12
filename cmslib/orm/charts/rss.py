"""RSS feed charts."""

from peewee import CharField, IntegerField, SmallIntegerField

from cmslib import dom
from cmslib.orm.charts.api import Chart


__all__ = ['RSS']


class RSS(Chart):
    """A chart for RSS feeds."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'chart_rss'

    title_color = IntegerField(default=0x000000)
    font_size_title = SmallIntegerField(default=26)
    text_color = IntegerField(default=0x000000)
    font_size_text = SmallIntegerField(default=26)
    url = CharField()

    def to_dom(self, brief=False):
        """Returns an XML DOM of this chart."""
        if brief:
            return super().to_dom(dom.BriefChart)

        xml = super().to_dom(dom.RSS)
        xml.title_color = self.title_color
        xml.font_size_title = self.font_size_title
        xml.text_color = self.text_color
        xml.font_size_text = self.font_size_text
        xml.url = self.url
        return xml
