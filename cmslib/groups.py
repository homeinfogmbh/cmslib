"""Group utilities."""

from __future__ import annotations
from itertools import zip_longest
from typing import Iterable, Iterator, Optional, Union

from mdb import Customer

from cmslib.orm.group import Group


__all__ = ['Groups']


def sort_by_index(groups: Iterable[Group]) -> list[Group]:
    """Sorts the given groups by index."""

    return sorted(groups, key=lambda group: group.index)


def get_ids(ids_or_groups: Iterable[Union[int, Group]]) -> Iterator[int]:
    """Yields IDs from IDs or groups."""

    for item in ids_or_groups:
        if isinstance(item, int):
            yield item
        elif isinstance(item, Group):
            yield item.id
        else:
            raise TypeError(f'Not a group or ID: {item}')


class Groups:
    """Wraps groups."""

    def __init__(self, groups: Iterable[Group]):
        self._groups = {group.id: group for group in groups}

    @classmethod
    def for_customer(cls, customer: Union[Customer, int]) -> Groups:
        """Creates a Groups object from groups of the given customer."""
        return cls(
            Group.select(cascade=True).where(Group.customer == customer)
        )

    @property
    def toplevel(self) -> Iterator[Group]:
        """Yields groups that do not have parents."""
        return filter(lambda grp: grp.parent is None, self._groups.values())

    def groups(self, ids_or_groups: Iterable[Union[Group, int]]) -> set[Group]:
        """Yields groups with the given IDs."""
        return {
            group for ident, group in self._groups.items()
            if ident in set(get_ids(ids_or_groups))
        }

    def group(self, ident: int) -> Group:
        """Returns the group with the given ID."""
        try:
            return self._groups[ident]
        except KeyError as key_error:
            raise Group.DoesNotExist() from key_error

    def children_of(self, parent: Group) -> Iterator[Group]:
        """Yields the children of the given group."""
        return filter(lambda grp: grp.parent == parent, self._groups.values())

    def tree(self, root: Optional[Group] = None) -> Union[list, dict]:
        """Returns a top-down group tree."""
        if root is None:
            return sort_by_index(map(self.tree, self.toplevel))

        return {
            root: sort_by_index(map(self.tree, self.children_of(root)))
        }

    def parents(self, group: Group) -> Iterator[Group]:
        """Yields parents of the given group."""
        while group := self._groups.get(group.parent_id):
            yield group

    def lineage(self, group: Group) -> Iterator[Group]:
        """Yields the group and its parents."""
        yield group
        yield from self.parents(group)

    def levels(self, groups: Iterable[Group]) -> Iterator[list[Group]]:
        """Yields levels of groups up from this group."""
        for level in zip_longest(*(self.lineage(group) for group in groups)):
            yield sort_by_index(filter(None, level))
