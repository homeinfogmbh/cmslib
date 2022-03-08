"""Deployment-related functions."""

from collections import defaultdict
from typing import Any, Callable, Iterable, Iterator, NamedTuple, Union

from peewee import Expression, Select

from his import CUSTOMER
from hwdb import Deployment, System
from mdb import Customer

from cmslib.orm.charts import BaseChart
from cmslib.orm.configuration import Configuration
from cmslib.orm.content.deployment import DeploymentBaseChart
from cmslib.orm.content.deployment import DeploymentConfiguration
from cmslib.orm.content.deployment import DeploymentMenu
from cmslib.orm.menu import Menu


__all__ = ['get_deployment', 'get_deployments', 'with_deployment']


class AssocDeployment(NamedTuple):
    """Deployment with associated data."""

    deployment: Deployment
    deployment_base_charts: dict[int, list[DeploymentBaseChart]]
    deployment_configurations: dict[int, list[DeploymentConfiguration]]
    deployment_menus: dict[int, list[DeploymentMenu]]
    systems_map: dict[int, list[int]]

    def __getattr__(self, item):
        return getattr(self.deployment, item)

    def to_json(self, **kwargs) -> dict[str, Any]:
        """Returns a JSON-ish dict."""
        deployment = self.deployment.to_json(address=True, **kwargs)
        deployment['systems'] = self.systems_map.get(self.deployment.id, [])
        return {
            'deployment': deployment,
            'content': {
                'charts': [
                    dbc.chart.to_json() for dbc in
                    self.deployment_base_charts.get(self.deployment.id, [])
                ],
                'configurations': [
                    dep_conf.to_json() for dep_conf in
                    self.deployment_configurations.get(self.deployment.id, [])
                ],
                'menus': [
                    deployment_menu.to_json() for deployment_menu in
                    self.deployment_menus.get(self.deployment.id, [])
                ]
            }
        }


class AssocDeployments:
    """Deployments with associated data."""

    def __init__(
            self,
            deployments: Iterable[Deployment],
            trashed: Union[Expression, bool] = True
    ):
        """Sets the deployments and trashed expression for charts."""
        self.deployments = deployments
        self.trashed = trashed

    def __iter__(self) -> Iterator[AssocDeployment]:
        deployment_base_charts_map = self.deployment_base_charts_map
        deployment_configurations_map = self.deployment_configurations_map
        deployment_menus_map = self.deployment_menus_map
        systems_map = self.systems_map

        for deployment in self.deployments:
            yield AssocDeployment(
                deployment,
                deployment_base_charts_map,
                deployment_configurations_map,
                deployment_menus_map,
                systems_map
            )

    @property
    def ids(self) -> set[int]:
        """Returns the deployment IDs."""
        return {deployment.id for deployment in self.deployments}

    @property
    def deployment_base_charts(self) -> Select:
        """Selects deployment base charts for the respective deployments."""
        return DeploymentBaseChart.select().join(BaseChart).where(
            (DeploymentBaseChart.deployment << self.ids) & self.trashed
        )

    @property
    def deployment_configurations(self) -> Select:
        """Selects deployment configurations of the respective deployments."""
        return DeploymentConfiguration.select().where(
            DeploymentConfiguration.deployment << self.ids
        )

    @property
    def deployment_menus(self) -> Select:
        """Selects deployment menus of the respective deployments."""
        return DeploymentMenu.select().where(
            DeploymentMenu.deployment << self.ids
        )

    @property
    def systems(self) -> Select:
        """Selects systems of the respective deployments."""
        return System.select().where(System.deployment << self.ids)

    @property
    def deployment_base_charts_map(self) -> dict[int, list[BaseChart]]:
        """Returns a map of deployments and base charts."""
        result = defaultdict(list)

        for dbc in self.deployment_base_charts:
            result[dbc.deployment_id].append(dbc)

        return result

    @property
    def deployment_configurations_map(self) -> dict[int, list[Configuration]]:
        """Returns a map of deployments and configurations."""
        result = defaultdict(list)

        for dep_conf in self.deployment_configurations:
            result[dep_conf.deployment_id].append(dep_conf)

        return result

    @property
    def deployment_menus_map(self) -> dict[int, list[Menu]]:
        """Returns a map of deployments and menus."""
        result = defaultdict(list)

        for deployment_menu in self.deployment_menus:
            result[deployment_menu.deployment_id].append(deployment_menu)

        return result

    @property
    def systems_map(self) -> dict[int, list[int]]:
        """Returns a map of deployments and system IDs."""
        result = defaultdict(list)

        for system in self.systems:
            if deployment := system.deployment_id:
                result[deployment].append(system.id)

        return result


def get_deployment(ident: int, customer: Union[Customer, int]) -> Deployment:
    """Returns the respective deployment."""

    return get_deployments(customer).where(Deployment.id == ident).get()


def get_deployments(
        customer: Union[Customer, int],
        testing: bool = True,
        content: bool = False,
        trashed: Union[Expression, bool] = False
) -> Union[Select, AssocDeployments]:
    """Selects the deployments of the current customer."""

    condition = Deployment.customer == customer

    if not testing:
        condition &= Deployment.testing == 0

    deployments = Deployment.select(cascade=True).where(condition)

    if not content:
        return deployments

    return AssocDeployments(deployments, trashed=trashed)


def with_deployment(function: Callable) -> Callable:
    """Decorator to pass a deployment ORM model
    derived from its id to the wrapped function.
    """

    def wrapper(ident: int, *args, **kwargs):
        """Wraps the function."""
        return function(get_deployment(ident, CUSTOMER.id), *args, **kwargs)

    return wrapper
