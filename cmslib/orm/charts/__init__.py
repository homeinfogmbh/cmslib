"""Chart ORM models.

This package provides ORM models
of the "chart" types of the CMS.
"""
from cmslib.orm.charts.api import CHARTS
from cmslib.orm.charts.api import ChartMode
from cmslib.orm.charts.api import BaseChart
from cmslib.orm.charts.api import Chart
from cmslib.orm.charts.api import ChartPIN
from cmslib.orm.charts.blackboard import Blackboard, Image as BlackboardImage
from cmslib.orm.charts.booking import Booking, BookableMapping
from cmslib.orm.charts.cleaning import Cleaning
from cmslib.orm.charts.facebook import Facebook, Account as FacebookAccount
from cmslib.orm.charts.form import Form
from cmslib.orm.charts.garbage_collection import GarbageCollection
from cmslib.orm.charts.guess_picture import GuessPicture
from cmslib.orm.charts.image_text import ImageText
from cmslib.orm.charts.image_text import Image as ImageTextImage
from cmslib.orm.charts.image_text import Text as ImageTextText
from cmslib.orm.charts.news import News, NewsProvider
from cmslib.orm.charts.poll import Poll
from cmslib.orm.charts.poll import Mode as PollMode
from cmslib.orm.charts.poll import Option as PollOption
from cmslib.orm.charts.public_transport import PublicTransport
from cmslib.orm.charts.quotes import Quotes
from cmslib.orm.charts.real_estates import RealEstates
from cmslib.orm.charts.real_estates import IdFilter
from cmslib.orm.charts.real_estates import ZipCodeFilter
from cmslib.orm.charts.soccer_table import SoccerTable
from cmslib.orm.charts.url import URL, Mode as URLMode
from cmslib.orm.charts.video import Video
from cmslib.orm.charts.weather import Weather, Image as WeatherImage


__all__ = [
    'CHARTS',
    'MODELS',
    'ChartMode',
    'BaseChart',
    'Chart',
    'ChartPIN',
    'Blackboard',
    'BlackboardImage',
    'Booking',
    'BookableMapping',
    'Cleaning',
    'Facebook',
    'FacebookAccount',
    'Form',
    'GarbageCollection',
    'GuessPicture',
    'ImageText',
    'ImageTextImage',
    'ImageTextText',
    'News',
    'NewsProvider',
    'Poll',
    'PollMode',
    'PollOption',
    'PublicTransport',
    'Quotes',
    'RealEstates',
    'IdFilter',     # Filter for real estates.
    'ZipCodeFilter',    # Filter for real estates.
    'SoccerTable',
    'URL',
    'URLMode',
    'Video',
    'Weather',
    'WeatherImage'
]


MODELS = (
    BaseChart, ChartPIN, Booking, BookableMapping, Cleaning, Facebook,
    FacebookAccount, Form, GarbageCollection, GuessPicture, ImageText,
    ImageTextImage, ImageTextText, Blackboard, BlackboardImage, News,
    NewsProvider, Poll, PollOption, PublicTransport, Quotes, RealEstates,
    IdFilter, ZipCodeFilter, SoccerTable, URL, Video, Weather, WeatherImage
)
