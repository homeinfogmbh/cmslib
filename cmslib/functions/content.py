"""Content-related functions."""

from typing import Optional, Union

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
        deployment: Optional[Union[Deployment, int]] = None,
        trashed: Optional[bool] = None) -> ModelSelect:
    """Selects deployment base charts."""

    condition = BaseChart.customer == CUSTOMER.id

    if deployment is not None:
        condition &= DeploymentBaseChart.deployment == deployment

    if trashed is not None:
        condition &= BaseChart.trashed == trashed

    return DeploymentBaseChart.select(cascade=True).where(condition)


def get_deployment_configurations(
        deployment: Optional[Union[Deployment, int]] = None) -> ModelSelect:
    """Selects deployment configurations."""

    condition = Configuration.customer == CUSTOMER.id

    if deployment is not None:
        condition &= DeploymentConfiguration.deployment == deployment

    return DeploymentConfiguration.select(cascade=True).where(condition)


def get_deployment_menus(deployment: Optional[Union[Deployment, int]] = None
        ) -> ModelSelect:
    """Selects deployment menus."""

    condition = Menu.customer == CUSTOMER.id

    if deployment is not None:
        condition &= DeploymentMenu.deployment == deployment

    return DeploymentMenu.select(cascade=True).where(condition)


def get_group_base_charts(
        group: Optional[Union[Group, int]] = None,
        trashed: Optional[bool] = None) -> ModelSelect:
    """Selects deployment base charts."""

    condition = BaseChart.customer == CUSTOMER.id

    if group is not None:
        condition &= GroupBaseChart.group == group

    if trashed is not None:
        condition &= BaseChart.trashed == trashed

    return GroupBaseChart.select(cascade=True).where(condition)


def get_group_configurations(group: Optional[Union[Group, int]] = None
        ) -> ModelSelect:
    """Selects deployment configurations."""

    condition = Configuration.customer == CUSTOMER.id

    if group is not None:
        condition &= GroupConfiguration.group == group

    return GroupConfiguration.select(cascade=True).where(condition)


def get_group_menus(group: Optional[Union[Group, int]] = None) -> ModelSelect:
    """Selects deployment menus."""

    condition = Menu.customer == CUSTOMER.id

    if group is not None:
        condition &= GroupMenu.group == group

    return GroupMenu.select(cascade=True).where(condition)
