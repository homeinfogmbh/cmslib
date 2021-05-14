"""Deployment-related functions."""

from sys import stdout
from typing import Callable

from peewee import JOIN, ModelSelect

from functoolsplus import timeit
from his import CUSTOMER
from hwdb import Deployment

from cmslib.functions.charts import get_trashed
from cmslib.orm.charts import BaseChart
from cmslib.orm.content.deployment import DeploymentBaseChart
from cmslib.orm.content.deployment import DeploymentConfiguration
from cmslib.orm.content.deployment import DeploymentMenu


__all__ = ['get_deployment', 'get_deployments', 'with_deployment']


def get_deployment(ident: int) -> Deployment:
    """Returns the respective deployment."""

    return get_deployments().where(Deployment.id == ident).get()


@timeit(file=stdout, flush=True)
def get_deployments(content: bool = False) -> ModelSelect:
    """Selects the deployments of the current customer."""

    condition = Deployment.customer == CUSTOMER.id
    select = Deployment.select(cascade=True)

    if not content:
        return select.where(condition)

    condition &= get_trashed()

    return select.join_from(
        Deployment, DeploymentBaseChart, join_type=JOIN.LEFT_OUTER).join(
        BaseChart).join_from(
        Deployment, DeploymentConfiguration,
        join_type=JOIN.LEFT_OUTER).join_from(
        Deployment, DeploymentMenu, join_type=JOIN.LEFT_OUTER
    ).where(condition)


def with_deployment(function: Callable) -> Callable:
    """Decorator to pass a deployment ORM model
    derived from it's id to the wrapped function.
    """

    def wrapper(ident: int, *args, **kwargs):
        """Wraps the function."""
        return function(get_deployment(ident), *args, **kwargs)

    return wrapper
