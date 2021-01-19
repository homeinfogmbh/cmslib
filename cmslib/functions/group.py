"""Group related functions."""

from peewee import ModelSelect

from his import CUSTOMER
from mdb import Address, Company, Customer

from cmslib.messages.group import NO_SUCH_GROUP
from cmslib.orm.group import Group


__all__ = ['get_group']


def list_group() -> ModelSelect:
    """Selects the groups of the current customer."""

    select = Group.select(Group, Customer, Company, Address)
    select = select.join(Customer).join(Company).join(Address)
    return select.where(Group.customer == CUSTOMER.id)


def get_group(ident: int) -> Group:
    """Returns the respective group of the current customer."""

    try:
        return list_group().where(Group.id == ident).get()
    except Group.DoesNotExist:
        raise NO_SUCH_GROUP from None
