"""File selection."""

from peewee import JOIN

from hisfs import File
from peeweeplus import ChangedConnection

from cmslib.orm.charts.blackboard import Blackboard, Image as BbImage
from cmslib.orm.charts.image_text import ImageText, Image as ItImage
from cmslib.orm.charts.real_estates import RealEstates, Contact
from cmslib.orm.charts.video import Video
from cmslib.orm.charts.weather import Weather, Image as WImage
from cmslib.orm.configuration import Configuration, Background
from cmslib.orm.menu import Menu, MenuItem


QUERY = File.select().join(MenuItem, JOIN.LEFT_OUTER).join(Menu)
QUERY = QUERY.join_from(File, ItImage, JOIN.LEFT_OUTER).join(ImageText)
QUERY = QUERY.join_from(File, BbImage, JOIN.LEFT_OUTER).join(Blackboard)
QUERY = QUERY.join_from(File, Video, JOIN.LEFT_OUTER)
QUERY = QUERY.join_from(File, WImage, JOIN.LEFT_OUTER).join(Weather)
QUERY = QUERY.join_from(File, Contact, JOIN.LEFT_OUTER).join(RealEstates)
QUERY = QUERY.join_from(File, Background, JOIN.LEFT_OUTER).join(Configuration)
LOGO = Configuration.logo == File.id
DUMMY_PICTURE = Configuration.dummy_picture == File.id
QUERY = QUERY.join_from(File, Configuration, JOIN.LEFT_OUTER, on=LOGO)
QUERY = QUERY.join_from(File, Configuration, JOIN.LEFT_OUTER, on=DUMMY_PICTURE)


def get_files(*, menus=None, image_text_charts=None, blackboard_charts=None,
              video_charts=None, weather_charts=None, real_estate_charts=None,
              configurations=None, base_charts=None):
    """Selects files for the given related records."""

    condition = True

    if menus is not None:
        condition &= Menu.id << menus

    if image_text_charts is not None:
        condition &= ImageText.id << image_text_charts

    if blackboard_charts is not None:
        condition &= Blackboard.id << blackboard_charts

    if video_charts is not None:
        condition &= Video.id << video_charts

    if weather_charts is not None:
        condition &= Weather.id << weather_charts

    if real_estate_charts is not None:
        condition &= RealEstates.id << real_estate_charts

    if configurations is not None:
        condition &= Configuration.id << configurations

    if base_charts is not None:
        bc_condition = ImageText.base << base_charts
        bc_condition |= Blackboard.base << base_charts
        bc_condition |= Video.base << base_charts
        bc_condition |= Weather.base << base_charts
        bc_condition |= RealEstates.base << base_charts
        condition &= bc_condition

    with ChangedConnection(File, ImageText):
        return QUERY.where(condition).execute()
