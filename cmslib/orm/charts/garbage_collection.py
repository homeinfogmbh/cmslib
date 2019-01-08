"""Garbage collection chart."""

from cmslib import dom
from cmslib.orm.charts.common import Chart


__all__ = ['GarbageCollection']


class GarbageCollection(Chart):
    """Chart for garbage collection."""

    class Meta:
        table_name = 'chart_garbage_collection'

    def to_dom(self, brief=False):
        """Returns an XML DOM of this chart."""
        if brief:
            return super().to_dom(dom.BriefChart)

        return super().to_dom(dom.GarbageCollection)
