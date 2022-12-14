"""New charts."""

from typing import Iterator, Union

from peewee import BooleanField
from peewee import CharField
from peewee import ForeignKeyField
from peewee import IntegerField
from peewee import Select
from peewee import SmallIntegerField

from newslib import Provider
from peeweeplus import Transaction

from cmslib import dom
from cmslib.orm.charts.api import Chart, ChartMode
from cmslib.orm.common import UNCHANGED, DSCMS4Model


__all__ = ['News', 'NewsProvider']


DomModel = Union[dom.BriefChart, dom.News]


class News(Chart):
    """Chart to display news."""

    class Meta:
        table_name = 'chart_news'

    font_size_title = SmallIntegerField(default=8)
    title_color = IntegerField(default=0x000000)
    font_size_text = SmallIntegerField(default=8)
    text_color = IntegerField(default=0x000000)
    ken_burns = BooleanField(null=True)

    @classmethod
    def from_json(cls, json: dict, **kwargs) -> Transaction:
        """Creates a new news chart from a JSON-ish dict."""
        providers = json.pop('providers', None) or ()
        transaction = super().from_json(json, **kwargs)

        for provider in providers:
            transaction.add(NewsProvider(
                chart=transaction.primary, provider=Provider(provider)
            ))

        return transaction

    @classmethod
    def subqueries(cls) -> Iterator[Select]:
        """Yields sub-queries"""
        yield from super().subqueries()
        yield NewsProvider.select()

    def patch_json(self, json: dict, **kwargs) -> Transaction:
        """Patches the chart and related components from a JSON-ish dict."""
        try:
            providers = json.pop('providers') or ()
        except KeyError:
            providers = UNCHANGED

        transaction = super().patch_json(json, **kwargs)

        if providers is not UNCHANGED:
            for provider in self.providers:
                provider.delete_instance()

            for provider in providers:
                transaction.add(NewsProvider(
                    chart=transaction.primary, provider=Provider(provider)
                ))

        return transaction

    def to_json(self, mode: ChartMode = ChartMode.FULL, **kwargs) -> dict:
        """Returns a JSON-ish dict."""
        json = super().to_json(mode=mode, **kwargs)

        if mode == ChartMode.FULL:
            json['providers'] = [
                provider.provider for provider in self.providers
            ]

        return json

    def to_dom(self, brief: bool = False) -> DomModel:
        """Returns an XML DOM of this chart."""
        if brief:
            return super().to_dom(dom.BriefChart)

        xml = super().to_dom(dom.News)
        xml.font_size_title = self.font_size_title
        xml.title_color = self.title_color
        xml.font_size_text = self.font_size_text
        xml.text_color = self.text_color
        xml.ken_burns = self.ken_burns
        xml.provider = [provider.provider for provider in self.providers]
        return xml


class NewsProvider(DSCMS4Model):
    """Mapping between a News chart and news providers."""

    class Meta:
        table_name = 'news_provider'

    chart = ForeignKeyField(
        News, column_name='chart', backref='providers', on_delete='CASCADE',
        on_update='CASCADE', lazy_load=False
    )
    provider = CharField(255)
