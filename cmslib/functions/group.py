"""Group related functions."""

from typing import Iterator, Optional, Union

from peewee import Select

from his import CUSTOMER
from hwdb import Deployment

from cmslib.orm.group import Group, GroupMemberDeployment
from cmslib.groups import Groups


__all__ = [
    'get_group',
    'get_groups',
    'get_group_member_deployment',
    'get_group_member_deployments',
    'get_group_ids',
    'get_groups_lineage'
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


def get_group_ids(deployment: Union[Deployment, int]) -> Iterator[int]:
    """Yield group IDs of the given deployment."""

    for group_member_deployment in GroupMemberDeployment.select().where(
            GroupMemberDeployment.deployment == deployment
    ):
        yield group_member_deployment.group


def get_groups_lineage(
        deployment: Union[Deployment, int], *,
        groups: Optional[Groups] = None
) -> Iterator[Group]:
    """Select the groups-lineage of the given user."""

    if groups is None:
        groups = Groups.for_customer(deployment.customer)

    for member_group in groups.groups(get_group_ids(deployment)):
        for group in groups.lineage(member_group):
            yield group
