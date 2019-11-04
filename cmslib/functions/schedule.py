"""Schedule related functions."""

from his import CUSTOMER

from cmslib.messages.schedule import NO_SUCH_SCHEDULE
from cmslib.orm.schedule import Schedule, BaseChartSchedule


__all__ = ['get_schedule', 'get_base_chart_schedule']


def get_schedule(ident):
    """Returns the respective schedule."""

    try:
        return Schedule.get(
            (Schedule.id == ident) & (Schedule.customer == CUSTOMER.id))
    except Schedule.DoesNotExist:
        raise NO_SUCH_SCHEDULE


def get_base_chart_schedule(ident):
    """Returns the respective base chart schedule."""

    try:
        return BaseChartSchedule.get(
            (BaseChartSchedule.id == ident)
            & (BaseChartSchedule.customer == CUSTOMER.id))
    except BaseChartSchedule.DoesNotExist:
        raise NO_SUCH_SCHEDULE
