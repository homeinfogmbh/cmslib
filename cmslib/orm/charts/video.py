"""Video charts."""

from peewee import ForeignKeyField

from hisfs import get_file, File

from cmslib import dom
from cmslib.attachments import attachment_dom, attachment_json
from cmslib.orm.charts.api import Chart
from cmslib.orm.common import UNCHANGED


__all__ = ['Video']


class Video(Chart):
    """A chart that may contain images and texts."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'chart_video'

    file = ForeignKeyField(File, column_name='file', null=True)

    @classmethod
    def from_json(cls, json, **kwargs):
        """Creates a new video chart from a JSON-ish dict."""
        file = json.pop('file', None)
        record = super().from_json(json)

        if file:
            record.file = get_file(file)

        return record

    @property
    def files(self):
        """Returns a set of IDs of files used by the chart."""
        files = set()

        if self.file is not None:
            files.add(self.file)

        return files

    def patch_json(self, json, **kwargs):
        """Patches a video chart."""
        file = json.pop('file', UNCHANGED)
        transaction = super().patch_json(json)

        if file is not UNCHANGED:
            self.file = get_file(file)

        return transaction

    def to_json(self, *args, skip=(), **kwargs):
        """Returns JSON representation of this chart."""
        skip = {*skip, 'file'} if skip else {'file'}
        json = super().to_json(*args, skip=skip, **kwargs)
        return attachment_json(self.file, json=json)

    def to_dom(self, brief=False):
        """Returns an XML DOM of this chart."""
        if brief:
            return super().to_dom(dom.BriefChart)

        xml = super().to_dom(dom.Video)
        xml.video = attachment_dom(self.file)
        return xml
