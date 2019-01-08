"""Content accumulation for groups."""

from functoolsplus import cached_method, coerce    # pylint: disable=E0401

from cmslib.exceptions import AmbiguousConfigurationsError
from cmslib.exceptions import NoConfigurationFound
from cmslib.orm.charts import BaseChart
from cmslib.orm.configuration import Configuration
from cmslib.orm.content.group import GroupBaseChart
from cmslib.orm.content.group import GroupConfiguration
from cmslib.orm.content.group import GroupMenu
from cmslib.orm.menu import Menu

from cmslib.presentation.common import charts
from cmslib.presentation.common import indexify
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
    @cached_method()
    @coerce(frozenset)
    def groups(self):
        """Yields all groups in a breadth-first search."""
        parent = self.group

        while parent:
            yield parent
            parent = parent.parent

    @property
    def groupconfigs(self):
        """Returns a configuration for the terminal's groups."""
        for index, group in enumerate(self.groups):
            group_configs = Configuration.select().join(
                GroupConfiguration).where(GroupConfiguration.group == group)

            try:
                configuration, *superfluous = group_configs
            except ValueError:
                continue

            if superfluous:
                raise AmbiguousConfigurationsError((group,), index)

            yield configuration

        raise NoConfigurationFound()

    @property
    def configuration(self):
        """Returns the terminal's configuration."""
        for configuration in self.groupconfigs:
            return configuration

        raise NoConfigurationFound()

    @property
    @cached_method()
    @coerce(frozenset)
    def menus(self):
        """Yields menus of this terminal."""
        yield from Menu.select().join(GroupMenu).where(
            GroupMenu.group << self.groups)
    @property
    @cached_method()
    @coerce(charts)
    def playlist(self):
        """Yields the terminal's base charts."""
        gbcs = GroupBaseChart.select().join(BaseChart).where(
            (GroupBaseChart.group << self.groups)
            & (BaseChart.trashed == 0)).order_by(GroupBaseChart.index)

        for base_chart_mapping in sorted(gbcs, key=indexify):
            yield base_chart_mapping.base_chart
