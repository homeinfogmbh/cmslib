"""Menu related functions."""

from typing import Optional, Union

from peewee import ModelSelect

from his import CUSTOMER

from cmslib.orm.menu import Menu, MenuItem, MenuItemChart


__all__ = ['get_menu', 'get_menu_item', 'get_menu_item_chart']


def list_menus() -> ModelSelect:
    """Lists the menus of the current customer."""

    return Menu.select(cascade=True).where(Menu.customer == CUSTOMER.id)


def get_menu(ident: int) -> Menu:
    """Returns the respective menu of the current customer."""

    return list_menus().where(Menu.id == ident).get()


def list_menu_items(menu: Optional[Union[Menu, int]] = None) -> ModelSelect:
    """Lists the menu items of the current customer."""

    condition = Menu.customer == CUSTOMER.id

    if menu is not None:
        condition &= MenuItem.menu == menu

    return MenuItem.select(cascade=True).where(condition)


def get_menu_item(ident: int) -> MenuItem:
    """Returns the respective menu item."""

    return list_menu_items().where(MenuItem.id == ident).get()


def list_menu_item_charts(
        menu: Optional[Union[Menu, int]] = None) -> ModelSelect:
    """Selects the menu item charts of the current customer."""

    condition = Menu.customer == CUSTOMER.id

    if menu is not None:
        condition &= MenuItemChart.menu == menu

    return MenuItemChart.select(cascade=True).where(condition)


def get_menu_item_chart(ident: int) -> MenuItemChart:
    """Returns the respective MenuItemChart."""

    return list_menu_item_charts().where(MenuItemChart.id == ident).get()
