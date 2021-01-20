"""Video charts."""

from typing import Set, Union

from peewee import JOIN, ForeignKeyField, ModelSelect

from hisfs import get_file, File
from peeweeplus import Transaction

from cmslib import dom
from cmslib.attachments import attachment_dom, attachment_json
from cmslib.orm.charts.api import ChartMode, Chart
from cmslib.orm.common import UNCHANGED


__all__ = ['Video']


DomModel = Union[dom.BriefChart, dom.Video]


class Video(Chart):
    """A chart that may contain images and texts."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'chart_video'

    file = ForeignKeyField(File, column_name='file', null=True)

    @classmethod
    def from_json(cls, json: dict, **kwargs) -> Transaction:
        """Creates a new video chart from a JSON-ish dict."""
        file = json.pop('file', None)
        transaction = super().from_json(json)
        chart = transaction.primary

        if file:
            chart.file = get_file(file)

        return transaction

    @classmethod
    def select(cls, *args, cascade: bool = False, **kwargs) -> ModelSelect:
        """Selects records."""
        if not cascade:
            return super().select(*args, **kwargs)

        return super().select(*args, File, cascade=True, **kwargs).join_from(
            cls, File, on=cls.file == File.id, join_type=JOIN.LEFT_OUTER)


    @property
    def files(self) -> Set[File]:
        """Returns a set of IDs of files used by the chart."""
        return {self.file} if self.file else set()

    def patch_json(self, json: dict, **kwargs) -> Transaction:
        """Patches a video chart."""
        file = json.pop('file', UNCHANGED)
        transaction = super().patch_json(json)

        if file is not UNCHANGED:
            self.file = get_file(file)

        return transaction

    def to_json(self, mode: ChartMode = ChartMode.FULL, **kwargs) -> dict:
        """Returns JSON representation of this chart."""
        json = super().to_json(mode=mode, **kwargs)

        if mode == ChartMode.FULL:
            json['file'] = attachment_json(self.file)

        return json

    def to_dom(self, brief: bool = False) -> DomModel:
        """Returns an XML DOM of this chart."""
        if brief:
            return super().to_dom(dom.BriefChart)

        xml = super().to_dom(dom.Video)
        xml.video = attachment_dom(self.file)
        return xml
