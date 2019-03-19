"""Menu related functions."""

from his import CUSTOMER

from cmslib.messages.menu import NO_SUCH_MENU
from cmslib.messages.menu import NO_SUCH_MENU_ITEM
from cmslib.messages.menu import NO_SUCH_MENU_ITEM_CHART
from cmslib.orm.menu import Menu, MenuItem, MenuItemChart


__all__ = ['get_menu', 'get_menu_item', 'get_menu_item_chart']


def get_menu(ident):
    """Returns the respective menu of the current customer."""

    try:
        return Menu.get((Menu.customer == CUSTOMER.id) & (Menu.id == ident))
    except Menu.DoesNotExist:
        raise NO_SUCH_MENU


def get_menu_item(ident):
    """Returns the respective menu item."""

    try:
        return MenuItem.select().join(Menu).where(
            (Menu.customer == CUSTOMER.id) & (MenuItem.id == ident)).get()
    except MenuItem.DoesNotExist:
        raise NO_SUCH_MENU_ITEM


def get_menu_item_chart(ident):
    """Returns the respective MenuItemChart."""

    try:
        return MenuItemChart.select().join(MenuItem).join(Menu).where(
            (Menu.customer == CUSTOMER.id) & (MenuItemChart.id == ident)).get()
    except MenuItemChart.DoesNotExist:
        raise NO_SUCH_MENU_ITEM_CHART
