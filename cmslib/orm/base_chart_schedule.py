"""Base chart related schedules."""

from peewee import ForeignKeyField

from cmslib.functions.charts import get_base_chart
from cmslib.functions.schedule import get_schedule
from cmslib.messages.schedule import NO_BASE_CHART_SPECIFIED
from cmslib.messages.schedule import NO_SCHEDULE_SPECIFIED
from cmslib.orm.charts import BaseChart
from cmslib.orm.common import UNCHANGED, DSCMS4Model
from cmslib.orm.schedule import Schedule


__all__ = ['MODELS', 'BaseChartSchedule']


class BaseChartSchedule(DSCMS4Model):  # pylint: disable=R0901
    """A schedule for base charts."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'base_chart_schedule'

    base_chart = ForeignKeyField(
        BaseChart, column_name='base_chart', on_delete='CASCADE')
    schedule = ForeignKeyField(
        Schedule, column_name='schedule', on_delete='CASCADE')

    @classmethod
    def from_json(cls, json, **kwargs):
        """Returns a new base chart schedule from a JSON-ish dict."""
        try:
            base_chart = json.pop('baseChart')
        except KeyError:
            raise NO_BASE_CHART_SPECIFIED

        try:
            schedule = json.pop('schedule')
        except KeyError:
            raise NO_SCHEDULE_SPECIFIED

        record = super().from_json(json, **kwargs)
        record.base_chart = get_base_chart(base_chart)
        record.schedule = get_schedule(schedule)
        return record

    def patch_json(self, json, **kwargs):
        """Patches the base chart schedule with a JSON-ish dict."""
        base_chart = json.pop('baseChart', UNCHANGED)
        schedule = json.pop('schedule', UNCHANGED)
        super().patch_json(json, **kwargs)

        if base_chart is not UNCHANGED:
            self.base_chart = get_base_chart(base_chart)

        if schedule is not UNCHANGED:
            self.schedule = get_schedule(base_chart)


MODELS = (BaseChartSchedule,)
