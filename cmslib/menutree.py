"""Menu tree utilities."""

from __future__ import annotations
from collections import defaultdict
from itertools import chain
from json import dumps
from typing import Any, Iterable, Iterator, NamedTuple, Union

from hisfs import File

from cmslib import dom  # pylint: disable=E0611
from cmslib.attachments import attachment_dom, attachment_json
from cmslib.orm.menu import Menu, MenuItem, MenuItemChart


__all__ = ['MenuTreeItem']


def merge(children: Iterable[MenuTreeItem]) -> list[MenuTreeItem]:
    """Merges lists of children by their signature."""

    mapping = defaultdict(list)

    for child in children:
        mapping[child.signature].append(child)

    return [sum(children) for children in mapping.values()]


def get_index(obj: Any) -> int:
    """Key function for sorting."""

    return obj.index


class MenuTreeItem(NamedTuple):
    """Menu item for tree structure."""

    name: str
    icon: str
    icon_image: File
    text_color: int
    background_color: int
    index: int
    menu_item_charts: Iterable[MenuItemChart]
    children: Iterable[MenuTreeItem]

    def __str__(self):
        """Returns a nested JSON object."""
        return dumps(self.to_json(), indent=2)

    def __add__(self, other: MenuTreeItem) -> MenuTreeItem:
        """Adds two menu tree items."""
        if self.signature != other.signature:
            raise ValueError('Can only add menu items with same signature.')

        children = merge(chain(self.children, other.children))
        base_charts = set()
        menu_item_charts = set()

        for mic in chain(self.menu_item_charts, other.menu_item_charts):
            if mic.base_chart_id not in base_charts:
                base_charts.add(mic.base_chart_id)
                menu_item_charts.add(mic)

        return MenuTreeItem(
            self.name, self.icon, self.icon_image, self.text_color,
            self.background_color, self.index, menu_item_charts, children
        )

    def __radd__(self, other: Union[MenuTreeItem, int]):
        """Compensate for start=0 on sum() call."""
        if other == 0:
            return self

        return self + other

    @classmethod
    def from_menu_item(
            cls,
            menu_item: MenuItem,
            menu_items: Iterable[MenuItem],
            menu_item_charts: Iterable[MenuItemChart]
    ) -> MenuTreeItem:
        """Creates a menu item tree from the given menu item."""
        children = [
            cls.from_menu_item(child, menu_items, menu_item_charts) for child
            in filter(lambda item: item.parent_id == menu_item.id, menu_items)
        ]
        menu_item_charts = [
            menu_item_chart for menu_item_chart in menu_item_charts
            if menu_item_chart.menu_item_id == menu_item.id
        ]
        return cls(
            menu_item.name, menu_item.icon, menu_item.icon_image,
            menu_item.text_color, menu_item.background_color, menu_item.index,
            menu_item_charts, children)

    @classmethod
    def from_menu_items(
            cls,
            menu_items: Iterable[MenuItem],
            menu_item_charts: Iterable[MenuItemChart]
    ) -> Iterator[MenuTreeItem]:
        """Yields menu tree items from the respective menu."""
        for root_item in filter(lambda item: item.parent is None, menu_items):
            yield cls.from_menu_item(root_item, menu_items, menu_item_charts)

    @classmethod
    def from_menus(cls, menus: Iterable[Menu]) -> Iterator[MenuTreeItem]:
        """Creates a tree from several menus."""
        menu_items = MenuItem.select(cascade=True).where(True)
        menu_item_charts = MenuItemChart.select(cascade=True).where(True)
        trees = [
            cls.from_menu_items(
                {item for item in menu_items if item.menu_id == menu.id},
                menu_item_charts
            ) for menu in menus
        ]
        return sorted(merge(chain(*trees)), key=get_index)


    @property
    def signature(self) -> tuple[str, str, int, int]:
        """Returns a tuple, identifying the menu tree item."""
        return self.name, self.icon, self.text_color, self.background_color

    def to_json(self) -> dict:
        """Returns a nested JSON-ish dict."""
        return {
            'name': self.name,
            'icon': self.icon,
            'iconImage': attachment_json(self.icon_image),
            'textColor': self.text_color,
            'backgroundColor': self.background_color,
            'index': self.index,
            'charts': [
                menu_item_chart.to_json(menu_item=False, base_chart=True)
                for menu_item_chart in sorted(
                    self.menu_item_charts, key=get_index
                )
                if not menu_item_chart.base_chart.trashed
            ],
            'menuItems': [
                child.to_json() for child in sorted(
                    self.children, key=get_index)
            ]
        }

    def to_dom(self) -> dom.MenuItem:
        """Returns an XML DOM of the model."""
        xml = dom.MenuItem()
        xml.name = self.name
        xml.icon = self.icon
        xml.icon_image = attachment_dom(self.icon_image)
        xml.text_color = self.text_color
        xml.background_color = self.background_color
        xml.index = self.index
        xml.menu_item = [item.to_dom() for item in self.children]
        xml.chart = [
            menu_item_chart.to_dom() for menu_item_chart
            in sorted(self.menu_item_charts, key=get_index)
            if not menu_item_chart.base_chart.trashed
        ]
        return xml
