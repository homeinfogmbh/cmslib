"""Menu related messages."""

from cmslib.messages.facility import DSCMS4_MESSAGE


__all__ = [
    'NO_MENU_SPECIFIED',
    'NO_SUCH_MENU',
    'INVALID_MENU_DATA',
    'MENU_ADDED',
    'MENU_PATCHED',
    'MENU_COPIED',
    'MENU_DELETED',
    'NO_MENU_ITEM_SPECIFIED',
    'NO_SUCH_MENU_ITEM',
    'MENU_ITEM_ADDED',
    'MENU_ITEM_PATCHED',
    'MENU_ITEM_DELETED',
    'MENU_ITEMS_SORTED',
    'DIFFERENT_MENUS_ERROR',
    'DIFFERENT_PARENTS_ERROR',
    'NO_SUCH_MENU_ITEM_CHART',
    'MENU_ITEM_CHART_ADDED',
    'MENU_ITEM_CHART_DELETED',
    'MENU_ITEM_CHARTS_SORTED',
    'DIFFERENT_MENU_ITEMS_ERROR',
    'MENU_XOR_PARENT']


NO_MENU_SPECIFIED = DSCMS4_MESSAGE('No menu specified.', status=400)
NO_SUCH_MENU = DSCMS4_MESSAGE('No such menu.', status=404)
INVALID_MENU_DATA = DSCMS4_MESSAGE('The menu data is invalid.', status=400)
MENU_ADDED = DSCMS4_MESSAGE('The menu has been added.', status=201)
MENU_PATCHED = DSCMS4_MESSAGE('The menu has been patched.', status=200)
MENU_COPIED = DSCMS4_MESSAGE('The menu has been copied.', status=200)
MENU_DELETED = DSCMS4_MESSAGE('The menu has been deleted.', status=200)
NO_MENU_ITEM_SPECIFIED = DSCMS4_MESSAGE('No menu item specified.', status=400)
NO_SUCH_MENU_ITEM = DSCMS4_MESSAGE('No such menu item.', status=404)
MENU_ITEM_ADDED = DSCMS4_MESSAGE('The menu item has been added.', status=201)
MENU_ITEM_PATCHED = DSCMS4_MESSAGE(
    'The menu item has been patched.', status=200)
MENU_ITEM_DELETED = DSCMS4_MESSAGE(
    'The menu item has been deleted.', status=200)
MENU_ITEMS_SORTED = DSCMS4_MESSAGE(
    'The menu items have been sorted.', status=200)
DIFFERENT_MENUS_ERROR = DSCMS4_MESSAGE(
    'The menu items are members of different menus.', status=400)
DIFFERENT_PARENTS_ERROR = DSCMS4_MESSAGE(
    'The menu items have different parent items.', status=400)
NO_SUCH_MENU_ITEM_CHART = DSCMS4_MESSAGE(
    'The menu item chart does not exist.', status=404)
MENU_ITEM_CHART_ADDED = DSCMS4_MESSAGE(
    'The menu item chart has been added.', status=201)
MENU_ITEM_CHART_DELETED = DSCMS4_MESSAGE(
    'The menu item chart has been deleted.', status=200)
MENU_ITEM_CHARTS_SORTED = DSCMS4_MESSAGE(
    'The menu item charts have been sorted.', status=200)
DIFFERENT_MENU_ITEMS_ERROR = DSCMS4_MESSAGE(
    'The menu item charts are members of different menu items.', status=400)
MENU_XOR_PARENT = DSCMS4_MESSAGE(
    'Must specify exclusively a menu or a parent menu item.', status=400)
