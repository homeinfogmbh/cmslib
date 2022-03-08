"""Group related functions."""

from typing import Iterator, Optional, Union

from peewee import Select

from hwdb import Deployment
from mdb import Customer

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


def get_group(ident: int, customer: Union[Customer, int]) -> Group:
    """Returns the respective group of the given customer."""

    return get_groups(customer).where(Group.id == ident).get()


def get_groups(customer: Union[Customer, int]) -> Select:
    """Selects the groups of the given customer."""

    return Group.select(cascade=True).where(Group.customer == customer)


def get_group_member_deployment(
        ident: int,
        customer: Union[Customer, int]
) -> GroupMemberDeployment:
    """Selects a group members deployment for the given customer."""

    return get_group_member_deployments(customer).where(
        GroupMemberDeployment.id == ident
    ).get()


def get_group_member_deployments(
        customer: Union[Customer, int],
        group: Optional[Union[Group, int]] = None
) -> Select:
    """Selects group member deployments for the given customer."""

    condition = Group.customer == customer

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
