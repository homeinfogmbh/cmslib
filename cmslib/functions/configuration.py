"""Configuration related functions."""

from peewee import Select

from his import CUSTOMER

from cmslib.orm.configuration import Configuration


__all__ = ['get_configuration', 'get_configurations']


def get_configuration(ident: int) -> Configuration:
    """Returns the respective configuration."""

    return get_configurations().where(Configuration.id == ident).get()


def get_configurations() -> Select:
    """Returns the respective configuration."""

    return Configuration.select(cascade=True).where(
        Configuration.customer == CUSTOMER.id)
