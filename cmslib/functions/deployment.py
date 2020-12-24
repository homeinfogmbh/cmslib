"""Deployment-related functions."""

from typing import Callable

from his import CUSTOMER
from hwdb import Deployment

from cmslib.messages.deployment import NO_SUCH_DEPLOYMENT


__all__ = ['get_deployment', 'with_deployment']


def get_deployment(ident: int) -> Deployment:
    """Returns the respective deployment."""

    condition = Deployment.id == ident
    condition &= Deployment.customer == CUSTOMER.id

    try:
        return Deployment.get(condition)
    except Deployment.DoesNotExist:
        raise NO_SUCH_DEPLOYMENT from None


def with_deployment(function: Callable) -> Callable:
    """Decorator to pass a deployment ORM model
    derived from it's id to the wrapped function.
    """

    def wrapper(ident: int, *args, **kwargs):
        """Wraps the function."""
        return function(get_deployment(ident), *args, **kwargs)

    return wrapper
