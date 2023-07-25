"""Schedule related functions."""

from typing import Union

from peewee import Select

from mdb import Customer

from cmslib.orm.schedule import Schedule


__all__ = ["get_schedule", "get_schedules"]


def get_schedule(ident: int, customer: Union[Customer, int]) -> Schedule:
    """Returns the respective schedule of the given customer."""

    return get_schedules(customer).where(Schedule.id == ident).get()


def get_schedules(customer: Union[Customer, int]) -> Select:
    """Selects the schedules of the given customer."""

    return Schedule.select(cascade=True).where(Schedule.customer == customer)
