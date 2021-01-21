"""Error messages and mappings."""

from wsgilib import JSONMessage

from cmslib.exceptions import AmbiguousBaseChart
from cmslib.exceptions import AmbiguousConfigurationsError
from cmslib.exceptions import CircularReference
from cmslib.exceptions import DifferentMenus
from cmslib.exceptions import MissingMenu
from cmslib.exceptions import NoConfigurationFound
from cmslib.exceptions import OrphanedBaseChart


__all__ = ['ERRORS']


ERRORS = {
    AmbiguousBaseChart: lambda error: JSONMessage(
        'Ambiguous base chart.', base_chart=error.base_chart.to_json(),
        references=[ref.to_json() for ref in error.references], status=400),
    AmbiguousConfigurationsError: lambda error: JSONMessage(
        'Ambiguous configurations.', level=error.level, index=error.index,
        status=400),
    CircularReference: lambda error: JSONMessage(
        'Circular reference.', type=type(error.model).__name__,
        model=error.model.to_json(), status=400),
    DifferentMenus: lambda error: JSONMessage(
        'Different menus.', menu=error.menu.to_json(),
        other=error.other.to_json(), status=400),
    MissingMenu: lambda _: JSONMessage('Missing Menu.', status=404),
    NoConfigurationFound: lambda _: JSONMessage(
        'No configuration found.', status=404),
    OrphanedBaseChart: lambda error: JSONMessage(
        'Orphaned base chart.', base_chart=error.base_chart.to_json(),
        status=400),
}
