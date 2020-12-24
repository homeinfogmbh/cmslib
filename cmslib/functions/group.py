"""Group related functions."""

from his import CUSTOMER

from cmslib.messages.group import NO_SUCH_GROUP
from cmslib.orm.group import Group


__all__ = ['get_group']


def get_group(ident: int) -> Group:
    """Returns the respective group of the current customer."""

    condition = Group.customer == CUSTOMER.id
    condition &= Group.id == ident

    try:
        return Group.get(condition)
    except Group.DoesNotExist:
        raise NO_SUCH_GROUP from None
