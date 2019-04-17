"""Digital signage systems-related functions."""

from his import CUSTOMER
from terminallib import Deployment, System

from cmslib.messages.system import NO_SUCH_SYSTEM


__all__ = ['get_system', 'with_system']


def get_system(ident):
    """Returns the respective system."""

    try:
        return System.select().join(Deployment).where(
            (System.id == ident) & (Deployment.customer == CUSTOMER.id)).get()
    except System.DoesNotExist:
        raise NO_SUCH_SYSTEM


def with_system(function):
    """Decorator to pass a system ORM model
    derived from it's id to the wrapped function.
    """

    def wrapper(ident, *args, **kwargs):
        """Wraps the function."""
        return function(get_system(ident), *args, **kwargs)

    return wrapper
