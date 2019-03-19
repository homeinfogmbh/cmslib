"""Configuration related functions."""

from his import CUSTOMER

from cmslib.messages.configuration import NO_SUCH_CONFIGURATION
from cmslib.orm.configuration import Configuration


__all__ = ['get_configuration', 'list_configurations']


def get_configuration(ident):
    """Returns the respective configuration."""

    try:
        return Configuration.get(
            (Configuration.customer == CUSTOMER.id)
            & (Configuration.id == ident))
    except Configuration.DoesNotExist:
        raise NO_SUCH_CONFIGURATION


def list_configurations():
    """Returns the respective configuration."""

    return Configuration.select().where(Configuration.customer == CUSTOMER.id)
