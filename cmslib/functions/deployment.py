"""Deployment-related functions."""

from typing import Callable

from peewee import ModelSelect

from his import CUSTOMER
from hwdb import Deployment


__all__ = ['get_deployment', 'get_deployments', 'with_deployment']


def get_deployment(ident: int) -> Deployment:
    """Returns the respective deployment."""

    return get_deployments().where(Deployment.id == ident).get()


def get_deployments() -> ModelSelect:
    """Selects the deployments of the current customer."""

    return Deployment.select(cascade=True).where(
        Deployment.customer == CUSTOMER.id)


def with_deployment(function: Callable) -> Callable:
    """Decorator to pass a deployment ORM model
    derived from it's id to the wrapped function.
    """

    def wrapper(ident: int, *args, **kwargs):
        """Wraps the function."""
        return function(get_deployment(ident), *args, **kwargs)

    return wrapper
