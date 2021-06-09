"""VFS related functions."""

from peewee import JOIN, ModelSelect

from his import CUSTOMER

from cmslib.orm.charts import BaseChart
from cmslib.orm.vfs import ContentChart, Directory


__all__ = [
    'get_directories',
    'get_root',
    'get_directory',
    'get_root_base_charts'
]


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


def get_root_base_charts() -> ModelSelect:
    """Lists root directories of the current customer."""

    return BaseChart.select(cascase=True).join_from(
        BaseChart, ContentChart, join_type=JOIN.LEFT_OUTER).where(
        (BaseChart.customer == CUSTOMER.id)
        & (ContentChart.directory >> None)
    )
