"""Common functions."""

from contextlib import suppress
from functools import lru_cache, partial
from itertools import chain
from logging import getLogger
from typing import Any, Callable, Iterable, Iterator, Set

from peewee import ModelSelect

from filedb import File as FileDBFile
from functoolsplus import coerce    # pylint: disable=E0401
from hisfs import File

from cmslib import dom  # pylint: disable=E0611
from cmslib.exceptions import AmbiguousBaseChart
from cmslib.exceptions import AmbiguousConfigurationsError
from cmslib.exceptions import NoConfigurationFound
from cmslib.exceptions import OrphanedBaseChart
from cmslib.menutree import merge, MenuTreeItem
from cmslib.orm.charts import BaseChart, ChartMode, Chart
from cmslib.orm.content.group import GroupBaseChart, GroupMenu
from cmslib.orm.configuration import Configuration
from cmslib.orm.content.group import GroupConfiguration
from cmslib.orm.group import Group
from cmslib.orm.menu import Menu, MenuItem, MenuItemChart


__all__ = ['PresentationMixin']


LOGGER = getLogger(__file__)


def get_files(ids: Iterator[int]) -> ModelSelect:
    """Yields files from their IDs."""

    return File.select(File, FileDBFile).join(FileDBFile).where(
        File.id << set(ids))


@coerce(tuple)
def resolve_charts(base_charts: Iterable[BaseChart]) -> Iterator[Chart]:
    """Yields the charts of the respective base charts."""

    for base_chart in base_charts:
        try:
            yield base_chart.chart
        except OrphanedBaseChart:
            LOGGER.error('Base chart is orphaned: %s.', base_chart)
        except AmbiguousBaseChart:
            LOGGER.error('Base chart is ambiguous: %s.', base_chart)


def get_index(item: Any) -> int:
    """Returns the item's index."""

    return item.index


@coerce(set)
def level_configs(level: int) -> Iterable[Configuration]:
    """Yields all configurations of a certain group level."""

    return Configuration.select().join(GroupConfiguration).where(
        GroupConfiguration.group << level)


def uniquesort(iterable: Iterable[Any], *, key: Callable = None,
               reverse: bool = False) -> Iterable[Any]:
    """Uniquely sorts an iterable."""

    return sorted(set(iterable), key=key, reverse=reverse)


class PresentationMixin:
    """Common presentation mixin."""

    @property
    def _configuration(self) -> Configuration:
        """Returns the accumulated object's configuration."""
        with suppress(NoConfigurationFound):
            return self.configuration

        for configuration in self.groupconfigs:
            return configuration

        raise NoConfigurationFound()

    @property
    def _group_base_charts(self) -> Iterable[GroupBaseChart]:
        """Charts attached to groups, the object is a member of."""
        return GroupBaseChart.select().join(BaseChart).where(
            (GroupBaseChart.group << self._groups)
            & (BaseChart.trashed == 0)
        ).order_by(GroupBaseChart.index)

    @property
    @lru_cache()
    @coerce(set)
    def _groups(self) -> Iterator[Group]:
        """Yields all groups in a breadth-first search."""
        for level in self.grouplevels:
            for group in level:
                yield group

    @property
    @lru_cache()
    @coerce(set)
    def _menus(self) -> Iterator[Menu]:
        """Yields the accumulated menus of this object."""
        return chain(self.menus, self.group_menus)

    @property
    @coerce(partial(uniquesort, key=lambda item: item.id))
    def charts(self) -> Iterator[Chart]:
        """Yields all charts for this object."""
        return chain(self.playlist, self.menu_charts)

    @property
    @lru_cache()
    @coerce(get_files)
    def files(self) -> Iterator[File]:
        """Yields the presentation's used file IDs."""
        yield from self._configuration.files

        for menu in self._menus:
            yield from menu.files

        for chart in self.charts:
            try:
                files = chart.files
            except AttributeError:
                continue

            yield from files

    @property
    def groupconfigs(self) -> Iterator[Configuration]:
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
    def grouplevels(self) -> Iterator[Set[Group]]:
        """Yields group levels in a breadth-first search."""
        level = set(self.groups)

        while level:
            yield level
            level = set(group.parent for group in level if group.parent)

    @property
    @lru_cache()
    @coerce(resolve_charts)
    def menu_charts(self) -> Iterable[BaseChart]:
        """Yields charts of the object's menu."""
        return BaseChart.select().join(MenuItemChart).join(MenuItem).where(
            (BaseChart.trashed == 0) & (MenuItem.menu << self._menus))

    @property
    def group_menus(self) -> Iterable[Menu]:
        """Yields menus attached to groups the object is a member of."""
        return Menu.select().join(GroupMenu).where(
            GroupMenu.group << self._groups)

    @property
    def menutree(self) -> Iterable[MenuTreeItem]:
        """Returns the merged menu tree."""
        items = chain(*(MenuTreeItem.from_menu(menu) for menu in self._menus))
        return sorted(merge(items), key=get_index)

    @property
    @lru_cache()
    @coerce(resolve_charts)
    def playlist(self) -> Iterator[BaseChart]:
        """Yields the playlist."""
        base_charts = chain(self._group_base_charts, self.base_charts)

        for base_chart_mapping in sorted(base_charts, key=get_index):
            yield base_chart_mapping.base_chart

    def to_dom(self) -> dom.presentation:
        """Returns an XML dom presentation."""
        xml = dom.presentation()
        xml.configuration = self._configuration.to_dom()
        xml.playlist = [chart.to_dom(brief=True) for chart in self.playlist]
        xml.menu_item = [item.to_dom() for item in self.menutree]
        xml.chart = [chart.to_dom() for chart in self.charts]
        return xml

    def to_json(self) -> dict:
        """Returns a JSON presentation."""
        return {
            'charts': [
                chart.to_json(fk_fields=False) for chart in self.charts],
            'configuration': self._configuration.to_json(
                cascade=True, fk_fields=False),
            'customer': self.customer.id,
            'menuItems': [item.to_json() for item in self.menutree],
            'playlist': [
                chart.to_json(mode=ChartMode.BRIEF, fk_fields=False)
                for chart in self.playlist]
        }
