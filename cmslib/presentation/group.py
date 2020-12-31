"""Content accumulation for groups."""

from typing import Iterable, Iterator

from mdb import Customer

from cmslib import dom  # pylint: disable=E0611
from cmslib.exceptions import NoConfigurationFound
from cmslib.orm.charts import BaseChart
from cmslib.orm.configuration import Configuration
from cmslib.orm.group import Group
from cmslib.orm.menu import Menu
from cmslib.presentation.common import PresentationMixin


__all__ = ['Presentation']


class Presentation(PresentationMixin):
    """Accumulates content for a group."""

    def __init__(self, group: Group):
        """Sets the respective group."""
        self.group = group
        self.cache = {}

    @property
    def customer(self) -> Customer:
        """Returns the respective customer."""
        return self.group.customer

    @property
    def base_charts(self) -> Iterable[BaseChart]:
        """Yields the group's base charts."""
        return ()   # Handled by group_base_charts.

    @property
    def configuration(self) -> Configuration:
        """Returns the group's direct configuratioin."""
        raise NoConfigurationFound()    # Handled by groupconfigs.

    @property
    def groups(self) -> Iterator[Group]:
        """Yields all groups in a breadth-first search."""
        # Need to start with itself to include the
        # group itself in all group-related methods.
        yield self.group

    @property
    def menus(self) -> Iterable[Menu]:
        """Yields menus of this group."""
        return ()   # Handled by group_menus.

    def to_dom(self) -> dom.presentation:
        """Returns an XML DOM."""
        xml = super().to_dom()
        xml.customer = self.customer.id
        xml.group = self.group.id
        return xml

    def to_json(self) -> dict:
        """Returns a JSON-ish dict."""
        json = super().to_json()
        json['group'] = self.group.id
        return json
