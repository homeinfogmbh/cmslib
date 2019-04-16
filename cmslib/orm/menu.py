"""Menus, menu items and chart members."""

from collections import namedtuple
from logging import getLogger

from peewee import ForeignKeyField, CharField, IntegerField

from cmslib import dom
from cmslib.exceptions import OrphanedBaseChart, AmbiguousBaseChart
from cmslib.messages.data import CIRCULAR_REFERENCE
from cmslib.messages.menu import NO_MENU_SPECIFIED, DIFFERENT_MENUS
from cmslib.orm.common import UNCHANGED, CustomerModel, DSCMS4Model
from cmslib.orm.charts import ChartMode, BaseChart


__all__ = ['Menu', 'MenuItem', 'MODELS']


LOGGER = getLogger('Menu')
COPY_SUFFIX = ' (Kopie)'


class MenuItemGroup(namedtuple(
        'MenuItemGroup', ('menu_item', 'childrens_children'))):
    """A group of menu items."""

    @property
    def id(self):   # pylint: disable=C0103
        """Returns the menu items's ID."""
        return self.menu_item.id

    def save(self):
        """Saves all menu items."""
        for menu_item in self.childrens_children:
            menu_item.save()

        self.menu_item.save()


class Menu(CustomerModel):
    """Menus trees."""

    name = CharField(255)
    description = CharField(255, null=True)

    @property
    def root_items(self):
        """Yields this menu's root items."""
        return self.items.where(MenuItem.parent >> None)

    def copy(self, suffix=COPY_SUFFIX):
        """Copies thhe respective menu."""
        copy = type(self)[self.id]
        copy.id = None
        copy.name = self.name + suffix
        yield copy

        for root_item in self.root_items:
            yield from root_item.copy(menu=copy)

    def to_json(self, *args, items=False, **kwargs):
        """Returns the menu as a dictionary."""
        json = super().to_json(*args, **kwargs)

        if items:
            json['items'] = [
                item.to_json(charts=True, children=True, fk_fields=False)
                for item in self.root_items.order_by(MenuItem.index)]

        return json


class MenuItem(DSCMS4Model):
    """A menu item."""

    class Meta:
        table_name = 'menu_item'

    menu = ForeignKeyField(
        Menu, column_name='menu', on_delete='CASCADE', backref='items')
    parent = ForeignKeyField(
        'self', column_name='parent', null=True, on_delete='CASCADE',
        backref='children')
    name = CharField(255)
    icon = CharField(255, null=True)
    text_color = IntegerField(default=0x000000)
    background_color = IntegerField(default=0xffffff)
    index = IntegerField(default=0)

    @classmethod
    def from_json(cls, json, customer, **kwargs):
        """Creates a new menu item from the provided dictionary."""
        menu = json.pop('menu')
        parent = json.pop('parent', None)
        menu_item = super().from_json(json, **kwargs)
        return menu_item.move(menu=menu, parent=parent, customer=customer)

    @property
    def root(self):
        """Determines whether this is a root node entry."""
        return self.menu is not None

    @property
    def childrens_children(self):
        """Recursively yields all submenus."""
        for child in self.children.order_by(type(self).index):
            for childrens_child in child.childrens_children:
                yield childrens_child

    @property
    def charts(self):
        """Yields the respective charts."""
        for menu_item_chart in self.menu_item_charts:
            base_chart = menu_item_chart.base_chart

            try:
                yield base_chart.chart
            except OrphanedBaseChart:
                LOGGER.error('Base chart #%i is orphaned.', base_chart.id)
            except AmbiguousBaseChart:
                LOGGER.error('Base chart #%i is ambiguous.', base_chart.id)

    def _get_menu(self, menu, customer=None):
        """Returns the respective menu."""
        if menu is None:
            raise NO_MENU_SPECIFIED

        if menu is UNCHANGED:
            return self.menu

        if customer is None:
            customer = self.menu.customer

        return Menu.get((Menu.customer == customer) & (Menu.id == menu))

    def _get_parent(self, parent, customer=None):
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

    def move(self, *, menu=UNCHANGED, parent=UNCHANGED, customer=None):
        """Moves the menu item to another menu and / or parent."""
        menu = self._get_menu(menu, customer=customer)
        parent = self._get_parent(parent, customer=customer)

        if parent is not None:
            if parent.menu != menu:
                raise DIFFERENT_MENUS

            if parent in self.childrens_children:
                raise CIRCULAR_REFERENCE

        self.menu = menu
        self.parent = parent
        childrens_children = []

        for child in self.childrens_children:
            child.menu = menu
            childrens_children.append(child)

        return MenuItemGroup(self, childrens_children)

    def copy(self, menu=None, parent=None):
        """Copies this menu item."""
        copy = type(self)[self.id]
        copy.id = None
        copy.menu = menu or self.menu
        copy.parent = parent
        yield copy

        for menu_item_chart in self.menu_item_charts:
            yield menu_item_chart.copy(menu_item=copy)

        for child in self.children:
            yield from child.copy(menu=menu, parent=copy)

    def delete_instance(self, update_children=False, **kwargs):
        """Removes this menu item."""
        if update_children:
            for child in self.children:
                child.move(parent=self.parent)

        return super().delete_instance(**kwargs)

    def patch_json(self, json, **kwargs):
        """Patches the menu item."""
        menu = json.pop('menu', UNCHANGED)
        parent = json.pop('parent', UNCHANGED)
        super().patch_json(json, **kwargs)
        return self.move(menu=menu, parent=parent)

    def to_json(self, charts=False, children=False, **kwargs):
        """Returns a JSON-ish dictionary."""
        json = super().to_json(**kwargs)

        if charts:
            json['charts'] = [
                menu_item_chart.to_json() for menu_item_chart
                in self.menu_item_charts.order_by(MenuItemChart.index)
                if not menu_item_chart.base_chart.trashed]

        if children:
            json['items'] = [
                item.to_json(charts=charts, children=children, **kwargs)
                for item in self.children]

        return json


class MenuItemChart(DSCMS4Model):
    """Mapping in-between menu items and base charts."""

    class Meta:
        table_name = 'menu_item_chart'

    menu_item = ForeignKeyField(
        MenuItem, column_name='menu_item', backref='menu_item_charts',
        on_delete='CASCADE')
    base_chart = ForeignKeyField(
        BaseChart, column_name='base_chart', on_delete='CASCADE')
    index = IntegerField(default=0)

    @classmethod
    def from_json(cls, json, menu_item, base_chart, **kwargs):
        """Creates a record from a JSON-ish dictionary."""
        menu_item_chart = super().from_json(json, **kwargs)
        menu_item_chart.menu_item = menu_item
        menu_item_chart.base_chart = base_chart
        return menu_item_chart

    def copy(self, menu_item=None):
        """Copies this menu item chart."""
        copy = type(self)[self.id]
        copy.id = None
        copy.menu_item = menu_item or self.menu_item
        return copy

    def to_json(self, menu_item=True, base_chart=True, cascade=False):
        """Returns a JSON-ish dictionary."""
        if menu_item and base_chart and not cascade:
            return super().to_json()

        skip = set()

        if not menu_item:
            skip.add('menu_item')

        if not base_chart:
            skip.add('base_chart')

        json = super().to_json(skip=skip)

        if cascade:
            chart = self.base_chart.chart
            json['chart'] = chart.to_json(mode=ChartMode.BRIEF)

        return json

    def to_dom(self):
        """Returns an XML DOM of the model."""
        xml = dom.MenuItemChart()
        chart = self.base_chart.chart
        xml.id = chart.id
        xml.type = type(chart).__name__
        xml.index = self.index
        return xml


MODELS = (Menu, MenuItem, MenuItemChart)
