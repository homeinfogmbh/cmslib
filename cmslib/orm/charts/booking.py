"""Booking chart."""

from typing import Iterable, Iterator, Union

from peewee import BooleanField, ForeignKeyField, Select

from bookings import get_bookable, Bookable
from peeweeplus import HTMLTextField, Transaction

from cmslib import dom
from cmslib.orm.charts.api import Chart, ChartMode
from cmslib.orm.common import UNCHANGED, DSCMS4Model


__all__ = ["Booking", "BookableMapping"]


DomModel = Union[dom.BriefChart, dom.Booking]


class Booking(Chart):
    """Chart for booking."""

    class Meta:
        table_name = "chart_booking"

    rentee = BooleanField(null=True)
    purpose = BooleanField(null=True)
    text = HTMLTextField(null=True)

    @classmethod
    def from_json(cls, json: dict, **kwargs) -> Transaction:
        """Creates a booking chart from a JSON-ish dict."""
        bookables = json.pop("bookables", ())
        transaction = super().from_json(json, **kwargs)
        transaction.primary.update_bookable_mappings(bookables, transaction)
        return transaction

    @classmethod
    def subqueries(cls) -> Iterator[Select]:
        """Yields sub-queries"""
        yield from super().subqueries()
        yield BookableMapping.select(cascade=True)

    def update_bookable_mappings(
        self, bookables: Iterable[int], transaction: Transaction
    ) -> None:
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

    def patch_json(self, json: dict, **kwargs) -> Transaction:
        """Patches the bookable chart."""
        bookables = json.pop("bookables", UNCHANGED)
        transaction = super().patch_json(json, **kwargs)
        self.update_bookable_mappings(bookables, transaction)
        return transaction

    def to_json(self, mode: ChartMode = ChartMode.FULL, **kwargs) -> dict:
        """Returns a JSON-ish dict."""
        json = super().to_json(mode=mode, **kwargs)

        if mode == ChartMode.FULL:
            json["bookables"] = [bmap.bookable_id for bmap in self.bookable_mappings]

        return json

    def to_dom(self, brief: bool = False) -> DomModel:
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

    class Meta:
        table_name = "chart_booking_bookable_mapping"

    chart = ForeignKeyField(
        Booking,
        column_name="chart",
        backref="bookable_mappings",
        on_delete="CASCADE",
        lazy_load=False,
    )
    bookable = ForeignKeyField(
        Bookable, column_name="bookable", on_delete="CASCADE", lazy_load=False
    )

    @classmethod
    def select(cls, *args, cascade: bool = False) -> Select:
        """Selects bookable mappings."""
        if not cascade:
            return super().select(*args)

        return super().select(cls, Bookable, *args).join(Bookable)
