"""Charts related functions."""

from typing import Iterator

from flask import request
from peewee import Expression, ModelBase, ModelSelect
from werkzeug.local import LocalProxy

from his import ACCOUNT, CUSTOMER
from his.messages.data import INVALID_DATA, NOT_AN_INTEGER
from peeweeplus import select_tree

from cmslib.messages.charts import INVALID_CHART_TYPE
from cmslib.messages.charts import NO_CHART_TYPE_SPECIFIED
from cmslib.messages.charts import NO_SUCH_BASE_CHART
from cmslib.messages.charts import NO_SUCH_CHART
from cmslib.orm.chart_acl import ChartACL
from cmslib.orm.charts import CHARTS, BaseChart, Chart, ChartMode


__all__ = [
    'CHART_TYPES',
    'CHART_TYPE',
    'get_base_chart',
    'get_charts',
    'get_chart',
    'get_mode'
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
            raise INVALID_CHART_TYPE from None


def _filtered_chart_types() -> Iterator[Chart]:
    """Yields filtered chart types."""

    for chart_type in _get_chart_types():
        if ACCOUNT.root or ChartACL.can_use(CUSTOMER.id, chart_type):
            yield chart_type


CHART_TYPES = LocalProxy(_filtered_chart_types)


def _get_chart_type() -> Chart:
    """Returns the selected chart type."""

    try:
        chart_type = request.args['type']
    except KeyError:
        raise NO_CHART_TYPE_SPECIFIED from None

    try:
        chart_type = CHARTS[chart_type]
    except KeyError:
        raise INVALID_CHART_TYPE from None

    if ACCOUNT.root or ChartACL.can_use(CUSTOMER.id, chart_type):
        return chart_type

    raise INVALID_CHART_TYPE


CHART_TYPE = LocalProxy(_get_chart_type)


def _get_trashed() -> Expression:
    """Returns a selection for the trashed status."""

    trashed = request.args.get('trashed')

    if trashed is None:
        return True     # Don't care.

    try:
        trashed = int(trashed)
    except ValueError:
        raise NOT_AN_INTEGER.update(key='trashed', value=trashed) from None

    if trashed:
        return BaseChart.trashed == 1

    return BaseChart.trashed == 0


def get_base_chart(ident: int) -> BaseChart:
    """Returns the respective base chart."""

    condition = BaseChart.id == ident
    condition &= BaseChart.customer == CUSTOMER

    try:
        return BaseChart.get(condition)
    except BaseChart.DoesNotExist:
        raise NO_SUCH_BASE_CHART from None


def get_charts() -> ModelSelect:
    """Lists the available charts."""

    condition = BaseChart.customer == CUSTOMER.id
    condition &= _get_trashed()

    for typ in CHART_TYPES:
        return select_tree(typ).where(condition)


def get_chart(ident: int, cls: ModelBase = CHART_TYPE) -> Chart:
    """Returns the selected chart."""

    condition = BaseChart.customer == CUSTOMER.id
    condition &= cls.id == ident

    try:
        return select_tree(cls).where(condition).get()
    except cls.DoesNotExist:
        raise NO_SUCH_CHART from None


def get_mode() -> ChartMode:
    """Determines the extend of the dataset."""

    try:
        mode = request.args['mode']
    except KeyError:
        return ChartMode.FULL

    try:
        return ChartMode(mode)
    except ValueError:
        raise INVALID_DATA.update(key='mode', value=mode) from None
