"""Configuration related functions."""

from peewee import ModelSelect

from his import CUSTOMER
from mdb import Address, Company, Customer

from cmslib.messages.configuration import NO_SUCH_CONFIGURATION
from cmslib.orm.configuration import Configuration


__all__ = ['get_configuration', 'list_configurations']


def list_configurations() -> ModelSelect:
    """Returns the respective configuration."""

    select = Configuration.select(Configuration, Customer, Company, Address)
    select = select.join(Customer).join(Company).join(Address)
    return select.where(Configuration.customer == CUSTOMER.id)


def get_configuration(ident: int) -> Configuration:
    """Returns the respective configuration."""

    try:
        return list_configurations().where(Configuration.id == ident).get()
    except Configuration.DoesNotExist:
        raise NO_SUCH_CONFIGURATION from None
