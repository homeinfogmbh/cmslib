"""Common functions."""

from contextlib import suppress
from functools import partial
from itertools import chain
from logging import getLogger

from functoolsplus import cached_method, coerce     # pylint: disable=E0401

from cmslib import dom  # pylint: disable=E0611
from cmslib.exceptions import AmbiguousBaseChart
from cmslib.exceptions import AmbiguousConfigurationsError
from cmslib.exceptions import NoConfigurationFound
from cmslib.exceptions import OrphanedBaseChart
from cmslib.menutree import merge, MenuTreeItem
from cmslib.orm.charts import BaseChart, ChartMode
from cmslib.orm.content.group import GroupBaseChart, GroupMenu
from cmslib.orm.configuration import Configuration
from cmslib.orm.content.group import GroupConfiguration
from cmslib.orm.menu import Menu, MenuItem, MenuItemChart


__all__ = [
    'charts',
    'identify',
    'indexify',
    'level_configs',
    'uniquesort',
    'PresentationMixin']


LOGGER = getLogger(__file__)


@coerce(tuple)
def charts(base_charts):
    """Yields the charts of the respective base charts."""

    for base_chart in base_charts:
        try:
            yield base_chart.chart
        except OrphanedBaseChart:
            LOGGER.error('Base chart is orphaned: %s.', base_chart)
        except AmbiguousBaseChart:
            LOGGER.error('Base chart is ambiguous: %s.', base_chart)


def identify(item):
    """Returns the item's ID."""

    return item.id


def indexify(item):
    """Returns the item's index."""

    return item.index


@coerce(frozenset)
def level_configs(level):
    """Yields all configurations of a certain group level."""

    return Configuration.select().join(GroupConfiguration).where(
        GroupConfiguration.group << level)


def uniquesort(iterable, *, key=None, reverse=False):
    """Uniquely sorts an iterable."""

    return sorted(frozenset(iterable), key=key, reverse=reverse)


class PresentationMixin:
    """Common presentation mixin."""

    @property
    def _configuration(self):
        """Returns the accumulated object's configuration."""
        with suppress(NoConfigurationFound):
            return self.configuration

        for configuration in self.groupconfigs:
            return configuration

        raise NoConfigurationFound()

    @property
    def _group_base_charts(self):
        """Charts attached to groups, the object is a member of."""
        return GroupBaseChart.select().join(BaseChart).where(
            (GroupBaseChart.group << self._groups)
            & (BaseChart.trashed == 0)).order_by(GroupBaseChart.index)

    @property
    @cached_method()
    @coerce(frozenset)
    def _groups(self):
        """Yields all groups in a breadth-first search."""
        for level in self.grouplevels:
            for group in level:
                yield group

    @property
    @cached_method()
    @coerce(frozenset)
    def _menus(self):
        """Yields the accumulated menus of this object."""
        return chain(self.menus, self.group_menus)

    @property
    @coerce(partial(uniquesort, key=identify))
    def charts(self):
        """Yields all charts for this object."""
        yield from self.playlist
        yield from self.menu_charts

    @property
    @cached_method()
    @coerce(frozenset)
    def files(self):
        """Yields the presentation's used file IDs."""
        yield from self._configuration.files

        for chart in self.charts:
            try:
                files = chart.files
            except AttributeError:
                continue

            yield from files

    @property
    def groupconfigs(self):
        """Returns a configuration for the object's groups."""
        for index, level in enumerate(self.grouplevels):
            try:
                configuration, *superfluous = level_configs(level)
            except ValueError:
                continue

            if superfluous:
                raise AmbiguousConfigurationsError(level, index)

            yield configuration

        raise NoConfigurationFound()

    @property
    def grouplevels(self):
        """Yields group levels in a breadth-first search."""
        level = frozenset(self.groups)

        while level:
            yield level
            level = frozenset(group.parent for group in level if group.parent)

    @property
    @cached_method()
    @coerce(charts)
    def menu_charts(self):
        """Yields charts of the object's menu."""
        yield from BaseChart.select().join(MenuItemChart).join(MenuItem).where(
            (BaseChart.trashed == 0) & (MenuItem.menu << self._menus))

    @property
    def group_menus(self):
        """Yields menus attached to groups the object is a member of."""
        return Menu.select().join(GroupMenu).where(
            GroupMenu.group << self._groups)

    @property
    def menutree(self):
        """Returns the merged menu tree."""
        items = chain(*(MenuTreeItem.from_menu(menu) for menu in self._menus))
        return sorted(merge(items), key=indexify)

    @property
    @cached_method()
    @coerce(charts)
    def playlist(self):
        """Yields the playlist."""
        base_charts = chain(self._group_base_charts, self.base_charts)

        for base_chart_mapping in sorted(base_charts, key=indexify):
            yield base_chart_mapping.base_chart

    def to_dom(self):
        """Returns an XML dom presentation."""
        xml = dom.presentation()
        xml.customer = self.customer.id
        xml.configuration = self._configuration.to_dom()
        xml.playlist = [chart.to_dom(brief=True) for chart in self.playlist]
        xml.menu_item = [item.to_dom() for item in self.menutree]
        xml.chart = [chart.to_dom() for chart in self.charts]
        return xml

    def to_json(self):
        """Returns a JSON presentation."""
        return {
            'customer': self.customer.id,
            'configuration': self._configuration.to_json(cascade=True),
            'playlist': [
                chart.to_json(mode=ChartMode.BRIEF)
                for chart in self.playlist],
            'menuItems': [item.to_json() for item in self.menutree],
            'charts': [chart.to_json() for chart in self.charts]}
