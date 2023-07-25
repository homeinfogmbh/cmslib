"""Content-related functions."""

from typing import Optional, Union

from peewee import Expression, Select

from mdb import Customer
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
    "get_deployment_base_charts",
    "get_deployment_base_chart",
    "get_deployment_configurations",
    "get_deployment_configuration",
    "get_deployment_menus",
    "get_deployment_menu",
    "get_group_base_charts",
    "get_group_base_chart",
    "get_group_configurations",
    "get_group_configuration",
    "get_group_menus",
    "get_group_menu",
]


def get_deployment_base_chart(
    ident: int, customer: Union[Customer, int]
) -> DeploymentBaseChart:
    """Returns the respective deployment base chart of the given customer."""

    return (
        get_deployment_base_charts(customer)
        .where(DeploymentBaseChart.id == ident)
        .get()
    )


def get_deployment_base_charts(
    customer: Union[Customer, int],
    deployment: Optional[Union[Deployment, int]] = None,
    trashed: Union[Expression, bool] = True,
) -> Select:
    """Selects deployment base charts of the given customer.

    Optionally filter deployment base charts for the given deployment.
    """

    condition = (BaseChart.customer == customer) & trashed

    if deployment is not None:
        condition &= DeploymentBaseChart.deployment == deployment

    return DeploymentBaseChart.select(cascade=True).where(condition)


def get_deployment_configuration(
    ident: int, customer: Union[Customer, int]
) -> DeploymentConfiguration:
    """Returns the respective deployment
    configuration for the given customer.
    """

    return (
        get_deployment_configurations(customer)
        .where(DeploymentConfiguration.id == ident)
        .get()
    )


def get_deployment_configurations(
    customer: Union[Customer, int], deployment: Optional[Union[Deployment, int]] = None
) -> Select:
    """Selects deployment configurations of the given customer."""

    condition = Configuration.customer == customer

    if deployment is not None:
        condition &= DeploymentConfiguration.deployment == deployment

    return DeploymentConfiguration.select(cascade=True).where(condition)


def get_deployment_menu(ident: int, customer: Union[Customer, int]) -> DeploymentMenu:
    """Returns the respective deployment menu of the given customer."""

    return get_deployment_menus(customer).where(DeploymentMenu.id == ident).get()


def get_deployment_menus(
    customer: Union[Customer, int], deployment: Optional[Union[Deployment, int]] = None
) -> Select:
    """Selects deployment menus of the given customer."""

    condition = Menu.customer == customer

    if deployment is not None:
        condition &= DeploymentMenu.deployment == deployment

    return DeploymentMenu.select(cascade=True).where(condition)


def get_group_base_chart(ident: int, customer: Union[Customer, int]) -> GroupBaseChart:
    """Returns the respective group base chart of the given customer."""

    return get_group_base_charts(customer).where(GroupBaseChart.id == ident).get()


def get_group_base_charts(
    customer: Union[Customer, int],
    group: Optional[Union[Group, int]] = None,
    trashed: Union[Expression, bool] = True,
) -> Select:
    """Selects deployment base charts of the given customer.

    Optionally filter group base charts of the given groups.
    """

    condition = (BaseChart.customer == customer) & trashed

    if group is not None:
        condition &= GroupBaseChart.group == group

    return GroupBaseChart.select(cascade=True).where(condition)


def get_group_configuration(
    ident: int, customer: Union[Customer, int]
) -> GroupConfiguration:
    """Returns the respective group configuration of the given customer."""

    return (
        get_group_configurations(customer).where(GroupConfiguration.id == ident).get()
    )


def get_group_configurations(
    customer: Union[Customer, int], group: Optional[Union[Group, int]] = None
) -> Select:
    """Selects deployment configurations of the given customer."""

    condition = Configuration.customer == customer

    if group is not None:
        condition &= GroupConfiguration.group == group

    return GroupConfiguration.select(cascade=True).where(condition)


def get_group_menu(ident: int, customer: Union[Customer, int]) -> GroupMenu:
    """Returns the respective group menu of the given customer."""

    return get_group_menus(customer).where(GroupMenu.id == ident).get()


def get_group_menus(
    customer: Union[Customer, int], group: Optional[Union[Group, int]] = None
) -> Select:
    """Selects deployment menus of the given customer."""

    condition = Menu.customer == customer

    if group is not None:
        condition &= GroupMenu.group == group

    return GroupMenu.select(cascade=True).where(condition)
