"""VFS related functions."""

from typing import Union

from peewee import JOIN, Select

from mdb import Customer

from cmslib.orm.charts import BaseChart
from cmslib.orm.vfs import ContentChart, Directory


__all__ = [
    'get_directories',
    'get_root',
    'get_directory',
    'get_unassigned_base_charts'
]


def get_directories(customer: Union[Customer, int]) -> Select:
    """Lists directories of the given customer."""

    return Directory.select(cascade=True).where(
        Directory.customer == customer
    )


def get_root(customer: Union[Customer, int]) -> Select:
    """Lists root directories of the given customer."""

    return get_directories(customer).where(Directory.parent >> None)


def get_directory(ident: int, customer: Union[Customer, int]) -> Directory:
    """Selects a specific directory of the given customer."""

    return get_directories(customer).where(Directory.id == ident).get()


def get_unassigned_base_charts(customer: Union[Customer, int]) -> Select:
    """Lists unassigned base charts of the given customer."""

    return BaseChart.select(cascade=True).join_from(
        BaseChart, ContentChart, join_type=JOIN.LEFT_OUTER).where(
        (BaseChart.customer == customer)
        & (ContentChart.directory >> None)
    )
