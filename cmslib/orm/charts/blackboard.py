"""Black board charts."""

from __future__ import annotations
from enum import Enum
from typing import Iterator, Union

from peewee import ForeignKeyField, IntegerField, Select

from hisfs import get_file, File
from peeweeplus import EnumField, Transaction

from cmslib import dom
from cmslib.attachments import attachment_dom, attachment_json
from cmslib.orm.charts.api import ChartMode, Chart
from cmslib.orm.common import UNCHANGED, Attachment


__all__ = ['Blackboard', 'Image']


DomModel = Union[dom.BriefChart, dom.Blackboard]


class Format(Enum):
    """Image display format."""

    A0 = 'A0'
    A1 = 'A1'
    A2 = 'A2'
    A3 = 'A3'
    A4 = 'A4'
    A5 = 'A5'
    A6 = 'A6'
    A7 = 'A7'


class Blackboard(Chart):
    """A chart that may contain images."""

    class Meta:
        table_name = 'chart_blackboard'

    @classmethod
    def from_json(cls, json: dict, **kwargs) -> Transaction:
        """Creates a new chart from a JSON-ish dict."""
        # Pop images first to exclude them from the
        # dictionary before invoking super().from_json().
        images = json.pop('images', ())
        transaction = super().from_json(json, **kwargs)

        for image in images:
            image = Image.from_json(image, transaction.primary)
            transaction.add(image)

        return transaction

    @property
    def files(self) -> set[File]:
        """Returns a set of files used by the chart."""
        return {image.file for image in self.images}

    @classmethod
    def subqueries(cls) -> Iterator[Select]:
        """Yields sub-queries"""
        yield from super().subqueries()
        yield Image.select(cascade=True, shallow=True).order_by(Image.index)

    def patch_json(self, json: dict, **kwargs) -> Transaction:
        """Patches the respective chart."""
        images = json.pop('images', UNCHANGED) or ()
        transaction = super().patch_json(json, **kwargs)

        if images is not UNCHANGED:
            for image in self.images:
                transaction.delete(image)

            for image in images:
                image = Image.from_json(image, transaction.primary)
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

        xml = super().to_dom(dom.Blackboard)
        xml.image = filter(None, (img.to_dom() for img in self.images))
        return xml


class Image(Attachment):
    """Image for an ImageText chart."""

    class Meta:
        table_name = 'chart_blackboard_image'

    chart = ForeignKeyField(
        Blackboard, column_name='chart', backref='images', on_delete='CASCADE',
        lazy_load=False
    )
    format = EnumField(Format, default=Format.A4)
    index = IntegerField(default=0)

    @classmethod
    def from_json(cls, json: dict, chart: Blackboard, **kwargs) -> Image:
        """Creates an image from the respective JSON-ish dict."""
        file_id = json.pop('file')
        record = super().from_json(json, **kwargs)
        record.chart = chart
        record.file = get_file(file_id)
        return record

    def to_json(self, *args, **kwargs) -> dict:
        """Returns a JSON representation of this record."""
        json = super().to_json(*args, **kwargs)
        return attachment_json(self.file, json=json)

    def to_dom(self) -> dom.Attachment:
        """Returns an XML DOM of this record."""
        return attachment_dom(
            self.file, format=self.format.value, index=self.index
        )
