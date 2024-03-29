"""Base chart and PINs.

The BaseChart contains information common to all chart types.
"""

from datetime import datetime
from logging import getLogger
from typing import Type
from uuid import uuid4

from peewee import JOIN
from peewee import BooleanField
from peewee import CharField
from peewee import DateTimeField
from peewee import ForeignKeyField
from peewee import Select
from peewee import SmallIntegerField
from peewee import UUIDField

from peeweeplus import EnumField, HTMLCharField, HTMLTextField, Transaction

from cmslib import dom
from cmslib.exceptions import OrphanedBaseChart, AmbiguousBaseChart
from cmslib.orm.charts.api.common import CHARTS
from cmslib.orm.charts.api.common import Transitions
from cmslib.orm.charts.api.common import CheckResult
from cmslib.orm.common import UNCHANGED, DSCMS4Model, CustomerModel
from cmslib.orm.schedule import Schedule


__all__ = ["BaseChart", "ChartPIN"]


LOGGER = getLogger(__file__)


class BaseChart(CustomerModel):
    """Common basic chart data model."""

    class Meta:
        table_name = "base_chart"

    type = CharField()
    uuid = UUIDField(default=uuid4)
    title = HTMLCharField(255)
    description = HTMLTextField(null=True)
    duration = SmallIntegerField(default=10)
    position = SmallIntegerField(null=True)
    display_from = DateTimeField(null=True)
    display_until = DateTimeField(null=True)
    transition = EnumField(Transitions, null=True)
    created = DateTimeField(default=datetime.now)
    trashed = BooleanField(default=False)
    log = BooleanField(default=False)
    schedule = ForeignKeyField(
        Schedule,
        column_name="schedule",
        null=True,
        on_delete="SET NULL",
        on_update="CASCADE",
        lazy_load=False,
    )

    @classmethod
    def from_json(cls, json: dict, typ: str, skip: set = None, **kwargs) -> Transaction:
        """Creates a base chart from a JSON-ish dict."""
        skip = {"type", "uuid", *(skip or ())}
        pins = json.pop("pins", ())
        schedule = json.pop("schedule", None)
        record = super().from_json(json, skip=skip, **kwargs)
        record.type = typ
        transaction = Transaction()
        transaction.add(record, primary=True)

        for pin in pins:
            chart_pin = ChartPIN(base_chart=record, pin=pin)
            transaction.add(chart_pin)

        if schedule:
            record.schedule = schedule = Schedule.from_json(schedule)
            transaction.add(schedule, left=True)

        return transaction

    @classmethod
    def check(cls, *, verbose: bool = False) -> CheckResult:
        """Checks base charts."""
        orphans = set()
        ambiguous = set()

        for base_chart in cls:
            try:
                chart = base_chart.chart
            except OrphanedBaseChart as orphaned_base_chart:
                orphans.add(base_chart)

                if verbose:
                    LOGGER.error(orphaned_base_chart)
            except AmbiguousBaseChart as ambiguous_base_chart:
                ambiguous.add(base_chart)

                if verbose:
                    LOGGER.error(ambiguous_base_chart)
            else:
                if verbose:
                    LOGGER.info("%s ↔ %s", base_chart, chart)

        return CheckResult(frozenset(orphans), frozenset(ambiguous))

    @classmethod
    def select(cls, *args, cascade: bool = False) -> Select:
        """Selects records."""
        if not cascade:
            return super().select(*args)

        return (
            super()
            .select(cls, Schedule, *args, cascade=cascade)
            .join_from(BaseChart, Schedule, join_type=JOIN.LEFT_OUTER)
        )

    @property
    def active(self) -> bool:
        """Determines whether the chart is considered active."""
        return self.is_active_at(datetime.now())

    @property
    def chart_class(self) -> Type[DSCMS4Model]:
        """Yields all charts that associate this base chart."""
        return CHARTS[self.type]

    @property
    def chart(self) -> DSCMS4Model:
        """Returns the mapped implementation of this base chart."""
        return (
            (Chart := self.chart_class)
            .select(cascade=True)
            .where(Chart.base == self)
            .get()
        )

    def _patch_pins(self, pins: dict, transaction: Transaction):
        """Patches the PINs."""
        if pins is UNCHANGED:
            return

        for chart_pin in self.pins:
            transaction.delete(chart_pin)

        if not pins:
            return

        for pin in pins:
            chart_pin = ChartPIN(base_chart=self, pin=pin)
            transaction.add(chart_pin)

    def _patch_schedule(self, schedule: dict, transaction: Transaction):
        """Patches the schedule."""
        if schedule is UNCHANGED:
            return

        if self.schedule:
            transaction.delete(self.schedule)

        if schedule:
            self.schedule = schedule = Schedule.from_json(schedule)
            transaction.add(schedule, left=True)
        else:
            self.schedule = None

    def is_active_at(self, timestamp: datetime) -> bool:
        """Checks whether this chart is active at the given timestamp."""
        return (self.display_from is None or self.display_from > timestamp) and (
            self.display_until is None or self.display_until < timestamp
        )

    def patch_json(self, json: dict, **kwargs) -> Transaction:
        """Patches the base chart."""
        pins = json.pop("pins", UNCHANGED)
        schedule = json.pop("schedule", UNCHANGED)
        super().patch_json(json, **kwargs)
        transaction = Transaction()
        transaction.add(self, primary=True)
        self._patch_pins(pins, transaction)
        self._patch_schedule(schedule, transaction)
        return transaction

    def to_json(self, brief: bool = False, **kwargs) -> dict:
        """Returns a JSON-ish dictionary."""
        if brief:
            return {"title": self.title}

        json = super().to_json(**kwargs)
        json["pins"] = [pin.pin for pin in self.pins]

        if self.schedule:
            json["schedule"] = self.schedule.to_json()

        return json

    def to_dom(self) -> dom.BaseChart:
        """Returns an XML DOM of the base chart."""
        xml = dom.BaseChart()
        xml.id = self.id
        xml.uuid = self.uuid.hex
        xml.title = self.title
        xml.description = self.description
        xml.duration = self.duration
        xml.position = self.position
        xml.display_from = self.display_from
        xml.display_until = self.display_until

        if self.transition is not None:
            xml.transition = self.transition.value

        xml.created = self.created
        xml.trashed = self.trashed
        xml.log = self.log

        if self.schedule:
            xml.schedule = self.schedule.to_dom()

        xml.pin = [pin.pin for pin in self.pins]
        return xml


class ChartPIN(DSCMS4Model):
    """PINs to lock a chart."""

    class Meta:
        table_name = "chart_pin"

    base_chart = ForeignKeyField(
        BaseChart,
        column_name="base_chart",
        backref="pins",
        on_delete="CASCADE",
        on_update="CASCADE",
        lazy_load=False,
    )
    pin = HTMLCharField(8)
