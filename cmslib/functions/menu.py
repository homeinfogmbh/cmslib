"""Menu related functions."""

from peewee import ModelSelect

from his import CUSTOMER
from hisfs import File
from mdb import Address, Company, Customer

from cmslib.messages.menu import NO_SUCH_MENU
from cmslib.messages.menu import NO_SUCH_MENU_ITEM
from cmslib.messages.menu import NO_SUCH_MENU_ITEM_CHART
from cmslib.orm.charts import BaseChart
from cmslib.orm.menu import Menu, MenuItem, MenuItemChart


__all__ = ['get_menu', 'get_menu_item', 'get_menu_item_chart']


def list_menus() -> ModelSelect:
    """Lists the menus of the current customer."""

    select = Menu.select(Menu, Customer, Company, Address)
    select = select.join(Customer).join(Company).join(Address)
    return select.where(Menu.customer == CUSTOMER.id)


def get_menu(ident: int) -> Menu:
    """Returns the respective menu of the current customer."""

    try:
        return list_menus().where(Menu.id == ident).get()
    except Menu.DoesNotExist:
        raise NO_SUCH_MENU from None


def list_menu_items() -> ModelSelect:
    """Lists the menu items of the current customer."""

    select = MenuItem.select(
        MenuItem, Menu, Customer, Company, Address, File)
    select = select.join(Menu).join(Customer).join(Company).join(Address)
    select = select.join_from(MenuItem, File)
    return select.where(Menu.customer == CUSTOMER.id).get()


def get_menu_item(ident: int) -> MenuItem:
    """Returns the respective menu item."""

    try:
        return list_menu_items().where(MenuItem.id == ident).get()
    except MenuItem.DoesNotExist:
        raise NO_SUCH_MENU_ITEM from None


def list_menu_item_charts() -> ModelSelect:
    """Selects the menu item charts of the current customer."""

    bc_customer = Customer.alias()
    bc_company = Company.alias()
    bc_address = Address.alias()
    select = MenuItemChart.select(
        MenuItemChart, MenuItem, Customer, Company, Address, Menu, File)
    select = select.join(MenuItem)
    select = select.join(Menu)
    select = select.join(Customer)
    select = select.join(Company)
    select = select.join(Address)
    select = select.join_from(MenuItem, File)
    select = select.join_from(MenuItemChart, BaseChart)
    select = select.join_from(BaseChart, bc_customer)
    select = select.join_from(bc_customer, bc_company)
    select = select.join_from(bc_company, bc_address)
    return select.where(Menu.customer == CUSTOMER.id)


def get_menu_item_chart(ident: int) -> MenuItemChart:
    """Returns the respective MenuItemChart."""

    try:
        return list_menu_item_charts().where(MenuItemChart.id == ident).get()
    except MenuItemChart.DoesNotExist:
        raise NO_SUCH_MENU_ITEM_CHART from None
