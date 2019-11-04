"""Schedules for recurring events."""

from enum import Enum

from peewee import DateTimeField, ForeignKeyField, IntegerField, TextField

from peeweeplus import EnumField

from cmslib.orm.charts import BaseChart
from cmslib.orm.common import CustomerModel, DSCMS4Model


__all__ = ['MODELS', 'Schedule', 'BaseChartSchedule']


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


class BaseChartSchedule(DSCMS4Model):  # pylint: disable=R0901
    """A schedule for base charts."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'base_chart_schedule'

    base_chart = ForeignKeyField(
        BaseChart, column_name='base_chart', on_delete='CASCADE')
    schedule = ForeignKeyField(
        Schedule, column_name='schedule', on_delete='CASCADE')


MODELS = (Schedule, BaseChartSchedule)
