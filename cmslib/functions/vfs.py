"""VFS related functions."""

from peewee import ModelSelect

from his import CUSTOMER

from cmslib.orm.vfs import Directory


__all__ = ['get_directories', 'get_root', 'get_directory']


def get_directories() -> ModelSelect:
    """Lists directories of the current customer."""

    return Directory.select(cascade=True).where(
        Directory.customer == CUSTOMER.id)


def get_root() -> ModelSelect:
    """Lists root directories of the current customer."""

    return get_directories().where(Directory.parent >> None)


def get_directory(ident: int) -> Directory:
    """Selects a specific directory."""

    return get_directories().where(Directory.id == ident).get()
