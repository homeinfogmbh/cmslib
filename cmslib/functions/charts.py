"""Charts related functions."""

from flask import request
from werkzeug.local import LocalProxy

from his import ACCOUNT, CUSTOMER
from his.messages.data import INVALID_DATA, NOT_AN_INTEGER

from cmslib.messages.charts import INVALID_CHART_TYPE
from cmslib.messages.charts import NO_CHART_TYPE_SPECIFIED
from cmslib.messages.charts import NO_SUCH_BASE_CHART
from cmslib.messages.charts import NO_SUCH_CHART
from cmslib.orm.charts import CHARTS, ChartMode, BaseChart
from cmslib.orm.chart_types import ChartType


__all__ = [
    'CHART_TYPES',
    'CHART_TYPE',
    'get_base_chart',
    'get_charts',
    'get_chart',
    'get_mode'
]


def _get_chart_types():
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
            raise INVALID_CHART_TYPE


def _filter_chart_types():
    """Yields filtered chart types."""

    for chart_type in _get_chart_types():
        if ACCOUNT.root or ChartType.can_use(CUSTOMER.id, chart_type):
            yield chart_type


CHART_TYPES = LocalProxy(_filter_chart_types)


def _get_chart_type():
    """Returns the selected chart type."""

    try:
        chart_type = request.args['type']
    except KeyError:
        raise NO_CHART_TYPE_SPECIFIED

    try:
        chart_type = CHARTS[chart_type]
    except KeyError:
        raise INVALID_CHART_TYPE

    if ACCOUNT.root or ChartType.can_use(CUSTOMER.id, chart_type):
        return chart_type

    raise INVALID_CHART_TYPE


CHART_TYPE = LocalProxy(_get_chart_type)


def _get_trashed():
    """Returns a selection for the trashed status."""

    trashed = request.args.get('trashed')

    if trashed is None:
        return True     # Don't care.

    try:
        trashed = int(trashed)
    except ValueError:
        raise NOT_AN_INTEGER.update(key='trashed', value=trashed)

    if trashed:
        return BaseChart.trashed == 1

    return BaseChart.trashed == 0


def get_base_chart(ident):
    """Returns the respective base chart."""

    condition = BaseChart.id == ident
    condition &= BaseChart.customer == CUSTOMER

    try:
        return BaseChart.get(condition)
    except BaseChart.DoesNotExist:
        raise NO_SUCH_BASE_CHART


def get_charts():
    """Lists the available charts."""

    condition = BaseChart.customer == CUSTOMER.id
    condition &= _get_trashed()

    for typ in CHART_TYPES:
        for record in typ.select().join(BaseChart).where(condition):
            yield record


def get_chart(ident, type=CHART_TYPE):  # pylint: disable=W0622
    """Returns the selected chart."""

    condition = BaseChart.customer == CUSTOMER.id
    condition &= type.id == ident

    try:
        return type.select().join(BaseChart).where(condition).get()
    except type.DoesNotExist:
        raise NO_SUCH_CHART


def get_mode():
    """Determines the extend of the dataset."""

    try:
        mode = request.args['mode']
    except KeyError:
        return ChartMode.FULL

    try:
        return ChartMode(mode)
    except ValueError:
        raise INVALID_DATA.update(key='mode', value=mode)
