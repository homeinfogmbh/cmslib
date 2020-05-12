"""Schedule related functions."""

from his import CUSTOMER

from cmslib.messages.schedule import NO_SUCH_SCHEDULE
from cmslib.orm.schedule import Schedule


__all__ = ['get_schedule']


def get_schedule(ident):
    """Returns the respective schedule."""

    condition = Schedule.id == ident
    condition &= Schedule.customer == CUSTOMER.id

    try:
        return Schedule.get(condition)
    except Schedule.DoesNotExist:
        raise NO_SUCH_SCHEDULE
