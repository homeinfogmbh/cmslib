"""Group related functions."""

from typing import Callable, Iterable, Iterator, Optional, Union

from peewee import Select

from his import CUSTOMER
from hwdb import Deployment

from cmslib.orm.group import Group, GroupMemberDeployment


__all__ = [
    'get_group',
    'get_groups',
    'get_group_member_deployment',
    'get_group_member_deployments',
    'get_groups_of'
]


def get_group(ident: int) -> Group:
    """Returns the respective group of the current customer."""

    return get_groups().where(Group.id == ident).get()


def get_groups() -> Select:
    """Selects the groups of the current customer."""

    return Group.select(cascade=True).where(Group.customer == CUSTOMER.id)


def get_group_member_deployment(ident: int) -> GroupMemberDeployment:
    """Selects group members deployments."""

    return get_group_member_deployments().where(
        GroupMemberDeployment.id == ident).get()


def get_group_member_deployments(
        group: Optional[Union[Group, int]] = None
) -> Select:
    """Selects group members deployments."""

    condition = Group.customer == CUSTOMER.id

    if group is not None:
        condition &= GroupMemberDeployment.group == group

    return GroupMemberDeployment.select(cascade=True).where(condition)


def get_groups_of(deployment: Union[Deployment, int]) -> Select:
    """Select groups of the given deployment."""

    return Group.select(cascade=True).join_from(
        Group, GroupMemberDeployment,
        on=GroupMemberDeployment.group == Group.id
    ).where(GroupMemberDeployment.deployment == deployment)
