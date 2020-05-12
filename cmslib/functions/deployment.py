"""Deployment-related functions."""

from his import CUSTOMER
from terminallib import Deployment

from cmslib.messages.deployment import NO_SUCH_DEPLOYMENT


__all__ = ['get_deployment', 'with_deployment']


def get_deployment(ident):
    """Returns the respective deployment."""

    condition = Deployment.id == ident
    condition &= Deployment.customer == CUSTOMER.id

    try:
        return Deployment.get(condition)
    except Deployment.DoesNotExist:
        raise NO_SUCH_DEPLOYMENT


def with_deployment(function):
    """Decorator to pass a deployment ORM model
    derived from it's id to the wrapped function.
    """

    def wrapper(ident, *args, **kwargs):
        """Wraps the function."""
        return function(get_deployment(ident), *args, **kwargs)

    return wrapper
