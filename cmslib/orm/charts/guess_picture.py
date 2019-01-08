"""Oicture guessing chart."""

from cmslib import dom
from cmslib.orm.charts.common import Chart


__all__ = ['GuessPicture']


class GuessPicture(Chart):
    """Chart for guessing pictures."""

    class Meta:
        table_name = 'chart_guess_picture'

    def to_dom(self, brief=False):
        """Returns an XML DOM of this chart."""
        if brief:
            return super().to_dom(dom.BriefChart)

        return super().to_dom(dom.GuessPicture)
