"""Deployment-related functions."""

from typing import Callable

from peewee import JOIN, Select

from his import CUSTOMER
from hwdb import Deployment

from cmslib.functions.charts import get_trashed
from cmslib.orm.charts import BaseChart
from cmslib.orm.content.deployment import DeploymentBaseChart
from cmslib.orm.content.deployment import DeploymentConfiguration
from cmslib.orm.content.deployment import DeploymentMenu


__all__ = ['get_deployment', 'get_deployments', 'with_deployment']


class AssocDeployment:
    """Deployment with associated data."""


def get_deployment(ident: int) -> Deployment:
    """Returns the respective deployment."""

    return get_deployments().where(Deployment.id == ident).get()


def get_deployments(content: bool = False) -> Select:
    """Selects the deployments of the current customer."""

    condition = Deployment.customer == CUSTOMER.id
    select = Deployment.select(cascade=True)

    if not content:
        return select.where(condition).distinct()

    condition &= get_trashed()

    return select.join_from(
        Deployment, DeploymentBaseChart, join_type=JOIN.LEFT_OUTER).join(
        BaseChart, join_type=JOIN.LEFT_OUTER).join_from(
        Deployment, DeploymentConfiguration,
        join_type=JOIN.LEFT_OUTER).join_from(
        Deployment, DeploymentMenu, join_type=JOIN.LEFT_OUTER
    ).where(condition).distinct()


def with_deployment(function: Callable) -> Callable:
    """Decorator to pass a deployment ORM model
    derived from its id to the wrapped function.
    """

    def wrapper(ident: int, *args, **kwargs):
        """Wraps the function."""
        return function(get_deployment(ident), *args, **kwargs)

    return wrapper
