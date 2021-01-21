"""Group related functions."""

from peewee import ModelSelect

from his import CUSTOMER

from cmslib.orm.group import Group


__all__ = ['get_group', 'get_groups']


def get_groups() -> ModelSelect:
    """Selects the groups of the current customer."""

    return Group.select(cascade=True).where(Group.customer == CUSTOMER.id)


def get_group(ident: int) -> Group:
    """Returns the respective group of the current customer."""

    return get_groups().where(Group.id == ident).get()
