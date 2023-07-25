"""Object-relational mappings.

This package provides the CMS's database models.
"""
from logging import getLogger

from cmslib.orm.charts import CHARTS
from cmslib.orm.charts import MODELS as CHART_MODELS
from cmslib.orm.charts import ChartMode
from cmslib.orm.charts import BaseChart
from cmslib.orm.charts import Chart
from cmslib.orm.charts import ChartPIN
from cmslib.orm.charts import Blackboard
from cmslib.orm.charts import BlackboardImage
from cmslib.orm.charts import Booking
from cmslib.orm.charts import BookableMapping
from cmslib.orm.charts import Cleaning
from cmslib.orm.charts import Form
from cmslib.orm.charts import GarbageCollection
from cmslib.orm.charts import GuessPicture
from cmslib.orm.charts import ImageText
from cmslib.orm.charts import ImageTextImage
from cmslib.orm.charts import ImageTextText
from cmslib.orm.charts import News
from cmslib.orm.charts import NewsProvider
from cmslib.orm.charts import Poll
from cmslib.orm.charts import PollMode
from cmslib.orm.charts import PollOption
from cmslib.orm.charts import PublicTransport
from cmslib.orm.charts import Quotes
from cmslib.orm.charts import RealEstates
from cmslib.orm.charts import IdFilter
from cmslib.orm.charts import ZipCodeFilter
from cmslib.orm.charts import SoccerTable
from cmslib.orm.charts import URL
from cmslib.orm.charts import URLMode
from cmslib.orm.charts import Video
from cmslib.orm.charts import Weather
from cmslib.orm.charts import WeatherImage
from cmslib.orm.common import DATABASE, UNCHANGED
from cmslib.orm.content import MODELS as CONTENT_MODELS
from cmslib.orm.content import DeploymentBaseChart
from cmslib.orm.content import DeploymentConfiguration
from cmslib.orm.content import DeploymentMenu
from cmslib.orm.content import GroupBaseChart
from cmslib.orm.content import GroupConfiguration
from cmslib.orm.content import GroupMenu
from cmslib.orm.chart_acl import MODELS as CHART_ACL_MODELS
from cmslib.orm.chart_acl import ChartACL
from cmslib.orm.configuration import MODELS as CONFIGURATION_MODELS
from cmslib.orm.configuration import Background
from cmslib.orm.configuration import Backlight
from cmslib.orm.configuration import Colors
from cmslib.orm.configuration import Configuration
from cmslib.orm.configuration import Design
from cmslib.orm.configuration import Font
from cmslib.orm.configuration import Ticker
from cmslib.orm.configuration import TickerType
from cmslib.orm.group import MODELS as GROUP_MODELS
from cmslib.orm.group import Group
from cmslib.orm.group import GroupMemberDeployment
from cmslib.orm.menu import MODELS as MENU_MODELS
from cmslib.orm.menu import Menu
from cmslib.orm.menu import MenuItem
from cmslib.orm.menu import MenuItemChart
from cmslib.orm.menu import MenuItemGroup
from cmslib.orm.schedule import MODELS as SCHEDULE_MODELS
from cmslib.orm.schedule import Schedule
from cmslib.orm.schedule import TimeUnit
from cmslib.orm.settings import MODELS as SETTINGS_MODELS
from cmslib.orm.settings import Settings
from cmslib.orm.vfs import MODELS as VFS_MODELS
from cmslib.orm.vfs import DirectoryNotEmpty
from cmslib.orm.vfs import Directory
from cmslib.orm.vfs import ContentChart


__all__ = [
    # Misc
    "DATABASE",
    "MODELS",
    "UNCHANGED",
    "create_tables",
    # Charts
    "CHARTS",
    "ChartMode",
    "BaseChart",
    "Chart",
    "ChartPIN",
    "Blackboard",
    "BlackboardImage",
    "Booking",
    "BookableMapping",
    "Cleaning",
    "Form",
    "GarbageCollection",
    "GuessPicture",
    "ImageText",
    "ImageTextImage",
    "ImageTextText",
    "News",
    "NewsProvider",
    "Poll",
    "PollMode",
    "PollOption",
    "PublicTransport",
    "Quotes",
    "RealEstates",
    "IdFilter",  # Filter for real estates.
    "ZipCodeFilter",  # Filter for real estates.
    "SoccerTable",
    "URL",
    "URLMode",
    "Video",
    "Weather",
    "WeatherImage",
    # Content
    "DeploymentBaseChart",
    "DeploymentConfiguration",
    "DeploymentMenu",
    "GroupBaseChart",
    "GroupConfiguration",
    "GroupMenu",
    # Chart ACLs
    "ChartACL",
    # Configuration
    "Background",
    "Backlight",
    "Colors",
    "Configuration",
    "Design",
    "Font",
    "Ticker",
    "TickerType",
    # Group
    "Group",
    "GroupMemberDeployment",
    # Menu
    "Menu",
    "MenuItem",
    "MenuItemChart",
    "MenuItemGroup",
    # Schedule
    "Schedule",
    "TimeUnit",
    # Settings
    "Settings",
    # VFS
    "DirectoryNotEmpty",
    "Directory",
    "ContentChart",
]


LOGGER = getLogger(__file__)

# Order matters here!
MODELS = (
    *CHART_MODELS,
    *CONFIGURATION_MODELS,
    *GROUP_MODELS,
    *MENU_MODELS,
    *CONTENT_MODELS,
    *CHART_ACL_MODELS,
    *SCHEDULE_MODELS,
    *SETTINGS_MODELS,
    *VFS_MODELS,
)


def create_tables(fail_silently: bool = True) -> None:
    """Create the respective tables."""

    for model in MODELS:
        try:
            model.create_table(fail_silently=fail_silently)
        except Exception as error:
            LOGGER.error('Could not create table for model "%s":\n%s.', model, error)
