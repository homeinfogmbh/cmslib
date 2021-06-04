"""Error messages and mappings."""

from hwdb import Deployment
from mdb import Customer
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
from cmslib.orm.chart_acl import ChartACL
from cmslib.orm.configuration import Configuration
from cmslib.orm.content.deployment import DeploymentBaseChart
from cmslib.orm.content.deployment import DeploymentConfiguration
from cmslib.orm.content.deployment import DeploymentMenu
from cmslib.orm.content.group import GroupBaseChart
from cmslib.orm.content.group import GroupConfiguration
from cmslib.orm.content.group import GroupMenu
from cmslib.orm.group import Group
from cmslib.orm.menu import Menu, MenuItem, MenuItemChart
from cmslib.orm.schedule import Schedule
from cmslib.orm.vfs import DirectoryNotEmpty, Directory


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
    ChartACL.DoesNotExist: lambda _: JSONMessage(
        'No such chart ACL.', status=404),
    CircularReference: lambda error: JSONMessage(
        'Circular reference.', type=type(error.model).__name__,
        model=error.model.to_json(), status=400),
    Customer.DoesNotExist: lambda _: JSONMessage(
        'No such customer.', status=404),
    Deployment.DoesNotExist: lambda _: JSONMessage(
        'No such deployment.', status=404),
    DeploymentBaseChart.DoesNotExist: lambda _: JSONMessage(
        'No such deployment base chart.', status=404),
    DeploymentConfiguration.DoesNotExist: lambda _: JSONMessage(
        'No such deployment configuration.', status=404),
    DeploymentMenu.DoesNotExist: lambda _: JSONMessage(
        'No such deployment menu.', status=404),
    DifferentMenus: lambda error: JSONMessage(
        'Different menus.', menu=error.menu.to_json(),
        other=error.other.to_json(), status=400),
    Directory.DoesNotExist: lambda _: JSONMessage(
        'No such directory.', status=404),
    DirectoryNotEmpty: lambda _: JSONMessage(
        'Directory is not empty.', status=400),
    Group.DoesNotExist: lambda _: JSONMessage('No such group.', status=404),
    GroupBaseChart.DoesNotExist: lambda _: JSONMessage(
        'No such group base chart.', status=404),
    GroupConfiguration.DoesNotExist: lambda _: JSONMessage(
        'No such group configuration.', status=404),
    GroupMenu.DoesNotExist: lambda _: JSONMessage(
        'No such group menu.', status=404),
    InvalidChartType: lambda error: JSONMessage(
        'Invalid chart type.', name=str(error), status=400),
    Menu.DoesNotExist: lambda _: JSONMessage('No such menu.', status=404),
    MenuItem.DoesNotExist: lambda _: JSONMessage(
        'No such menu item.', status=404),
    MenuItemChart.DoesNotExist: lambda _: JSONMessage(
        'No such menu item chart.', status=404),
    MissingMenu: lambda _: JSONMessage('Missing Menu.', status=404),
    NoConfigurationFound: lambda _: JSONMessage(
        'No configuration found.', status=404),
    Configuration.DoesNotExist: lambda _: JSONMessage(
        'No such configuration.', status=404),
    OrphanedBaseChart: lambda error: JSONMessage(
        'Orphaned base chart.', base_chart=error.base_chart.to_json(),
        status=400),
    Schedule.DoesNotExist: lambda _: JSONMessage(
        'No such schedule.', status=404),
}
