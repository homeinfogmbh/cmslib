"""Booking chart."""

from peewee import BooleanField, ForeignKeyField, TextField

from bookings import get_bookable, Bookable

from cmslib import dom
from cmslib.orm.charts.api import Chart, ChartMode
from cmslib.orm.common import UNCHANGED, DSCMS4Model


__all__ = ['Booking', 'BookableMapping']


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
        transaction.primary.update_bookable_mappings(bookables, transaction)
        return transaction

    @property
    def bookables(self):
        """Yields the respective bookables."""
        for bookable_mapping in self.bookable_mappings:
            yield bookable_mapping.bookable

    def update_bookable_mappings(self, bookables, transaction):
        """Updates the bookable objects."""
        if bookables == UNCHANGED:
            return

        if self.id is not None:
            for bookable_mapping in self.bookable_mappings:
                transaction.delete(bookable_mapping)

        for ident in bookables or ():
            bookable = get_bookable(ident)
            bookable_mapping = BookableMapping(chart=self, bookable=bookable)
            transaction.add(bookable_mapping)

    def patch_json(self, json, **kwargs):
        """Patches the bookable chart."""
        bookables = json.pop('bookables', UNCHANGED)
        transaction = super().patch_json(json, **kwargs)
        self.update_bookable_mappings(bookables, transaction)
        return transaction

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
        xml.bookable = [bmap.bookable_id for bmap in self.bookable_mappings]
        xml.rentee = self.rentee
        xml.purpose = self.purpose
        xml.text = self.text
        return xml


class BookableMapping(DSCMS4Model):
    """Many-to-many mapping of bookables and charts."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'chart_booking_bookable_mapping'

    chart = ForeignKeyField(
        Booking, column_name='chart', backref='bookable_mappings',
        on_delete='CASCADE')
    bookable = ForeignKeyField(
        Bookable, column_name='bookable', on_delete='CASCADE')
