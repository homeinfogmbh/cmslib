"""Local public transport charts."""

from typing import Union

from cmslib import dom
from cmslib.orm.charts.api import Chart


__all__ = ["PublicTransport"]


DomModel = Union[dom.BriefChart, dom.PublicTransport]


class PublicTransport(Chart):
    """Public transport chart."""

    class Meta:
        table_name = "chart_public_transport"

    def to_dom(self, brief: bool = False) -> DomModel:
        """Returns an XML DOM of this chart."""
        if brief:
            return super().to_dom(dom.BriefChart)

        return super().to_dom(dom.PublicTransport)
