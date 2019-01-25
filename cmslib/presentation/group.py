"""Content accumulation for groups."""

from cmslib.exceptions import NoConfigurationFound
from cmslib.presentation.common import PresentationMixin


__all__ = ['Presentation']


class Presentation(PresentationMixin):
    """Accumulates content for a group."""

    def __init__(self, group):
        """Sets the respective group."""
        self.group = group
        self.cache = {}

    @property
    def customer(self):
        """Returns the respective customer."""
        return self.group.customer

    @property
    def base_charts(self):
        """Yields the terminal's base charts."""
        return ()   # Handled by group_base_charts.

    @property
    def configuration(self):
        """Returns the group's direct configuratioin."""
        raise NoConfigurationFound()    # Handled by groupconfigs.

    @property
    def groups(self):
        """Yields all groups in a breadth-first search."""
        # Need to start with itself to include the
        # group itself in all group-related methods.
        yield self.group

    @property
    def menus(self):
        """Yields menus of this terminal."""
        return ()   # Handled by group_menus.
