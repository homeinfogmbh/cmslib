"""Common functions."""

from collections import defaultdict
from contextlib import suppress
from functools import lru_cache
from itertools import chain
from logging import getLogger
from typing import Iterable, Iterator, List, NamedTuple, Set

from peewee import Model, ModelSelect

from filedb import File as FileDBFile
from functoolsplus import coerce    # pylint: disable=E0401
from hisfs import File
from mdb import Customer

from cmslib import dom  # pylint: disable=E0611
from cmslib.exceptions import NoConfigurationFound
from cmslib.groups import Groups
from cmslib.menutree import MenuTreeItem
from cmslib.orm.charts import CHARTS, BaseChart, ChartMode, Chart
from cmslib.orm.content.group import GroupBaseChart, GroupMenu
from cmslib.orm.configuration import Configuration
from cmslib.orm.content.group import GroupConfiguration
from cmslib.orm.group import Group
from cmslib.orm.menu import Menu, MenuItem, MenuItemChart


__all__ = ['IndexedBaseChart', 'Presentation']


LOGGER = getLogger(__file__)


class IndexedBaseChart(NamedTuple):
    """An indexed base chart."""

    index: int
    base_chart: BaseChart


def select_files(ids: Iterator[int]) -> ModelSelect:
    """Yields files from their IDs."""

    return File.select(File, FileDBFile).join(FileDBFile).where(
        File.id << set(ids)).iterator()


def key(model: Model) -> int:
    """Returns the model's index."""

    return model.index


def get_group_levels(groups: Groups, memberships: Iterable[Group]) \
        -> Iterator[List[Group]]:
    """Yields group levels."""

    return groups.levels(memberships)


def get_group_set(group_levels: Iterable[List[Group]]) -> Set[Group]:
    """Returns a set of groups the target
    is directly or indirectly a member of.
    """

    return set(chain(*group_levels))


def get_group_configurations(group_levels: Iterable[List[Group]],
                             groups: Set[Group]) -> Iterator[Configuration]:
    """Yields group configurations."""

    configurations = defaultdict(set)

    for config in Configuration.select(
            GroupConfiguration, cascade=True).join_from(
            Configuration, GroupConfiguration).where(
            GroupConfiguration.group << groups):
        configurations[config.groupconfiguration.group_id].add(config)

    for level in group_levels:
        for group in level:
            with suppress(KeyError):
                yield from configurations[group.id]


def get_configuration(*configs: Iterable[Configuration]) -> Configuration:
    """Returns the first best configuration."""

    for config in chain(*configs):
        return config

    raise NoConfigurationFound()


def get_group_base_charts(groups: Set[Group]) -> Iterator[IndexedBaseChart]:
    """Charts attached to groups, the object is a member of."""

    for base_chart in BaseChart.select(GroupBaseChart, cascade=True).join_from(
            BaseChart, GroupBaseChart).where(
            (GroupBaseChart.group << groups)
            & (BaseChart.trashed == 0)):
        yield IndexedBaseChart(base_chart.groupbasechart.index, base_chart)


def get_unique_charts(*charts: Iterable[Chart]) -> List[Chart]:
    """Yields all charts for this object."""

    return sorted(set(chain(*charts)), key=lambda chart: chart.id)


def get_menu_charts(menus: Iterable[Menu]) -> Iterator[Chart]:
    """Yields charts of the object's menu."""

    base_charts = BaseChart.select().join(
        MenuItemChart).join(MenuItem).where(
        (BaseChart.trashed == 0) & (MenuItem.menu << menus))

    for chart_type in CHARTS.values():
        yield from chart_type.select(cascade=True).where(
            chart_type.base << base_charts)


def get_group_menus(groups: Set[Group]) -> Iterable[Menu]:
    """Yields menus attached to groups the object is a member of."""

    return Menu.select(cascade=True).join_from(Menu, GroupMenu).where(
        GroupMenu.group << groups)


def get_menutree(menus: Iterable[Menu]) -> Iterable[MenuTreeItem]:
    """Returns the merged menu tree."""

    return MenuTreeItem.from_menus(menus)


def get_playlist(*indexed_base_charts: Iterable[IndexedBaseChart]) \
        -> List[Chart]:
    """Yields the playlist."""

    indexed_base_charts = list(chain(*indexed_base_charts))
    base_charts_indices = {
        base_chart: index for index, base_chart in indexed_base_charts
    }
    base_chart_ids = {
        base_chart.id for base_chart in base_charts_indices.keys()
    }
    charts_by_base_chart = {}

    for chart_type in CHARTS.values():
        for chart in chart_type.select(cascade=True).where(
                chart_type.base << base_chart_ids):
            charts_by_base_chart[chart.base] = chart

    playlist = [
        charts_by_base_chart[ibc.base_chart] for ibc in indexed_base_charts
    ]
    return sorted(playlist, key=lambda chart: base_charts_indices[chart.base])


class Presentation:
    """A presentation object."""

    def __init__(self, customer: Customer):
        """Initializes the presentation."""
        self.customer = customer

    @property
    @lru_cache()
    def groups(self):
        """Returns Groups."""
        return Groups.for_customer(self.customer)

    @property
    @lru_cache()
    def _group_levels(self):
        """Returns the group levels."""
        return list(get_group_levels(self.groups, self.get_memberships()))

    @property
    @lru_cache()
    def _group_set(self):
        """Returns the group set."""
        return get_group_set(self._group_levels)

    @property
    @lru_cache()
    def _group_base_charts(self):
        """Returns the group base charts."""
        return list(get_group_base_charts(self._group_set))

    @property
    @lru_cache()
    def _base_charts(self):
        """Returns the base charts."""
        try:
            return self.get_base_charts()
        except NotImplementedError:
            return []

    @property
    @lru_cache()
    def playlist(self):
        """Returns the playlist."""
        return get_playlist(self._group_base_charts, self._base_charts)

    @property
    @lru_cache()
    def _menus(self):
        """Returns the menus."""
        try:
            return self.get_menus()
        except NotImplementedError:
            return []

    @property
    @lru_cache()
    def menus(self):
        """Returns the menus."""
        return set(chain(get_group_menus(self._group_set), self._menus))

    @property
    @lru_cache()
    def charts(self):
        """REturns the charts."""
        return get_unique_charts(self.playlist, get_menu_charts(self.menus))

    @property
    @lru_cache()
    def menu_tree(self):
        """Returns the menu tree."""
        return get_menutree(self.menus)

    @property
    @lru_cache()
    def _group_configurations(self):
        """Returns the group configurations."""
        return list(get_group_configurations(
            self._group_levels, self._group_set))

    @property
    @lru_cache()
    def _configs(self):
        """Returns the configurations."""
        try:
            return self.get_configurations()
        except NotImplementedError:
            return []

    @property
    @lru_cache()
    def configuration(self):
        """Returns the configuration."""
        return get_configuration(self._configs, self._group_configurations)

    @property
    @coerce(select_files)
    def files(self) -> Iterator[File]:
        """Yields the presentation's used file IDs."""

        yield from self.configuration.files

        for menu in self.menus:
            yield from menu.files

        for chart in self.charts:
            try:
                files = chart.files
            except AttributeError:
                continue

            yield from files

    def get_base_charts(self) -> Iterable[IndexedBaseChart]:
        """Yields base charts directly attached to the target."""
        raise NotImplementedError()

    def get_configurations(self) -> Iterable[Configuration]:
        """Yields configurations."""
        raise NotImplementedError()

    def get_memberships(self) -> Iterable[Group]:
        """Yields group memberships."""
        raise NotImplementedError()

    def get_menus(self) -> Iterable[Menu]:
        """Yields menus directly attached to the target."""
        raise NotImplementedError()

    def to_dom(self) -> dom.presentation:
        """Returns an XML dom presentation."""
        xml = dom.presentation()
        xml.customer = self.customer.id
        xml.configuration = self.configuration.to_dom()
        xml.playlist = [chart.to_dom(brief=True) for chart in self.playlist]
        xml.menu_item = [item.to_dom() for item in self.menu_tree]
        xml.chart = [chart.to_dom() for chart in self.charts]
        return xml

    def to_json(self) -> dict:
        """Returns a JSON presentation."""
        return {
            'charts': [
                chart.to_json(fk_fields=False) for chart in self.charts
            ],
            'configuration': self.configuration.to_json(
                cascade=True, fk_fields=False),
            'customer': self.customer.id,
            'menuItems': [item.to_json() for item in self.menu_tree],
            'playlist': [
                chart.to_json(mode=ChartMode.BRIEF, fk_fields=False)
                for chart in self.playlist
            ]
        }
