"""Common functions."""

from __future__ import annotations
from collections import defaultdict
from typing import Iterable, Iterator

from cmslib.orm import CHARTS
from cmslib.orm import Chart
from cmslib.orm import Configuration
from cmslib.orm import Group
from cmslib.orm import GroupConfiguration
from cmslib.presentation2.indexed_base_chart import IndexedBaseChart


__all__ = ['get_charts', 'sorted_base_charts', 'get_group_configurations']


def get_charts(base_charts: Iterable[int]) -> Iterator[Chart]:
    """Yields charts from the given base charts."""

    for chart_type in CHARTS.values():
        yield from chart_type.prefetch(
            chart_type.select(cascade=True).where(
                chart_type.base << base_charts
            )
        )


def sorted_base_charts(
        indexed_base_charts: Iterable[IndexedBaseChart]
) -> list[int]:
    """Yields base chart IDs from indexed base charts."""

    return sorted(
        (indexed_base_chart.id for indexed_base_chart in indexed_base_charts),
        key=IndexedBaseChart.key
    )


def get_group_configurations(
        group_levels: Iterable[list[Group]],
        groups_set: set[Group]
) -> Iterator[Configuration]:
    """Yields group configurations."""

    configurations = defaultdict(set)

    for group_config in GroupConfiguration.select().where(
            GroupConfiguration.group << groups_set
    ):
        configurations[group_config.group].add(group_config.configuration)

    for level in group_levels:
        for group in level:
            yield from configurations[group.id]
