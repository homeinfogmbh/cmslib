"""Charts related functions."""

from typing import Iterator

from flask import request
from peewee import Expression, ModelBase, ModelSelect
from werkzeug.local import LocalProxy

from his import ACCOUNT, CUSTOMER
from wsgilib import get_bool

from cmslib.exceptions import InvalidChartType
from cmslib.orm.chart_acl import ChartACL
from cmslib.orm.charts import CHARTS, BaseChart, Chart, ChartMode
from cmslib.orm.settings import Settings


__all__ = [
    'CHART_TYPES',
    'CHART_TYPE',
    'get_base_chart',
    'get_base_charts',
    'get_chart',
    'get_charts',
    'get_chart_acls',
    'get_mode',
    'get_trashed'
]


def _get_chart_types() -> Iterator[Chart]:
    """Yields selected chart types."""

    try:
        type_names = request.args['types']
    except KeyError:
        yield from CHARTS.values()
        return

    for type_name in type_names.split(','):
        try:
            yield CHARTS[type_name]
        except KeyError:
            raise InvalidChartType(type_name) from None


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


def get_trashed() -> bool:
    """Returns a flag whether trashed charts should be selected."""

    trashed = get_bool('trashed', default=None)

    if trashed is None:
        return Settings.for_customer(CUSTOMER.id).trashed

    return trashed


def get_base_charts() -> ModelSelect:
    """Returns the base charts of the current customer."""

    return BaseChart.select(cascade=True).where(BaseChart.customer == CUSTOMER)


def get_base_chart(ident: int) -> BaseChart:
    """Returns the respective base chart."""

    return get_base_charts().where(BaseChart.id == ident).get()


def _get_charts(cls: ModelBase) -> ModelSelect:
    """Selects charts of the given type for the current customer."""

    return cls.select(cascade=True).where(
        (BaseChart.customer == CUSTOMER.id)
        & (BaseChart.trashed == get_trashed()))


def get_charts() -> Iterator[Chart]:
    """Lists the available charts."""

    for cls in CHART_TYPES:
        yield from _get_charts(cls)


def get_chart(ident: int, cls: ModelBase = CHART_TYPE) -> Chart:
    """Returns the selected chart."""

    return _get_charts(cls).where(cls.id == ident).get()


def get_chart_acls() -> ModelSelect:
    """Returns chart ACLs of the current customer."""

    return ChartACL.select(cascade=True).where(
        ChartACL.customer == CUSTOMER.id)


def get_mode() -> ChartMode:
    """Determines the extend of the dataset."""

    try:
        mode = request.args['mode']
    except KeyError:
        return ChartMode.FULL

    return ChartMode(mode)
