"""Schedule related functions."""

from peewee import ModelSelect

from his import CUSTOMER
from mdb import Address, Company, Customer

from cmslib.messages.schedule import NO_SUCH_SCHEDULE
from cmslib.orm.schedule import Schedule


__all__ = ['get_schedule']


def list_schedules() -> ModelSelect:
    """Selects the schedules of the current customer."""

    select = Schedule.select(Schedule, Customer, Company, Address)
    select = select.join(Customer).join(Company).join(Address)
    return select.where(Schedule.customer == CUSTOMER.id)


def get_schedule(ident: int) -> Schedule:
    """Returns the respective schedule."""

    try:
        return list_schedules().get(Schedule.id == ident)
    except Schedule.DoesNotExist:
        raise NO_SUCH_SCHEDULE from None
