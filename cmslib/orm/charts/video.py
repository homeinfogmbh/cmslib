"""Video charts."""

from peewee import ForeignKeyField

from hisfs import File

from cmslib import dom
from cmslib.attachments import attachment_dom, attachment_json
from cmslib.orm.charts.api import Chart


__all__ = ['Video']


class Video(Chart):
    """A chart that may contain images and texts."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'chart_video'

    file = ForeignKeyField(File, column_name='file', null=True)

    @property
    def files(self):
        """Returns a set of IDs of files used by the chart."""
        files = set()

        if self.file is not None:
            files.add(self.file)

        return files

    def to_json(self, *args, **kwargs):
        """Returns JSON representation of this chart."""
        json = super().to_json(*args, **kwargs)
        return attachment_json(self.file, json=json)

    def to_dom(self, brief=False):
        """Returns an XML DOM of this chart."""
        if brief:
            return super().to_dom(dom.BriefChart)

        xml = super().to_dom(dom.Video)
        xml.video = attachment_dom(self.file)
        return xml
