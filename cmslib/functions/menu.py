"""Menu related functions."""

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


def list_menu_items() -> ModelSelect:
    """Lists the menu items of the current customer."""

    return MenuItem.select(cascade=True).where(Menu.customer == CUSTOMER.id)


def get_menu_item(ident: int) -> MenuItem:
    """Returns the respective menu item."""

    return list_menu_items().where(MenuItem.id == ident).get()


def list_menu_item_charts() -> ModelSelect:
    """Selects the menu item charts of the current customer."""

    return MenuItemChart.select(cascade=True).where(
        Menu.customer == CUSTOMER.id)


def get_menu_item_chart(ident: int) -> MenuItemChart:
    """Returns the respective MenuItemChart."""

    return list_menu_item_charts().where(MenuItemChart.id == ident).get()
