"""Charts for forms."""

from enum import Enum

from peeweeplus import EnumField

from cmslib import dom
from cmslib.orm.charts.common import Chart


__all__ = ['Mode', 'Form']


class Mode(Enum):
    """Form type."""

    REPAIR = 'repair'
    TENANT_TO_TENANT = 'tenant2tenant'


class Form(Chart):
    """A form chart."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'chart_form'

    mode = EnumField(Mode, column_name='mode')

    def to_dom(self, brief=False):
        """Returns an XML DOM of this chart."""
        if brief:
            return super().to_dom(dom.BriefChart)

        xml = super().to_dom(dom.Form)
        xml.mode = self.mode.value
        return xml
