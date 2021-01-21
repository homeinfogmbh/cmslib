"""Error messages and mappings."""

from wsgilib import JSONMessage

from cmslib.exceptions import AmbiguousBaseChart
from cmslib.exceptions import AmbiguousConfigurationsError
from cmslib.exceptions import CircularReference
from cmslib.exceptions import DifferentMenus
from cmslib.exceptions import InvalidChartType
from cmslib.exceptions import MissingMenu
from cmslib.exceptions import NoConfigurationFound
from cmslib.exceptions import OrphanedBaseChart
from cmslib.orm.charts import CHARTS, BaseChart
from cmslib.orm.configuration import Configuration


__all__ = ['ERRORS']


CHART_ERRORS = {
    chart.DoesNotExist: lambda _: JSONMessage('No such chart.', status=404)
    for chart in CHARTS.values()
}


ERRORS = {
    **CHART_ERRORS,
    AmbiguousBaseChart: lambda error: JSONMessage(
        'Ambiguous base chart.', base_chart=error.base_chart.to_json(),
        references=[ref.to_json() for ref in error.references], status=400),
    AmbiguousConfigurationsError: lambda error: JSONMessage(
        'Ambiguous configurations.', level=error.level, index=error.index,
        status=400),
    BaseChart.DoesNotExist: lambda _: JSONMessage(
        'No such base chart.', status=404),
    CircularReference: lambda error: JSONMessage(
        'Circular reference.', type=type(error.model).__name__,
        model=error.model.to_json(), status=400),
    DifferentMenus: lambda error: JSONMessage(
        'Different menus.', menu=error.menu.to_json(),
        other=error.other.to_json(), status=400),
    InvalidChartType: lambda error: JSONMessage(
        'Invalid chart type.', name=str(error), status=400),
    MissingMenu: lambda _: JSONMessage('Missing Menu.', status=404),
    NoConfigurationFound: lambda _: JSONMessage(
        'No configuration found.', status=404),
    Configuration.DoesNotExist: lambda _: JSONMessage(
        'No such configuration.', status=404),
    OrphanedBaseChart: lambda error: JSONMessage(
        'Orphaned base chart.', base_chart=error.base_chart.to_json(),
        status=400),
}
