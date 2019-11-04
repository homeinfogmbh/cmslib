"""Schedules for recurring events."""

from enum import Enum

from peewee import DateTimeField, IntegerField, TextField

from peeweeplus import EnumField

from cmslib.orm.common import CustomerModel


__all__ = ['MODELS', 'TimeUnit', 'Schedule']


class TimeUnit(Enum):
    """Time units."""

    DAY = 'day'
    WEEK = 'week'
    MONTH = 'month'
    YEAR = 'year'


class Schedule(CustomerModel):
    """A schedule for recurring events."""

    description = TextField(null=True)
    start = DateTimeField()
    end = DateTimeField(null=True)
    duration_value = IntegerField()
    duration_unit = EnumField(TimeUnit)
    interval_value = IntegerField()
    interval_unit = EnumField(TimeUnit)


MODELS = (Schedule,)
