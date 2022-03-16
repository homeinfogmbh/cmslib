"""An indexed base chart."""

from __future__ import annotations
from typing import Iterable, Iterator, NamedTuple

from cmslib.orm import DeploymentBaseChart
from cmslib.orm import GroupBaseChart
from cmslib.orm import MenuItem
from cmslib.orm import MenuItemChart


__all__ = ['IndexedBaseChart']


class IndexedBaseChart(NamedTuple):
    """Base chart ID with index."""

    id: int
    index: int = 0

    @classmethod
    def from_menus(cls, menus: Iterable[int]) -> Iterator[IndexedBaseChart]:
        """Yields indexed base charts from the given menus."""
        for menu_item_chart in MenuItemChart.select().join(MenuItem).where(
                MenuItem.id << set(menus)
        ):
            yield cls(menu_item_chart.base_chart, menu_item_chart.index)

    @classmethod
    def from_groups(
            cls,
            groups: Iterable[int]
    ) -> Iterator[IndexedBaseChart]:
        """Yields indexed base charts from the given groups."""
        for group_base_chart in GroupBaseChart.select().where(
            GroupBaseChart.group << set(groups)
        ):
            yield cls(group_base_chart.base_chart, group_base_chart.index)

    @classmethod
    def from_deployment(cls, deployment: int) -> Iterator[IndexedBaseChart]:
        """Yields indexed base charts for the given deployment."""
        for deployment_base_chart in DeploymentBaseChart.select().where(
                DeploymentBaseChart.deployment == deployment
        ):
            yield cls(deployment_base_chart.id, deployment_base_chart.index)

    def key(self) -> int:
        """Returns the index for sorting."""
        return self.index
