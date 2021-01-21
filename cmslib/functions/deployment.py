"""Deployment-related functions."""

from typing import Callable

from peewee import ModelSelect

from his import CUSTOMER
from hwdb import Deployment
from mdb import Address, Company, Customer


__all__ = ['get_deployment', 'get_deployments', 'with_deployment']


def get_deployments() -> ModelSelect:
    """Selects the deployments of the current customer."""

    deployment_address = Address.alias()
    lpt_address = Address.alias()
    select = Deployment.select(
        Deployment, Customer, Company, Address, deployment_address,
        lpt_address).join(Customer).join(Company).join(Address).join_from(
        Deployment, deployment_address,
        on=Deployment.address == deployment_address.id).join_from(
        Deployment, lpt_address, on=Deployment.lpt_address == lpt_address.id)
    return select.where(Deployment.customer == CUSTOMER.id)


def get_deployment(ident: int) -> Deployment:
    """Returns the respective deployment."""

    return get_deployments().where(Deployment.id == ident).get()


def with_deployment(function: Callable) -> Callable:
    """Decorator to pass a deployment ORM model
    derived from it's id to the wrapped function.
    """

    def wrapper(ident: int, *args, **kwargs):
        """Wraps the function."""
        return function(get_deployment(ident), *args, **kwargs)

    return wrapper
