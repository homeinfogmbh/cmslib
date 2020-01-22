"""Schedules for recurring events."""

from enum import Enum

from peewee import DateTimeField, IntegerField, TextField

from peeweeplus import EnumField

from cmslib import dom  # pylint: disable=E0611
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

    def to_dom(self):
        """Returns an XML DOM."""
        xml = dom.Schedule()
        xml.description = self.description
        xml.start = self.start
        xml.end = self.end
        xml.duration = dom.TimeInterval()
        xml.duration.value_ = self.duration_value
        xml.duration.unit = self.duration_unit.value
        xml.interval = dom.TimeInterval()
        xml.interval.value_ = self.interval_value
        xml.interval.unit = self.interval_unit.value
        return xml


MODELS = (Schedule,)
