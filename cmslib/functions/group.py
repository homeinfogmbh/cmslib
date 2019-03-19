"""Group related functions."""

from his import CUSTOMER

from cmslib.messages.group import NO_SUCH_GROUP
from cmslib.orm.group import Group


__all__ = ['get_group']


def get_group(ident):
    """Returns the respective group of the current customer."""

    try:
        return Group.get((Group.customer == CUSTOMER.id) & (Group.id == ident))
    except Group.DoesNotExist:
        raise NO_SUCH_GROUP
