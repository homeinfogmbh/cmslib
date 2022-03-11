"""Weather chart."""

from typing import Iterator, Union

from peewee import ForeignKeyField, IntegerField, Select

from hisfs import get_file, File
from peeweeplus import HTMLCharField, Transaction

from cmslib import dom
from cmslib.attachments import attachment_dom, attachment_json
from cmslib.orm.charts.api import ChartMode, Chart
from cmslib.orm.common import UNCHANGED, Attachment


__all__ = ['Weather', 'Image']


DomModel = Union[dom.BriefChart, dom.Weather]


class Weather(Chart):
    """Weather data."""

    class Meta:
        table_name = 'chart_weather'

    location = HTMLCharField(255)
    font_color = IntegerField()
    icon_color = IntegerField()
    box_color_top = IntegerField()
    box_color_middle = IntegerField()
    box_color_bottom = IntegerField()
    transparency = IntegerField()

    @classmethod
    def from_json(cls, json: dict, **kwargs) -> Transaction:
        """Creates a new quotes chart from the
        dictionary for the respective customer.
        """
        # Pop images and texts first to exclude them from the
        # dictionary before invoking super().from_json().
        images = json.pop('images', ())
        transaction = super().from_json(json, **kwargs)

        for image in images:
            file = get_file(image)
            image = Image(chart=transaction.primary, file=file)
            transaction.add(image)

        return transaction

    @property
    def files(self) -> set[File]:
        """Returns a set of IDs of files used by the chart."""
        return {image.file for image in self.images}

    @classmethod
    def subqueries(cls) -> Iterator[Select]:
        """Yields sub-queries"""
        yield from super().subqueries()
        yield Image.select(cascade=True, shallow=True)

    def patch_json(self, json: dict, **kwargs) -> Transaction:
        """Patches the respective chart."""
        images = json.pop('images', UNCHANGED) or ()
        transaction = super().patch_json(json, **kwargs)

        if images is not UNCHANGED:
            for image in self.images:
                transaction.delete(image)

            for image in images:
                file = get_file(image)
                image = Image(chart=transaction.primary, file=file)
                transaction.add(image)

        return transaction

    def to_json(self, mode: ChartMode = ChartMode.FULL, **kwargs) -> dict:
        """Returns the dictionary representation of this chart's fields."""
        json = super().to_json(mode=mode, **kwargs)

        if mode == ChartMode.FULL:
            json['images'] = [
                image.to_json(fk_fields=False, autofields=False)
                for image in self.images
            ]

        return json

    def to_dom(self, brief: bool = False) -> DomModel:
        """Returns an XML DOM of this chart."""
        if brief:
            return super().to_dom(dom.BriefChart)

        xml = super().to_dom(dom.Weather)
        xml.location = self.location
        xml.font_color = self.font_color
        xml.icon_color = self.icon_color
        xml.box_color_top = self.box_color_top
        xml.box_color_middle = self.box_color_middle
        xml.box_color_bottom = self.box_color_bottom
        xml.transparency = self.transparency
        xml.image = list(filter(None, (img.to_dom() for img in self.images)))
        return xml


class Image(Attachment):
    """Image for an ImageTextChart."""

    class Meta:
        table_name = 'chart_weather_image'

    chart = ForeignKeyField(
        Weather, column_name='chart', backref='images', on_delete='CASCADE',
        lazy_load=False
    )

    def to_json(self, *args, **kwargs) -> dict:
        """Returns a JSON representation of this record."""
        json = super().to_json(*args, **kwargs)
        return attachment_json(self.file, json=json)

    def to_dom(self) -> dom.Attachment:
        """Returns an XML DOM of this record."""
        return attachment_dom(self.file)
