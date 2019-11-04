"""Base chart schedule related functions."""

from his import CUSTOMER

from cmslib.messages.schedule import NO_SUCH_SCHEDULE
from cmslib.orm.base_chart_schedule import BaseChartSchedule


__all__ = ['get_base_chart_schedule']


def get_base_chart_schedule(ident):
    """Returns the respective base chart schedule."""

    try:
        return BaseChartSchedule.get(
            (BaseChartSchedule.id == ident)
            & (BaseChartSchedule.customer == CUSTOMER.id))
    except BaseChartSchedule.DoesNotExist:
        raise NO_SUCH_SCHEDULE
