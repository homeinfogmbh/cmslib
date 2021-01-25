"""Menus, menu items and chart members."""

from __future__ import annotations
from logging import getLogger
from typing import Iterable, Iterator, Set, Union

from peewee import ForeignKeyField, IntegerField, ModelSelect

from hisfs import get_file, File
from mdb import Company, Customer
from peeweeplus import HTMLCharField

from cmslib import dom
from cmslib.attachments import attachment_json
from cmslib.exceptions import AmbiguousBaseChart
from cmslib.exceptions import CircularReference
from cmslib.exceptions import DifferentMenus
from cmslib.exceptions import MissingMenu
from cmslib.exceptions import OrphanedBaseChart
from cmslib.orm.common import UNCHANGED, CustomerModel, DSCMS4Model
from cmslib.orm.charts import BaseChart, Chart, ChartMode


__all__ = ['Menu', 'MenuItem', 'MODELS']


LOGGER = getLogger('Menu')
SUFFIX = ' (Kopie)'


class Menu(CustomerModel):
    """Menus trees."""

    name = HTMLCharField(255)
    description = HTMLCharField(255, null=True)

    @property
    def root_items(self) -> Iterable[MenuItem]:
        """Yields this menu's root items."""
        return self.items.where(MenuItem.parent >> None)

    @property
    def files(self) -> Set[File]:
        """Returns a set of IDs of files used by the chart."""
        return {
            item.icon_image for item in self.items
            if item.icon_image is not None
        }

    def copy(self, suffix: str = SUFFIX) -> Iterator[Union[Menu, MenuItem]]:
        """Copies thhe respective menu."""
        copy = type(self)[self.id]
        copy.id = None
        copy.name = self.name + suffix
        yield copy

        for root_item in self.root_items:
            yield from root_item.copy(menu=copy)

    def to_json(self, *args, items: bool = False, **kwargs) -> dict:
        """Returns the menu as a dictionary."""
        json = super().to_json(*args, **kwargs)

        if items:
            json['items'] = [
                item.to_json(charts=True, children=True, fk_fields=False)
                for item in self.root_items.order_by(MenuItem.index)
            ]

        return json


class MenuItem(DSCMS4Model):
    """A menu item."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'menu_item'

    menu = ForeignKeyField(
        Menu, column_name='menu', on_delete='CASCADE', backref='items',
        lazy_load=False)
    parent = ForeignKeyField(
        'self', column_name='parent', null=True, on_delete='CASCADE',
        backref='children', lazy_load=True)
    name = HTMLCharField(255)
    icon = HTMLCharField(255, null=True)
    icon_image = ForeignKeyField(
        File, column_name='icon_image', null=True, lazy_load=False)
    text_color = IntegerField(default=0x000000)
    background_color = IntegerField(default=0xffffff)
    index = IntegerField(default=0)

    @classmethod
    def from_json(cls, json: dict, customer: int, **kwargs) -> MenuItem:
        """Creates a new menu item from the provided dictionary."""
        menu = json.pop('menu')
        parent = json.pop('parent', None)
        icon_image = json.pop('iconImage', None)
        menu_item = super().from_json(json, **kwargs)

        if icon_image is not None:
            menu_item.icon_image = get_file(icon_image)

        return menu_item.move(menu=menu, parent=parent, customer=customer)

    @classmethod
    def select(cls, *args, cascade: bool = False, **kwargs) -> ModelSelect:
        """Selects records."""
        if not cascade:
            return super().select(*args, **kwargs)

        args = {cls, Menu, Customer, Company, *args}
        return super().select(*args, **kwargs).join_from(cls, Menu).join(
            Customer).join(Company)

    @property
    def root(self) -> bool:
        """Determines whether this is a root node entry."""
        return self.menu is not None

    @property
    def ordered_children(self) -> ModelSelect:
        """Returns the children."""
        return self.children.order_by(type(self).index)

    @property
    def tree(self) -> Iterator[MenuItem]:
        """Recursively yields all submenus."""
        yield self

        for child in self.ordered_children:
            yield from child.tree

    @property
    def charts(self) -> Iterator[Chart]:
        """Yields the respective charts."""
        for menu_item_chart in self.menu_item_charts:
            base_chart = menu_item_chart.base_chart

            try:
                yield base_chart.chart
            except OrphanedBaseChart:
                LOGGER.error('Base chart #%i is orphaned.', base_chart.id)
            except AmbiguousBaseChart:
                LOGGER.error('Base chart #%i is ambiguous.', base_chart.id)

    def _get_menu(self, menu: int, customer: int = None) -> Menu:
        """Returns the respective menu."""
        if menu is None:
            raise MissingMenu()

        if menu is UNCHANGED:
            return self.menu

        if customer is None:
            customer = self.menu.customer

        return Menu.get((Menu.customer == customer) & (Menu.id == menu))

    def _get_parent(self, parent: int, customer: int = None) -> MenuItem:
        """Returns the respective parent."""
        if parent is None:
            return None

        if parent is UNCHANGED:
            return self.parent

        if customer is None:
            customer = self.menu.customer

        cls = type(self)
        return cls.select().join(Menu).where(
            (Menu.customer == customer) & (cls.id == parent)).get()

    def move(self, *, menu: int = UNCHANGED, parent: int = UNCHANGED,
             customer: int = None) -> MenuItemGroup:
        """Moves the menu item to another menu and / or parent."""
        menu = self._get_menu(menu, customer=customer)
        parent = self._get_parent(parent, customer=customer)

        if parent is not None:
            if parent.menu != menu:
                raise DifferentMenus(menu, parent.menu)

            if parent in self.tree:
                raise CircularReference(parent)

        self.parent = parent
        menu_items = [self]

        if self.id is not None:     # Fix #351.
            for menu_item in self.tree:
                menu_item.menu = menu
                menu_items.append(menu_item)

        return MenuItemGroup(menu_items)

    def copy(self, menu: Menu = None, parent: MenuItem = None) \
            -> Iterator[Union[MenuItem, MenuItemChart]]:
        """Copies this menu item."""
        copy = type(self)[self.id]
        copy.id = None
        copy.menu = menu or self.menu
        copy.parent = parent
        yield copy

        for menu_item_chart in self.menu_item_charts:
            yield menu_item_chart.copy(menu_item=copy)

        for child in self.ordered_children:
            yield from child.copy(menu=menu, parent=copy)

    def delete_instance(self, update_children: bool = False, **kwargs) -> int:
        """Removes this menu item."""
        if update_children:
            for child in self.children:
                child.move(parent=self.parent)

        return super().delete_instance(**kwargs)

    def patch_json(self, json: dict, **kwargs) -> MenuItemGroup:
        """Patches the menu item."""
        menu = json.pop('menu', UNCHANGED)
        parent = json.pop('parent', UNCHANGED)
        icon_image = json.pop('iconImage', UNCHANGED)
        super().patch_json(json, **kwargs)

        if icon_image is not UNCHANGED:
            self.icon_image = get_file(icon_image)

        return self.move(menu=menu, parent=parent)

    def to_json(self, charts: bool = False, children: bool = False,
                **kwargs) -> dict:
        """Returns a JSON-ish dictionary."""
        json = super().to_json(**kwargs)
        json['iconImage'] = attachment_json(self.icon_image)

        if charts:
            json['charts'] = [
                menu_item_chart.to_json(
                    menu_item=False, base_chart=False, chart=True)
                for menu_item_chart in self.menu_item_charts.order_by(
                    MenuItemChart.index)
                if not menu_item_chart.base_chart.trashed
            ]

        if children:
            json['items'] = [
                item.to_json(charts=charts, children=children, **kwargs)
                for item in self.ordered_children
            ]

        return json


class MenuItemChart(DSCMS4Model):
    """Mapping in-between menu items and base charts."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'menu_item_chart'

    menu_item = ForeignKeyField(
        MenuItem, column_name='menu_item', backref='menu_item_charts',
        on_delete='CASCADE', lazy_load=False)
    base_chart = ForeignKeyField(
        BaseChart, column_name='base_chart', on_delete='CASCADE',
        lazy_load=False)
    index = IntegerField(default=0)

    @classmethod
    def from_json(cls, json: dict, menu_item: MenuItem, base_chart: BaseChart,
                  **kwargs) -> MenuItemChart:
        """Creates a record from a JSON-ish dictionary."""
        menu_item_chart = super().from_json(json, **kwargs)
        menu_item_chart.menu_item = menu_item
        menu_item_chart.base_chart = base_chart
        return menu_item_chart

    @classmethod
    def select(cls, *args, cascade: bool = False, **kwargs) -> ModelSelect:
        """Selects records."""
        if not cascade:
            return super().select(*args, **kwargs)

        args = {cls, MenuItem, Menu, Customer, Company, BaseChart, *args}
        return super().select(*args, **kwargs).join_from(cls, MenuItem).join(
            Menu).join(Customer).join(Company).join_from(cls, BaseChart)

    def copy(self, menu_item: MenuItem = None) -> MenuItemChart:
        """Copies this menu item chart."""
        copy = type(self)[self.id]
        copy.id = None
        copy.menu_item = menu_item or self.menu_item
        return copy

    def to_json(self, menu_item: bool = True, base_chart: bool = True,
                chart: bool = False) -> dict:
        """Returns a JSON-ish dictionary."""
        if menu_item and base_chart and not chart:
            return super().to_json()

        skip = set()

        if not menu_item:
            skip.add('menuItem')

        if not base_chart:
            skip.add('baseChart')

        json = super().to_json(skip=skip)

        if chart:
            json['chart'] = self.base_chart.chart.to_json(mode=ChartMode.BRIEF)

        return json

    def to_dom(self) -> dom.MenuItemChart:
        """Returns an XML DOM of the model."""
        xml = dom.MenuItemChart()
        chart = self.base_chart.chart
        xml.id = chart.id
        xml.type = type(chart).__name__
        xml.index = self.index
        return xml


class MenuItemGroup(tuple):
    """A group of menu items."""

    @property
    def id(self):   # pylint: disable=C0103
        """Returns the first menu items's ID."""
        return self[0].id

    def save(self):
        """Saves all menu items."""
        for menu_item in self:
            menu_item.save()


MODELS = (Menu, MenuItem, MenuItemChart)
