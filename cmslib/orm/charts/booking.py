"""Booking chart."""

from peewee import BooleanField, ForeignKeyField, TextField

from bookings import get_bookable, Bookable

from cmslib import dom
from cmslib.orm.charts.common import Chart, ChartMode
from cmslib.orm.common import DSCMS4Model


__all__ = ['Booking', 'BookableMapping']


_UNCHANGED = object()


class Booking(Chart):
    """Chart for booking."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'chart_booking'

    rentee = BooleanField(null=True)
    purpose = BooleanField(null=True)
    text = TextField(null=True)

    @classmethod
    def from_json(cls, json, **kwargs):
        """Creates a booking chart from a JSON-ish dict."""
        bookables = json.pop('bookables', ())
        transaction = super().from_json(json, **kwargs)
        return transaction.chart.update_bookables(bookables, transaction)

    @property
    def bookables(self):
        """Yields bookable objects."""
        for bookable in self.bookables:
            yield bookable.bookable

    def update_bookables(self, bookables, transaction):
        """Updates the bookable objects."""
        if bookables is _UNCHANGED:
            return transaction

        if self.id is not None:
            for bookable in self.bookables:
                bookable.delete_instance()

        if not bookables:
            return transaction

        for bookable in (get_bookable(ident) for ident in bookables):
            bookable_mapping = BookableMapping(chart=self, bookable=bookable)
            transaction.add(bookable_mapping)

        return transaction

    def patch_json(self, json, **kwargs):
        """Patches the bookable chart."""
        bookables = json.pop('bookables', _UNCHANGED)
        transaction = super().patch_json(json, **kwargs)
        return transaction.chart.update_bookables(bookables, transaction)

    def to_json(self, mode=ChartMode.FULL, **kwargs):
        """Returns a JSON-ish dict."""
        json = super().to_json(mode=mode, **kwargs)

        if mode == ChartMode.FULL:
            json['bookables'] = [
                bookable.to_json() for bookable in self.bookables]

        return json

    def to_dom(self, brief=False):
        """Returns an XML DOM."""
        if brief:
            return super().to_dom(dom.BriefChart)

        xml = super().to_dom(dom.Booking)
        xml.bookable = [bookable.id for bookable in self.bookables]
        return xml


class BookableMapping(DSCMS4Model):
    """Many-to-many mapping of bookables and charts."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'chart_booking_bookable_mapping'

    chart = ForeignKeyField(
        Booking, column_name='chart', backref='bookables', on_delete='CASCADE')
    bookable = ForeignKeyField(
        Bookable, column_name='bookable', on_delete='CASCADE')
