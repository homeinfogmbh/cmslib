"""Black board charts."""

from enum import Enum

from peewee import ForeignKeyField, IntegerField

from hisfs import get_file, File
from peeweeplus import EnumField

from cmslib import dom
from cmslib.attachments import attachment_dom, attachment_json
from cmslib.orm.charts.api import ChartMode, Chart
from cmslib.orm.common import UNCHANGED, DSCMS4Model


__all__ = ['Blackboard', 'Image']


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

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'chart_blackboard'

    @classmethod
    def from_json(cls, json, **kwargs):
        """Creates a new chart ffrom a JSON-ish dict."""
        # Pop images first to exclude them from the
        # dictionary before invoking super().from_json().
        images = json.pop('images', ())
        transaction = super().from_json(json, **kwargs)

        for image in images:
            image = Image.from_json(image, transaction.primary)
            transaction.add(image)

        return transaction

    @property
    def files(self):
        """Returns a set of IDs of files used by the chart."""
        return set(image.file for image in self.images)

    def patch_json(self, json, **kwargs):
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

    def to_json(self, mode=ChartMode.FULL, **kwargs):
        """Returns the dictionary representation of this chart's fields."""
        json = super().to_json(mode=mode, **kwargs)

        if mode == ChartMode.FULL:
            json['images'] = [
                image.to_json(fk_fields=False, autofields=False)
                for image in self.images.order_by(Image.index)]

        return json

    def to_dom(self, brief=False):
        """Returns an XML DOM of this chart."""
        if brief:
            return super().to_dom(dom.BriefChart)

        xml = super().to_dom(dom.Blackboard)
        images = (img.to_dom() for img in self.images.order_by(Image.index))
        xml.image = filter(None, images)
        return xml


class Image(DSCMS4Model):
    """Image for an ImageText chart."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'chart_blackboard_image'

    chart = ForeignKeyField(
        Blackboard, column_name='chart', backref='images', on_delete='CASCADE')
    file = ForeignKeyField(File, column_name='file')
    format = EnumField(Format, default=Format.A4)
    index = IntegerField(default=0)

    @classmethod
    def from_json(cls, json, chart=None, **kwargs):
        """Creates an image from the respective JSON-ish dict."""
        try:
            file_id = json.pop('file')
        except KeyError:
            file_id = json.pop('image')

        record = super().from_json(json, **kwargs)
        record.chart = chart
        record.file = get_file(file_id)
        return record

    def to_json(self, *args, **kwargs):
        """Returns a JSON representation of this record."""
        json = super().to_json(*args, **kwargs)
        return attachment_json(self.file, json=json)

    def to_dom(self):
        """Returns an XML DOM of this record."""
        return attachment_dom(
            self.file, format=self.format.value, index=self.index)
