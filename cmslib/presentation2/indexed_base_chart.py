"""An indexed base chart."""

from __future__ import annotations
from typing import Iterable, Iterator, NamedTuple

from cmslib.orm import DeploymentBaseChart
from cmslib.orm import GroupBaseChart


__all__ = ["IndexedBaseChart"]


class IndexedBaseChart(NamedTuple):
    """Base chart ID with index."""

    id: int
    index: int = 0

    @classmethod
    def from_groups(cls, groups: Iterable[int]) -> Iterator[IndexedBaseChart]:
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
            yield cls(deployment_base_chart.base_chart, deployment_base_chart.index)

    def key(self) -> int:
        """Returns the index for sorting."""
        return self.index
