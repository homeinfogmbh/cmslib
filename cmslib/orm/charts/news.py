"""New charts."""

from peewee import BooleanField
from peewee import CharField
from peewee import ForeignKeyField
from peewee import IntegerField
from peewee import SmallIntegerField

from newslib import Provider
from peeweeplus import EnumField

from cmslib import dom
from cmslib.orm.charts.common import Chart, ChartMode
from cmslib.orm.common import DSCMS4Model


__all__ = ['News', 'NewsProvider']


_UNCHANGED = object()


class News(Chart):
    """Chart to display news."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'chart_news'

    font_size_title = SmallIntegerField(default=8)
    title_color = IntegerField(default=0x000000)
    font_size_text = SmallIntegerField(default=8)
    text_color = IntegerField(default=0x000000)
    ken_burns = BooleanField(null=True)
    token = CharField(36, null=True)

    @classmethod
    def from_json(cls, json, **kwargs):
        """Creates an new news chart from a JSON-ish dict."""
        providers = json.pop('providers', None) or ()
        transaction = super().from_json(json, **kwargs)

        for provider in providers:
            transaction.add(NewsProvider(
                chart=transaction.chart, provider=provider))

        return transaction

    def patch_json(self, json, **kwargs):
        """Patches the chart and related components from a JSON-ish dict."""
        try:
            providers = json.pop('providers') or ()
        except KeyError:
            providers = _UNCHANGED

        transaction = super().from_json(json, **kwargs)

        if providers is not _UNCHANGED:
            for provider in self.providers:
                provider.delete_instance()

            for provider in providers:
                transaction.add(NewsProvider(
                    chart=transaction.chart, provider=provider))

        return transaction

    def to_json(self, mode=ChartMode.FULL, **kwargs):
        """Returns a JSON-ish dict."""
        json = super().to_json(mode=mode **kwargs)

        if mode == ChartMode.FULL:
            json['providers'] = [
                provider.provider.value for provider in self.providers]

        return json

    def to_dom(self, brief=False):
        """Returns an XML DOM of this chart."""
        if brief:
            return super().to_dom(dom.BriefChart)

        xml = super().to_dom(dom.News)
        xml.font_size_title = self.font_size_title
        xml.title_color = self.title_color
        xml.font_size_text = self.font_size_text
        xml.text_color = self.text_color
        xml.ken_burns = self.ken_burns
        xml.token = self.token
        return xml


class NewsProvider(DSCMS4Model):
    """Mapping between a News chart and news providers."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'news_provider'

    chart = ForeignKeyField(
        News, column_name='chart', backref='providers', on_delete='CASCADE',
        on_update='CASCADE')
    provider = EnumField(Provider)
