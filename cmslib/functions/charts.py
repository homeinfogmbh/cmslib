"""Charts related functions."""

from typing import Iterable, Iterator, Type, Union

from peewee import Expression, Select

from mdb import Customer

from cmslib.orm.chart_acl import ChartACL
from cmslib.orm.charts import BaseChart, Chart


__all__ = [
    'get_base_chart',
    'get_base_charts',
    'get_chart',
    'get_charts',
    'get_chart_acls'
]


def _get_charts(
        typ: Type[Chart],
        customer: Union[Customer, int],
        trashed: Union[Expression, bool] = True
) -> Select:
    """Selects charts of the given type for the given customer."""

    return typ.select(cascade=True).where(
        (BaseChart.customer == customer) & trashed
    )


def get_base_chart(ident: int, customer: Union[Customer, int]) -> BaseChart:
    """Returns the respective base chart of the given customer."""

    return get_base_charts(customer).where(BaseChart.id == ident).get()


def get_base_charts(customer: Union[Customer, int]) -> Select:
    """Returns the base charts of the given customer."""

    return BaseChart.select(cascade=True).where(
        BaseChart.customer == customer
    )


def get_chart(
        ident: int,
        customer: Union[Customer, int],
        typ: Type[Chart]
) -> Chart:
    """Returns the selected chart of the given customer."""

    return _get_charts(typ, customer).where(typ.id == ident).get()


def get_charts(
        customer: Union[Customer, int],
        types: Iterable[Type[Chart]],
        trashed: Union[Expression, bool] = True
) -> Iterator[Chart]:
    """Lists the chart types available to the given customer."""

    for typ in types:
        yield from _get_charts(typ, customer, trashed)


def get_chart_acls(customer: Union[Customer, int]) -> Select:
    """Returns chart ACLs of the given customer."""

    return ChartACL.select(cascade=True).where(
        ChartACL.customer == customer
    )
