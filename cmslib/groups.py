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


class Groups:
    """Wraps groups."""

    def __init__(self, groups: Iterable[Group]):
        self.groups = groups

    @classmethod
    def for_customer(cls, customer: Union[Customer, int]) -> Groups:
        """Creates a Groups object from groups of the given customer."""
        return cls(
            Group.select(cascade=True).where(Group.customer == customer)
        )

    @property
    def toplevel(self) -> Iterator[Group]:
        """Yields groups that do not have parents."""
        return filter(lambda group: group.parent is None, self.groups)

    def children_of(self, parent: Group) -> Iterator[Group]:
        """Yields the children of the given group."""
        return filter(lambda group: group.parent == parent, self.groups)

    def tree(self, root: Optional[Group] = None) -> Union[list, dict]:
        """Returns a top-down group tree."""
        if root is None:
            return sort_by_index(map(self.tree, self.toplevel))

        return {
            root: sort_by_index(map(self.tree, self.children_of(root)))
        }

    def parents(self, group: Group) -> Iterator[Group]:
        """Yields parents of the given group."""
        groups = {group.id: group for group in self.groups}

        while group := groups.get(group.parent_id):
            yield group

    def lineage(self, group: Group) -> Iterator[Group]:
        """Yields the group and its parents."""
        yield group
        yield from self.parents(group)

    def levels(self, groups: Iterable[Group]) -> Iterator[list[Group]]:
        """Yields levels of groups up from this group."""
        for level in zip_longest(*(self.lineage(group) for group in groups)):
            yield sort_by_index(filter(None, level))
