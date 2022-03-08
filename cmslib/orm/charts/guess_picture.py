"""Picture guessing chart."""

from typing import Union

from cmslib import dom
from cmslib.orm.charts.api import Chart


__all__ = ['GuessPicture']


DomModel = Union[dom.BriefChart, dom.GuessPicture]


class GuessPicture(Chart):
    """Chart for guessing pictures."""

    class Meta:
        table_name = 'chart_guess_picture'

    def to_dom(self, brief: bool = False) -> DomModel:
        """Returns an XML DOM of this chart."""
        if brief:
            return super().to_dom(dom.BriefChart)

        return super().to_dom(dom.GuessPicture)
