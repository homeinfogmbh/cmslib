"""Configuration related functions."""

from typing import Union

from peewee import Select

from mdb import Customer

from cmslib.orm.configuration import Configuration


__all__ = ['get_configuration', 'get_configurations']


def get_configuration(
        ident: int,
        customer: Union[Customer, int]
) -> Configuration:
    """Returns the respective configuration of the given customer."""

    return get_configurations(customer).where(Configuration.id == ident).get()


def get_configurations(customer: Union[Customer, int]) -> Select:
    """Returns the configurations of the given customer."""

    return Configuration.select(cascade=True).where(
        Configuration.customer == customer
    )
