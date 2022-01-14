"""Group related functions."""

from typing import Callable, Iterable, Iterator, Optional, Union

from peewee import Select

from his import CUSTOMER

from cmslib.orm.group import Group, GroupMemberDeployment


__all__ = [
    'get_group',
    'get_groups',
    'get_group_member_deployment',
    'get_group_member_deployments',
    'get_tree'
]


def get_parent(group: Group, groups: dict[int, Group]) -> Optional[Group]:
    """Returns the parent of the group from the given groups."""

    if group.parent_id is None:
        return None

    return groups.get(group.parent_id)


def get_lineage(
        group: Union[Group, int], *,
        groups: Optional[dict[int, Group]] = None,
        include_group: bool = True
) -> Iterator[Group]:
    """Returns the given group and all of
    its parents throughout its lineage.
    """

    if isinstance(group, int):
        group = Group[group]

    if groups is None:
        groups = {
            group.id: group for group in
            Group.select().where(Group.customer == group.customer)
        }

    if include_group:
        yield group

    while group := get_parent(group.parent_id, groups):
        yield group


def get_children(groups: Iterable[Group], parent: Group) -> list[Group]:
    """Returns the children of the group."""

    return sorted(
        filter(lambda group: group.parent == parent, groups),
        key=lambda group: group.index
    )


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


def get_condition(ident: Optional[int]) -> Callable[[Group], bool]:
    """Returns a group filtering condition for get_tree()"""

    if ident is None:
        return lambda group: group.parent is None

    return lambda group: group.id == ident


def get_tree(
        groups: Iterable[Group], ident: Optional[int] = None
) -> dict:
    """Returns a dict of groups representing the groups tree."""

    return {
        root: get_children(groups, root)
        for root in filter(get_condition(ident), groups)
    }
