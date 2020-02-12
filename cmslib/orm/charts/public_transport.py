"""Local public transport charts."""

from cmslib import dom
from cmslib.orm.charts.api import Chart


__all__ = ['PublicTransport']


class PublicTransport(Chart):
    """Public transport chart."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'chart_public_transport'

    def to_dom(self, brief=False):
        """Returns an XML DOM of this chart."""
        if brief:
            return super().to_dom(dom.BriefChart)

        return super().to_dom(dom.PublicTransport)
