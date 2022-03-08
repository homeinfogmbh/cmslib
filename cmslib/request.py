"""Request-context sensitive functions."""

from typing import Iterator, Type, Union

from his import ACCOUNT, CUSTOMER

from flask import request
from peewee import Expression
from werkzeug.local import LocalProxy

from mdb import Customer
from wsgilib import get_bool

from cmslib.exceptions import InvalidChartType
from cmslib.orm.chart_acl import ChartACL
from cmslib.orm.charts import CHARTS, BaseChart, Chart, ChartMode
from cmslib.orm.settings import Settings


__all__ = ['CHART_TYPE', 'CHART_TYPES', 'get_chart_mode', 'get_trashed_flag']


def _parse_charts(type_names: str) -> Iterator[Type[Chart]]:
    """Yields charts by type name."""

    for type_name in type_names.split(','):
        try:
            yield CHARTS[type_name]
        except KeyError:
            raise InvalidChartType(type_name) from None


def _get_chart_types() -> Iterator[Type[Chart]]:
    """Yields selected chart types."""

    try:
        type_names = request.args['types']
    except KeyError:
        return CHARTS.values()

    return _parse_charts(type_names)


def _filtered_chart_types() -> Iterator[Chart]:
    """Yields filtered chart types."""

    for chart_type in _get_chart_types():
        if ACCOUNT.root or ChartACL.can_use(CUSTOMER.id, chart_type):
            yield chart_type


CHART_TYPES = LocalProxy(_filtered_chart_types)


def _get_chart_type() -> Chart:
    """Returns the selected chart type."""

    chart_type = request.args['type']

    try:
        chart_type = CHARTS[chart_type]
    except KeyError:
        raise InvalidChartType(chart_type) from None

    if ACCOUNT.root or ChartACL.can_use(CUSTOMER.id, chart_type):
        return chart_type

    raise InvalidChartType(chart_type)


CHART_TYPE = LocalProxy(_get_chart_type)


def get_chart_mode() -> ChartMode:
    """Determines the extend of the dataset."""

    try:
        mode = request.args['mode']
    except KeyError:
        return ChartMode.FULL

    return ChartMode(mode)


def get_trashed_flag(
        customer: Union[Customer, int]
) -> Union[Expression, bool]:
    """Returns an expression to select base
    charts with a certain trashed flag.
    """

    if (trashed := get_bool('trashed', default=None)) is None:
        trashed = Settings.for_customer(customer).trashed

    if trashed is None:
        return True

    return BaseChart.trashed == trashed
