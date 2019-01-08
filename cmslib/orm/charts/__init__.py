"""Chart ORM models.

This package provides ORM models
of the "chart" types of the CMS.
"""
from cmslib.orm.charts.blackboard import Blackboard, Image as BlackboardImage
from cmslib.orm.charts.cleaning import Cleaning
from cmslib.orm.charts.common import ChartMode, BaseChart, Chart
from cmslib.orm.charts.facebook import Facebook, Account
from cmslib.orm.charts.form import Form
from cmslib.orm.charts.garbage_collection import GarbageCollection
from cmslib.orm.charts.guess_picture import GuessPicture
from cmslib.orm.charts.image_text import ImageText
from cmslib.orm.charts.image_text import Image as ImageTextImage
from cmslib.orm.charts.image_text import Text
from cmslib.orm.charts.news import News
from cmslib.orm.charts.poll import PollMode, Poll, Option as PollOption
from cmslib.orm.charts.public_transport import PublicTransport
from cmslib.orm.charts.quotes import Quotes
from cmslib.orm.charts.real_estates import RealEstates
from cmslib.orm.charts.real_estates import IdFilter
from cmslib.orm.charts.real_estates import ZipCodeFilter
from cmslib.orm.charts.video import Video
from cmslib.orm.charts.weather import Weather, Image as WeatherImage


__all__ = ['MODELS', 'ChartMode', 'BaseChart', 'Chart']


MODELS = (
    BaseChart, Cleaning, Facebook, Account, Form, GarbageCollection,
    GuessPicture, ImageText, ImageTextImage, Blackboard, BlackboardImage, Text,
    News, Poll, PollOption, PublicTransport, Quotes, RealEstates, IdFilter,
    ZipCodeFilter, Video, Weather, WeatherImage)
