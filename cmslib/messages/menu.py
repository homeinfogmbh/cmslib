"""Menu related messages."""

from wsgilib import JSONMessage


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
    'DIFFERENT_MENUS',
    'DIFFERENT_PARENTS',
    'NO_SUCH_MENU_ITEM_CHART',
    'MENU_ITEM_CHART_ADDED',
    'MENU_ITEM_CHART_DELETED',
    'MENU_ITEM_CHARTS_SORTED',
    'DIFFERENT_MENU_ITEMS',
    'MENU_XOR_PARENT']


NO_MENU_SPECIFIED = JSONMessage('No menu specified.', status=400)
NO_SUCH_MENU = JSONMessage('No such menu.', status=404)
INVALID_MENU_DATA = JSONMessage('The menu data is invalid.', status=400)
MENU_ADDED = JSONMessage('The menu has been added.', status=201)
MENU_PATCHED = JSONMessage('The menu has been patched.', status=200)
MENU_COPIED = JSONMessage('The menu has been copied.', status=200)
MENU_DELETED = JSONMessage('The menu has been deleted.', status=200)
NO_MENU_ITEM_SPECIFIED = JSONMessage('No menu item specified.', status=400)
NO_SUCH_MENU_ITEM = JSONMessage('No such menu item.', status=404)
MENU_ITEM_ADDED = JSONMessage('The menu item has been added.', status=201)
MENU_ITEM_PATCHED = JSONMessage('The menu item has been patched.', status=200)
MENU_ITEM_DELETED = JSONMessage('The menu item has been deleted.', status=200)
MENU_ITEMS_SORTED = JSONMessage('The menu items have been sorted.', status=200)
DIFFERENT_MENUS = JSONMessage(
    'The menu items are members of different menus.', status=400)
DIFFERENT_PARENTS = JSONMessage(
    'The menu items have different parent items.', status=400)
NO_SUCH_MENU_ITEM_CHART = JSONMessage(
    'The menu item chart does not exist.', status=404)
MENU_ITEM_CHART_ADDED = JSONMessage(
    'The menu item chart has been added.', status=201)
MENU_ITEM_CHART_DELETED = JSONMessage(
    'The menu item chart has been deleted.', status=200)
MENU_ITEM_CHARTS_SORTED = JSONMessage(
    'The menu item charts have been sorted.', status=200)
DIFFERENT_MENU_ITEMS = JSONMessage(
    'The menu item charts are members of different menu items.', status=400)
MENU_XOR_PARENT = JSONMessage(
    'Must specify exclusively a menu or a parent menu item.', status=400)
