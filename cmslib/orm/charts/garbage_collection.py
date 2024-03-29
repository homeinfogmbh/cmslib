"""Garbage collection chart."""

from typing import Union

from cmslib import dom
from cmslib.orm.charts.api import Chart


__all__ = ["GarbageCollection"]


DomModel = Union[dom.BriefChart, dom.GarbageCollection]


class GarbageCollection(Chart):
    """Chart for garbage collection."""

    class Meta:
        table_name = "chart_garbage_collection"

    def to_dom(self, brief: bool = False) -> DomModel:
        """Returns an XML DOM of this chart."""
        if brief:
            return super().to_dom(dom.BriefChart)

        return super().to_dom(dom.GarbageCollection)
