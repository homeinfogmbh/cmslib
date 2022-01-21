"""Schedule related functions."""

from peewee import Select

from his import CUSTOMER

from cmslib.orm.schedule import Schedule


__all__ = ['get_schedule', 'get_schedules']


def get_schedule(ident: int) -> Schedule:
    """Returns the respective schedule."""

    return get_schedules().where(Schedule.id == ident).get()


def get_schedules() -> Select:
    """Selects the schedules of the current customer."""

    return Schedule.select(cascade=True).where(
        Schedule.customer == CUSTOMER.id)
