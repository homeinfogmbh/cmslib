"""Schedule related functions."""

from his import CUSTOMER

from cmslib.messages.schedule import NO_SUCH_SCHEDULE
from cmslib.orm.schedule import Schedule


__all__ = ['get_schedule']


def get_schedule(ident):
    """Returns the respective schedule."""

    try:
        return Schedule.get(
            (Schedule.id == ident) & (Schedule.customer == CUSTOMER.id))
    except Schedule.DoesNotExist:
        raise NO_SUCH_SCHEDULE
