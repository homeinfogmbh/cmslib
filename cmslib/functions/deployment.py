"""Deployment-related functions."""

from collections import defaultdict
from typing import Any, Callable, Iterable, Iterator, NamedTuple, Union

from peewee import Expression, Select

from his import CUSTOMER
from hwdb import Deployment
from mdb import Customer

from cmslib.orm.charts import BaseChart
from cmslib.orm.configuration import Configuration
from cmslib.orm.content.deployment import DeploymentBaseChart
from cmslib.orm.content.deployment import DeploymentConfiguration
from cmslib.orm.content.deployment import DeploymentMenu
from cmslib.orm.menu import Menu


__all__ = ['get_deployment', 'get_deployments', 'with_deployment']


class AssocDeployment(NamedTuple):
    """An associated deployment."""

    deployment: Deployment
    base_charts_map: dict[Deployment, list[BaseChart]]
    configurations_map: dict[Deployment, list[Configuration]]
    menus_map: dict[Deployment, list[Menu]]

    def to_json(self, **kwargs) -> dict[str, Any]:
        """Returns a JSON-ish dict."""
        return {
            'deployment': self.deployment.to_json(**kwargs),
            'content': {
                'charts': [
                    base_chart.chart.to_json() for base_chart in
                    self.base_charts_map.get(self.deployment, [])
                ],
                'configurations': [
                    configuration.to_json() for configuration in
                    self.configurations_map.get(self.deployment, [])
                ],
                'menus': [
                    menu.to_json() for menu in
                    self.menus_map.get(self.deployment, [])
                ]
            }
        }


class AssocDeployments:
    """Deployment with associated data."""

    def __init__(
            self,
            deployments: Iterable[Deployment],
            trashed: Union[Expression, bool] = False
    ):
        """Sets the deployments and trashed expression for charts."""
        self.deployments = deployments
        self.trashed = trashed

    def __iter__(self) -> Iterator[AssocDeployment]:
        base_charts_map = self.base_charts_map
        configurations_map = self.configurations_map
        menus_map = self.menus_map

        for deployment in self.deployments:
            yield AssocDeployment(
                deployment, base_charts_map, configurations_map, menus_map
            )

    @property
    def deployment_base_charts(self) -> Select:
        """Selects deployment base charts for the respective deployments."""
        return DeploymentBaseChart.select(
            DeploymentBaseChart, BaseChart
        ).join(BaseChart).where(
            (DeploymentBaseChart.deployment << self.deployments) & self.trashed
        )

    @property
    def deployment_configurations(self) -> Select:
        """Selects deployment configurations of the respective deployments."""
        return DeploymentConfiguration.select(
            DeploymentConfiguration, Configuration
        ).join(Configuration).where(
            DeploymentConfiguration.deployment << self.deployments
        )

    @property
    def deployment_menus(self) -> Select:
        """Selects deployment menus of the respective deployments."""
        return DeploymentMenu.select(DeploymentMenu, Menu).join(Menu).where(
            DeploymentMenu.deployment << self.deployments
        )

    @property
    def base_charts_map(self) -> dict[Deployment, list[BaseChart]]:
        """Returns a map of deployments and base charts."""
        result = defaultdict(list)

        for dbc in self.deployment_base_charts:
            result[dbc.deployment].append(dbc.base_chart)

        return result

    @property
    def configurations_map(self) -> dict[Deployment, list[Configuration]]:
        """Returns a map of deployments and configurations."""
        result = defaultdict(list)

        for dep_conf in self.deployment_configurations:
            result[dep_conf.deployment].append(dep_conf.configuration)

        return result

    @property
    def menus_map(self) -> dict[Deployment, list[Menu]]:
        """Returns a map of deployments and menus."""
        result = defaultdict(list)

        for deployment_menu in self.deployment_menus:
            result[deployment_menu.deployment].append(deployment_menu.menu)

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

    deployments = Deployment.select(cascade=True).where(condition).distinct()

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
