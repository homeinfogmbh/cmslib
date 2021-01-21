"""Content-related functions."""

from typing import Union

from peewee import ModelSelect

from his import CUSTOMER
from hwdb import Deployment

from cmslib.orm.charts import BaseChart
from cmslib.orm.configuration import Configuration
from cmslib.orm.content.deployment import DeploymentBaseChart
from cmslib.orm.content.deployment import DeploymentConfiguration
from cmslib.orm.content.deployment import DeploymentMenu
from cmslib.orm.content.group import GroupBaseChart
from cmslib.orm.content.group import GroupConfiguration
from cmslib.orm.content.group import GroupMenu
from cmslib.orm.group import Group
from cmslib.orm.menu import Menu


__all__ = [
    'get_deployment_base_charts',
    'get_deployment_configurations',
    'get_deployment_menus',
    'get_group_base_charts',
    'get_group_configurations',
    'get_group_menus'
]


def get_deployment_base_charts(
        deployment: Union[Deployment, int]) -> ModelSelect:
    """Selects deployment base charts."""

    return DeploymentBaseChart.select(cascade=True).where(
        (DeploymentBaseChart.deployment == deployment)
        & (BaseChart.customer == CUSTOMER.id))


def get_deployment_configurations(
        deployment: Union[Deployment, int]) -> ModelSelect:
    """Selects deployment configurations."""

    return DeploymentConfiguration.select(cascade=True).where(
        (DeploymentConfiguration.deployment == deployment)
        & (Configuration.customer == CUSTOMER.id))


def get_deployment_menus(deployment: Union[Deployment, int]) -> ModelSelect:
    """Selects deployment menus."""

    return DeploymentMenu.select(cascade=True).where(
        (DeploymentMenu.deployment == deployment)
        & (Menu.customer == CUSTOMER.id))


def get_group_base_charts(group: Union[Group, int]) -> ModelSelect:
    """Selects deployment base charts."""

    return GroupBaseChart.select(cascade=True).where(
        (GroupBaseChart.group == group)
        & (BaseChart.customer == CUSTOMER.id))


def get_group_configurations(group: Union[Group, int]) -> ModelSelect:
    """Selects deployment configurations."""

    return GroupConfiguration.select(cascade=True).where(
        (GroupConfiguration.group == group)
        & (Configuration.customer == CUSTOMER.id))


def get_group_menus(group: Union[Group, int]) -> ModelSelect:
    """Selects deployment menus."""

    return GroupMenu.select(cascade=True).where(
        (GroupMenu.group == group) & (Menu.customer == CUSTOMER.id))
