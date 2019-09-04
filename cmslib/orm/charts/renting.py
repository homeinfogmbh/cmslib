"""Renting chart."""

from peewee import ForeignKeyField

from rentallib import get_rentable, Rentable

from cmslib import dom
from cmslib.orm.charts.common import Chart, ChartMode
from cmslib.orm.common import DSCMS4Model


__all__ = ['Renting', 'RentableMapping']


_UNCHANGED = object()


class Renting(Chart):
    """Chart for renting."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'chart_renting'

    @classmethod
    def from_json(cls, json, **kwargs):
        """Creates a renting chart from a JSON-ish dict."""
        rentables = json.pop('rentables', ())
        transaction = super().from_json(json, **kwargs)
        return transaction.chart.update_rentables(rentables, transaction)

    @property
    def rentables(self):
        """Yields rentables."""
        for rentable_mapping in self.rentable_map:
            yield rentable_mapping.rentable

    def update_rentables(self, rentables, transaction):
        """Updates the rentables."""
        if rentables is _UNCHANGED:
            return transaction

        if self.id is not None:
            for rentable in self.rentables:
                rentable.delete_instance()

        if not rentables:
            return transaction

        for rentable in (get_rentable(ident) for ident in rentables):
            rentable_mapping = RentableMapping(chart=self, rentable=rentable)
            transaction.add(rentable_mapping)

        return transaction

    def patch_json(self, json, **kwargs):
        """Patches the rentable chart."""
        rentables = json.pop('rentables', _UNCHANGED)
        transaction = super().patch_json(json, **kwargs)
        return transaction.chart.update_rentables(rentables, transaction)

    def to_json(self, mode=ChartMode.FULL, **kwargs):
        """Returns a JSON-ish dict."""
        json = super().to_json(mode=mode, **kwargs)

        if mode == ChartMode.FULL:
            json['rentables'] = [
                rentable.to_json() for rentable in self.rentables]

        return json

    def to_dom(self, brief=False):
        """Returns an XML DOM."""
        if brief:
            return super().to_dom(dom.BriefChart)

        xml = super().to_dom(dom.Renting)
        xml.rentable = [rentable.id for rentable in self.rentables]
        return xml


class RentableMapping(DSCMS4Model):
    """Many-to-many mapping of rentables and charts."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'chart_renting_rentable_mapping'

    chart = ForeignKeyField(
        Renting, column_name='chart', backref='rentable_map',
        on_delete='CASCADE')
    rentable = ForeignKeyField(
        Rentable, column_name='rentable', on_delete='CASCADE')
