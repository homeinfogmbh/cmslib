"""Menu related functions."""

from his import CUSTOMER

from cmslib.messages.menu import NO_SUCH_MENU
from cmslib.messages.menu import NO_SUCH_MENU_ITEM
from cmslib.messages.menu import NO_SUCH_MENU_ITEM_CHART
from cmslib.orm.menu import Menu, MenuItem, MenuItemChart


__all__ = ['get_menu', 'get_menu_item', 'get_menu_item_chart']


def get_menu(ident: int) -> Menu:
    """Returns the respective menu of the current customer."""

    condition = Menu.customer == CUSTOMER.id
    condition &= Menu.id == ident

    try:
        return Menu.get(condition)
    except Menu.DoesNotExist:
        raise NO_SUCH_MENU from None


def get_menu_item(ident: int) -> MenuItem:
    """Returns the respective menu item."""

    condition = Menu.customer == CUSTOMER.id
    condition &= MenuItem.id == ident

    try:
        return MenuItem.select().join(Menu).where(condition).get()
    except MenuItem.DoesNotExist:
        raise NO_SUCH_MENU_ITEM from None


def get_menu_item_chart(ident: int) -> MenuItemChart:
    """Returns the respective MenuItemChart."""

    select = MenuItemChart.select().join(MenuItem).join(Menu)
    condition = Menu.customer == CUSTOMER.id
    condition &= MenuItemChart.id == ident

    try:
        return select.where(condition).get()
    except MenuItemChart.DoesNotExist:
        raise NO_SUCH_MENU_ITEM_CHART from None
