"""Configuration related functions."""

from peewee import ModelSelect

from his import CUSTOMER

from cmslib.orm.configuration import Configuration


__all__ = ['get_configuration', 'get_configurations']


def get_configurations() -> ModelSelect:
    """Returns the respective configuration."""

    return Configuration.select(cascade=True).where(
        Configuration.customer == CUSTOMER.id)


def get_configuration(ident: int) -> Configuration:
    """Returns the respective configuration."""

    return get_configurations().where(Configuration.id == ident).get()
