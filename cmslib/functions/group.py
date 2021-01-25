"""Group related functions."""

from typing import Iterable, Optional, Union

from peewee import ModelSelect

from his import CUSTOMER

from cmslib.orm.group import Group, GroupMemberDeployment


__all__ = [
    'get_group',
    'get_groups',
    'get_group_member_deployment',
    'get_group_member_deployments',
    'get_tree'
]


def get_groups() -> ModelSelect:
    """Selects the groups of the current customer."""

    return Group.select(cascade=True).where(Group.customer == CUSTOMER.id)


def get_group(ident: int) -> Group:
    """Returns the respective group of the current customer."""

    return get_groups().where(Group.id == ident).get()


def get_group_member_deployments(
        group: Optional[Union[Group, int]] = None) -> ModelSelect:
    """Selects group members deployments."""

    condition = Group.customer == CUSTOMER.id

    if group is not None:
        condition &= GroupMemberDeployment.group == group

    return GroupMemberDeployment.select(cascade=True).where(condition)


def get_group_member_deployment(ident: int) -> GroupMemberDeployment:
    """Selects group members deployments."""

    return get_group_member_deployments().where(
        GroupMemberDeployment.id == ident).get()


def get_children(groups: Iterable[Group], group: Group) -> dict:
    """Returns the children of the group."""

    children = filter(lambda child: child.parent == group, groups)
    return {child: get_children(groups, child) for child in children}


def get_tree(groups: Iterable[Group], ident: Optional[int] = None) -> dict:
    """Returns a dict of groups representing the groups tree."""

    if ident is None:
        condition = lambda group: group.parent is None
    else:
        condition = lambda group: group.id == ident

    return {
        root: get_children(groups, root)
        for root in filter(condition, groups)
    }
