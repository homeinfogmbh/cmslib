"""Common presentation base."""

from __future__ import annotations
from itertools import chain
from typing import Iterator, NamedTuple

from mdb import Customer
from hwdb import Deployment

from cmslib import dom
from cmslib.exceptions import NoConfigurationFound
from cmslib.groups import Groups
from cmslib.menutree import MenuTreeItem
from cmslib.orm import Chart
from cmslib.orm import ChartMode
from cmslib.orm import Configuration
from cmslib.orm import DeploymentConfiguration
from cmslib.orm import DeploymentMenu
from cmslib.orm import GroupMemberDeployment
from cmslib.orm import GroupMenu
from cmslib.presentation2.functions import get_charts
from cmslib.presentation2.functions import get_group_configurations
from cmslib.presentation2.functions import sorted_base_charts
from cmslib.presentation2.indexed_base_chart import IndexedBaseChart


__all__ = ['Presentation']


class Presentation(NamedTuple):
    """An abstract presentation."""

    customer: Customer
    configuration: Configuration
    chart_map: dict[int, Chart]
    play_order: list[int]
    menu_tree: list[MenuTreeItem]

    @classmethod
    def from_deployment(cls, deployment: Deployment) -> Presentation:
        """Initializes the presentation for the given customer."""
        groups = Groups.for_customer(deployment.customer)
        membership_ids = {
            group_member_deployment.group for group_member_deployment in
            GroupMemberDeployment.select().where(
                GroupMemberDeployment.deployment == deployment.id
            )
        }
        memberships = {group for group in groups.groups(membership_ids)}
        group_levels = list(groups.levels(memberships))
        groups_set = set(chain.from_iterable(group_levels))

        deployment_menus = {
            deployment_menu.menu for deployment_menu in
            DeploymentMenu.select().where(
                DeploymentMenu.deployment == deployment
            )
        }
        group_menus = {
            group_menu.menu for group_menu in GroupMenu.select().where(
                GroupMenu.group << groups_set
            )
        }
        menu_ids = {
            *deployment_menus,
            *group_menus
        }

        try:
            configuration = DeploymentConfiguration.select().where(
                DeploymentConfiguration.deployment == deployment
            ).get().configuration
        except DeploymentConfiguration.DoesNotExist:
            try:
                configuration, *_ = get_group_configurations(
                    group_levels, groups_set
                )
            except ValueError:
                raise NoConfigurationFound()

        play_order = sorted_base_charts(
            chain(
                IndexedBaseChart.from_deployment(deployment),
                IndexedBaseChart.from_groups(groups_set),
                IndexedBaseChart.from_menus(menu_ids)
            )
        )

        return cls(
            deployment.customer,
            Configuration.select(cascade=True).where(
                Configuration.id == configuration
            ).get(),
            {chart.base.id: chart for chart in get_charts(set(play_order))},
            play_order,
            list(MenuTreeItem.from_menu_ids(menu_ids))
        )

    @property
    def charts(self) -> Iterator[Chart]:
        """Yields all charts."""
        return self.chart_map.keys()

    @property
    def playlist(self) -> Iterator[Chart]:
        """Yields the playlist charts."""
        for base_chart_id in self.play_order:
            yield self.chart_map[base_chart_id]

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
                cascade=True, fk_fields=False
            ),
            'customer': self.customer.id,
            'menuItems': [item.to_json() for item in self.menu_tree],
            'playlist': [
                chart.to_json(mode=ChartMode.BRIEF, fk_fields=False)
                for chart in self.playlist
            ]
        }
