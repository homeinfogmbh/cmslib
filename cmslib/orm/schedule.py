"""Schedules for recurring events."""

from enum import Enum

from peewee import DateTimeField, IntegerField

from peeweeplus import EnumField

from cmslib.orm.common import CustomerModel


__all__ = ['MODELS', 'Schedule']


class TimeUnit(Enum):
    """Time units."""

    DAY = 'day'
    WEEK = 'week'
    MONTH = 'month'
    YEAR = 'year'


class Schedule(CustomerModel):
    """A schedule for recurring events."""

    start = DateTimeField()
    end = DateTimeField(null=True)
    duration_value = IntegerField()
    duration_unit = EnumField(TimeUnit)
    interval_value = IntegerField()
    interval_unit = EnumField(TimeUnit)


MODELS = (Schedule,)
