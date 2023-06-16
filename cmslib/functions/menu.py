"""Menu related functions."""

from typing import Iterable, Optional, Union

from peewee import Select

from mdb import Customer

from cmslib.orm.menu import Menu, MenuItem, MenuItemChart


__all__ = [
    'get_menu',
    'get_menus',
    'get_menu_item',
    'get_menu_items',
    'get_menu_item_chart',
    'get_menu_item_charts'
]


def get_menu(ident: int, customer: Union[Customer, int]) -> Menu:
    """Returns the respective menu of the given customer."""

    return get_menus(customer).where(Menu.id == ident).get()


def get_menus(customer: Union[Customer, int]) -> Select:
    """Lists the menus of the given customer."""

    return Menu.select(cascade=True).where(Menu.customer == customer)


def get_menu_item(ident: int, customer: Union[Customer, int]) -> MenuItem:
    """Returns the respective menu item of the given customer."""

    return get_menu_items(customer).where(MenuItem.id == ident).get()


def get_menu_items(
        customer: Union[Customer, int],
        *,
        menu: Optional[Union[Menu, int]] = None,
        ids: Optional[Iterable[int]] = None
) -> Select:
    """Lists the menu items of the given customer."""

    condition = Menu.customer == customer

    if menu is not None:
        condition &= MenuItem.menu == menu

    if ids is not None:
        condition &= MenuItem.id << set(ids)

    return MenuItem.select(cascade=True).where(condition)


def get_menu_item_chart(
        ident: int,
        customer: Union[Customer, int]
) -> MenuItemChart:
    """Returns the respective menu item chart of the given customer."""

    return get_menu_item_charts(customer).where(
        MenuItemChart.id == ident
    ).get()


def get_menu_item_charts(
        customer: Union[Customer, int],
        menu: Optional[Union[Menu, int]] = None
) -> Select:
    """Selects the menu item charts of the given customer."""

    condition = Menu.customer == customer

    if menu is not None:
        condition &= MenuItemChart.menu == menu

    return MenuItemChart.select(cascade=True).where(condition)
