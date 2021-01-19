"""Menu related functions."""

from peewee import ModelSelect

from his import CUSTOMER
from peeweeplus import select_tree

from cmslib.messages.menu import NO_SUCH_MENU
from cmslib.messages.menu import NO_SUCH_MENU_ITEM
from cmslib.messages.menu import NO_SUCH_MENU_ITEM_CHART
from cmslib.orm.menu import Menu, MenuItem, MenuItemChart


__all__ = ['get_menu', 'get_menu_item', 'get_menu_item_chart']


def list_menus() -> ModelSelect:
    """Lists the menus of the current customer."""

    return select_tree(Menu).where(Menu.customer == CUSTOMER.id)


def get_menu(ident: int) -> Menu:
    """Returns the respective menu of the current customer."""

    try:
        return list_menus().where(Menu.id == ident).get()
    except Menu.DoesNotExist:
        raise NO_SUCH_MENU from None


def list_menu_items() -> ModelSelect:
    """Lists the menu items of the current customer."""

    return select_tree(MenuItem).where(Menu.customer == CUSTOMER.id).get()


def get_menu_item(ident: int) -> MenuItem:
    """Returns the respective menu item."""

    try:
        return list_menu_items().where(MenuItem.id == ident).get()
    except MenuItem.DoesNotExist:
        raise NO_SUCH_MENU_ITEM from None


def list_menu_item_charts() -> ModelSelect:
    """Selects the menu item charts of the current customer."""

    return select_tree(MenuItemChart).where(Menu.customer == CUSTOMER.id)


def get_menu_item_chart(ident: int) -> MenuItemChart:
    """Returns the respective MenuItemChart."""

    try:
        return list_menu_item_charts().where(MenuItemChart.id == ident).get()
    except MenuItemChart.DoesNotExist:
        raise NO_SUCH_MENU_ITEM_CHART from None
