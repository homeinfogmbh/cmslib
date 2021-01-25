"""Group related functions."""

from typing import Dict, Iterable, Optional, Union

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


def get_children(groups: Iterable[Group], group: Group) -> Dict[Group]:
    """Returns the children of the group."""

    return {
        child: list(get_children(groups, group))
        for child in filter(lambda child: child.parent == group, groups)
    }


def get_tree(ident: Optional[int] = None) -> Dict[Group]:
    """Returns a dict of groups representing the groups tree."""

    groups = Group.select(cascade=True).where(Group.customer == CUSTOMER.id)

    if ident is None:
        condition = lambda group: group.parent is None
    else:
        condition = lambda group: group.id == ident

    return {
        root: list(get_children(groups, root))
        for root in filter(condition, groups)
    }
