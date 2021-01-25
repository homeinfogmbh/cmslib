"""Group utilities."""

from __future__ import annotations
from itertools import zip_longest
from typing import Iterable, Iterator, List, Optional, Union

from mdb import Customer

from cmslib.orm.group import Group


__all__ = ['Groups']


def key(group: Group) -> int:
    """Returns a sorting key for a given group."""

    return group.index


class Groups:
    """Wraps customer groups."""

    def __init__(self, groups: Iterable[Group]):
        """Initializes the customer groups wrapper."""
        self.groups = groups

    @classmethod
    def for_customer(cls, customer: Union[Customer, int]) -> Groups:
        """Selects the customer groups."""
        groups = Group.select(cascade=True).where(Group.customer == customer)
        return cls(groups)

    def tree(self, root: Optional[Group] = None) -> dict:
        """Returns a top-down group tree."""
        if root is None:
            toplevel = filter(lambda group: group.parent is None, self.groups)
            return sorted((self.tree(group) for group in toplevel), key=key)

        children = filter(lambda group: group.parent == root, self.groups)
        return {
            root: sorted((self.tree(child) for child in children), key=key)
        }

    def parents(self, group: Group) -> Iterator[Group]:
        """Yields parents of the given group."""
        groups = {group.id: group for group in self.groups}

        while group.parent is not None:
            parent = groups[group.parent]
            yield parent

    def rtree(self, leaf: Group) -> Iterator[Group]:
        """Yields the group and its parents."""
        yield leaf
        yield from self.parents(leaf)

    def levels(self, leafs: Iterable[Group]) -> Iterator[List[Group]]:
        """Yields levels of groups up from this group."""
        for level in zip_longest(*(self.rtree(leaf) for leaf in leafs)):
            yield sorted(filter(None, level), key=key)
