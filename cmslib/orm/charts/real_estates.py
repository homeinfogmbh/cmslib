"""Real estate chart ORM."""

from __future__ import annotations
from collections import defaultdict
from enum import Enum
from itertools import chain
from typing import Iterable, Iterator, Type, Union

from peewee import BooleanField
from peewee import ForeignKeyField
from peewee import IntegerField
from peewee import Model
from peewee import Select
from peewee import SmallIntegerField

from hisfs import get_file, File
from openimmodb import Immobilie
from peeweeplus import EnumField, HTMLCharField, Transaction

from cmslib import dom
from cmslib.attachments import attachment_dom, attachment_json
from cmslib.orm.charts.api import ChartMode, Chart
from cmslib.orm.common import UNCHANGED, Attachment, DSCMS4Model


__all__ = ["RealEstates", "IdFilter", "ZipCodeFilter"]


DomModel = Union[dom.BriefChart, dom.RealEstates]


def _update_json_transaction(
    model: Type[Model],
    json_list: list[dict],
    transaction: Transaction,
    delete: list[Model] = None,
) -> None:
    """Adds models for the given JSON data to a transaction."""

    if delete:
        for record in delete:
            transaction.delete(record)

    if not json_list:
        return

    for json in json_list:
        record = model.from_json(json, transaction.primary)
        transaction.add(record)


class DisplayFormat(Enum):
    """Display formats."""

    BIG_PICTURE = "big picture"
    THREE = "three"
    FIFTY_FIFTY = "fifty-fifty"


class IdTypes(Enum):
    """Real estate ID types."""

    INTERN = "objektnr_intern"
    EXTERN = "objektnr_extern"
    OPENIMMO = "openimmo_obid"


class RealEstates(Chart):
    """Chart for real estate displaying."""

    class Meta:
        table_name = "chart_real_estates"

    display_format = EnumField(DisplayFormat, default=DisplayFormat.BIG_PICTURE)
    ken_burns = BooleanField(default=False)
    scaling = BooleanField(default=False)
    slideshow = BooleanField(default=True)
    qr_codes = BooleanField(default=False)
    show_contact = BooleanField(default=True)
    contact_picture = BooleanField(default=True)
    font_size = SmallIntegerField(default=8)
    font_color = IntegerField(default=0x000000)
    # Further colors:
    data = IntegerField(default=0x000000)
    background_data = IntegerField(default=0x000000)
    values = IntegerField(default=0x000000)
    background_values = IntegerField(default=0x000000)
    amenities_background_even = IntegerField(default=0x000000)
    amenities_text_even = IntegerField(default=0x000000)
    amenities_background_uneven = IntegerField(default=0x000000)
    amenities_text_uneven = IntegerField(default=0x000000)
    # Data field selections:
    amenities = BooleanField(default=True)
    construction = BooleanField(default=True)
    courtage = BooleanField(default=True)
    floor = BooleanField(default=True)
    area = BooleanField(default=True)
    free_from = BooleanField(default=True)
    coop_share = BooleanField(default=True)
    total_area = BooleanField(default=True)
    plot_area = BooleanField(default=True)
    cold_rent = BooleanField(default=True)
    purchase_price = BooleanField(default=True)
    security_deposit = BooleanField(default=True)
    service_charge = BooleanField(default=True)
    object_id = BooleanField(default=True)
    description = BooleanField(default=True)
    warm_rent = BooleanField(default=True)
    rooms = BooleanField(default=True)
    # Amenities tags:
    lift = BooleanField(default=True)
    bathtub = BooleanField(default=True)
    balcony = BooleanField(default=True)
    accessibility = BooleanField(default=True)
    assited_living = BooleanField(default=True)
    carport = BooleanField(default=True)
    floorboards = BooleanField(default=True)
    duplex = BooleanField(default=True)
    shower = BooleanField(default=True)
    builtin_kitchen = BooleanField(default=True)
    screed = BooleanField(default=True)  # Estrich.
    tiles = BooleanField(default=True)
    outdoor_parking = BooleanField(default=True)
    garage = BooleanField(default=True)
    cable_sat_tv = BooleanField(default=True)
    fireplace = BooleanField(default=True)
    basement = BooleanField(default=True)
    plastic = BooleanField(default=True)
    furnished = BooleanField(default=True)
    parquet = BooleanField(default=True)
    car_park = BooleanField(default=True)
    wheelchair_accessible = BooleanField(default=True)
    sauna = BooleanField(default=True)
    stone = BooleanField(default=True)
    swimming_pool = BooleanField(default=True)
    carpet = BooleanField(default=True)
    underground_carpark = BooleanField(default=True)
    lavatory = BooleanField(default=True)
    # Rooms selector:
    rooms_1 = BooleanField(default=True)
    rooms_2 = BooleanField(default=True)
    rooms_3 = BooleanField(default=True)
    rooms_4 = BooleanField(default=True)
    rooms_5 = BooleanField(default=True)
    rooms_5_or_more = BooleanField(default=True)
    # Real estate type:
    finance_project = BooleanField(default=True)
    business_realty = BooleanField(default=True)
    short_term_accommodation = BooleanField(default=True)
    living_realty = BooleanField(default=True)
    # Subtypes:
    office = BooleanField(default=True)
    retail = BooleanField(default=True)
    recreational = BooleanField(default=True)
    hospitality_industry = BooleanField(default=True)
    plot = BooleanField(default=True)
    hall_warehouse_production = BooleanField(default=True)
    house = BooleanField(default=True)
    agriculture_forestry = BooleanField(default=True)
    miscellaneous = BooleanField(default=True)
    flat = BooleanField(default=True)
    room = BooleanField(default=True)
    income_property = BooleanField(default=True)
    # Sale type:
    emphyteusis = BooleanField(default=True)  # Erbpacht.
    leasing = BooleanField(default=True)
    rent = BooleanField(default=True)
    sale = BooleanField(default=True)

    @classmethod
    def from_json(cls, json: dict, **kwargs) -> Transaction:
        """Creates a new chart from the respective dictionary."""
        filters = json.pop("filters", {})
        contacts = json.pop("contacts", ())
        transaction = super().from_json(json, **kwargs)
        _update_json_transaction(IdFilter, filters.get("id"), transaction)
        _update_json_transaction(ZipCodeFilter, filters.get("zipCode"), transaction)
        _update_json_transaction(Contact, contacts, transaction)
        return transaction

    @property
    def zip_code_whitelist(self) -> Iterable[ZipCodeFilter]:
        """Yields ZIP code whitelist filters."""
        return self.zip_code_filters.where(ZipCodeFilter.blacklist == 0)

    @property
    def zip_code_blacklist(self) -> Iterable[ZipCodeFilter]:
        """Yields ZIP code blacklist filters."""
        return self.zip_code_filters.where(ZipCodeFilter.blacklist == 1)

    @property
    def real_estates(self) -> Iterable[Immobilie]:
        """Yields filtered real estates for this chart."""
        return self.filter(
            Immobilie.select(cascade=True).where(Immobilie.customer == self.customer)
        )

    @property
    def filters_dictionary(self) -> dict[str, list[dict]]:
        """Dictionary of filters."""
        filters = defaultdict(list)
        skip = ("id", "chart")

        for fltr in self.id_filters:
            filters["id"].append(fltr.to_json(skip=skip))

        for fltr in self.zip_code_filters:
            filters["zipCode"].append(fltr.to_json(skip=skip))

        return filters

    @property
    def files(self) -> set[File]:
        """Returns the used files."""
        return {contact.file for contact in self.contacts}

    @classmethod
    def subqueries(cls) -> Iterator[Select]:
        """Yields sub-queries"""
        yield from super().subqueries()
        yield IdFilter.select()
        yield ZipCodeFilter.select()
        yield Contact.select(cascade=True, shallow=True)

    def patch_json(self, json: dict, **kwargs) -> Transaction:
        """Creates a new chart from the respective dictionary."""
        filters = json.pop("filters", {})
        contacts = json.pop("contacts", UNCHANGED)
        transaction = super().patch_json(json, **kwargs)

        try:
            id_filters = filters["id"]
        except KeyError:
            pass
        else:
            _update_json_transaction(
                IdFilter, id_filters, transaction, delete=self.id_filters
            )

        try:
            zip_code_filters = filters["zipCode"]
        except KeyError:
            pass
        else:
            _update_json_transaction(
                ZipCodeFilter,
                zip_code_filters,
                transaction,
                delete=self.zip_code_filters,
            )

        if contacts is not UNCHANGED:
            _update_json_transaction(
                Contact, contacts, transaction, delete=self.contacts
            )

        return transaction

    def match(self, real_estate: Immobilie) -> bool:
        """Matches the respective real estate
        against the configures filters.
        """
        # Discard blacklisted real estates.
        if any(fltr(real_estate) for fltr in self.zip_code_blacklist):
            return False

        zip_code_whitelist = set(self.zip_code_whitelist)

        if zip_code_whitelist:
            # Discard non-whitelisted real estates
            # iff ZIP code whitelist has entries.
            if not any(fltr(real_estate) for fltr in zip_code_whitelist):
                return False

        id_filters = set(self.id_filters)

        if id_filters:
            # Discard non-whitelisted real estates
            # iff ID whitelist has entries.
            if not any(fltr(real_estate) for fltr in id_filters):
                return False

        return True

    def filter(self, real_estates: Iterable[Immobilie]) -> Iterator[Immobilie]:
        """Yields filtered real estates."""
        return filter(self.match, real_estates)

    def to_json(self, mode: ChartMode = ChartMode.FULL, **kwargs) -> dict:
        """Returns a JSON-ish dictionary of the record's properties."""
        json = super().to_json(mode=mode, **kwargs)

        if mode == ChartMode.FULL:
            json["filters"] = self.filters_dictionary
            json["contacts"] = [
                contact.to_json(fk_fields=False, autofields=False)
                for contact in self.contacts
            ]

        return json

    def to_dom(self, brief: bool = False) -> DomModel:  # pylint: disable=R0915
        """Returns an XML DOM of this chart."""
        if brief:
            return super().to_dom(dom.BriefChart)

        xml = super().to_dom(dom.RealEstates)
        xml.display_format = self.display_format.value
        xml.ken_burns = self.ken_burns
        xml.scaling = self.scaling
        xml.slideshow = self.slideshow
        xml.qr_codes = self.qr_codes
        xml.show_contact = self.show_contact
        xml.contact_picture = self.contact_picture
        xml.font_size = self.font_size
        xml.font_color = self.font_color
        # Further colors:
        xml.data = self.data
        xml.background_data = self.background_data
        xml.values = self.values
        xml.background_values = self.background_values
        xml.amenities_background_even = self.amenities_background_even
        xml.amenities_text_even = self.amenities_text_even
        xml.amenities_background_uneven = self.amenities_background_uneven
        xml.amenities_text_uneven = self.amenities_text_uneven
        # Data field selections:
        xml.amenities = self.amenities
        xml.construction = self.construction
        xml.courtage = self.courtage
        xml.floor = self.floor
        xml.area = self.area
        xml.free_from = self.free_from
        xml.coop_share = self.coop_share
        xml.total_area = self.total_area
        xml.plot_area = self.plot_area
        xml.cold_rent = self.cold_rent
        xml.purchase_price = self.purchase_price
        xml.security_deposit = self.security_deposit
        xml.service_charge = self.service_charge
        xml.object_id = self.object_id
        xml.description = self.description
        xml.warm_rent = self.warm_rent
        xml.rooms = self.rooms
        # Amenities tags:
        xml.lift = self.lift
        xml.bathtub = self.bathtub
        xml.balcony = self.balcony
        xml.accessibility = self.accessibility
        xml.assited_living = self.assited_living
        xml.carport = self.carport
        xml.floorboards = self.floorboards
        xml.duplex = self.duplex
        xml.shower = self.shower
        xml.builtin_kitchen = self.builtin_kitchen
        xml.screed = self.screed
        xml.tiles = self.tiles
        xml.outdoor_parking = self.outdoor_parking
        xml.garage = self.garage
        xml.cable_sat_tv = self.cable_sat_tv
        xml.fireplace = self.fireplace
        xml.basement = self.basement
        xml.plastic = self.plastic
        xml.furnished = self.furnished
        xml.parquet = self.parquet
        xml.car_park = self.car_park
        xml.wheelchair_accessible = self.wheelchair_accessible
        xml.sauna = self.sauna
        xml.stone = self.stone
        xml.swimming_pool = self.swimming_pool
        xml.carpet = self.carpet
        xml.underground_carpark = self.underground_carpark
        xml.lavatory = self.lavatory
        # Rooms selector:
        xml.rooms_1 = self.rooms_1
        xml.rooms_2 = self.rooms_2
        xml.rooms_3 = self.rooms_3
        xml.rooms_4 = self.rooms_4
        xml.rooms_5 = self.rooms_5
        xml.rooms_5_or_more = self.rooms_5_or_more
        # Real estate type:
        xml.finance_project = self.finance_project
        xml.business_realty = self.business_realty
        xml.short_term_accommodation = self.short_term_accommodation
        xml.living_realty = self.living_realty
        # Subtypes:
        xml.office = self.office
        xml.retail = self.retail
        xml.recreational = self.recreational
        xml.hospitality_industry = self.hospitality_industry
        xml.plot = self.plot
        xml.hall_warehouse_production = self.hall_warehouse_production
        xml.house = self.house
        xml.agriculture_forestry = self.agriculture_forestry
        xml.miscellaneous = self.miscellaneous
        xml.flat = self.flat
        xml.room = self.room
        xml.income_property = self.income_property
        # Sale type:
        xml.emphyteusis = self.emphyteusis
        xml.leasing = self.leasing
        xml.rent = self.rent
        xml.sale = self.sale
        xml.filter = [
            filter.to_dom() for filter in chain(self.id_filters, self.zip_code_filters)
        ]
        xml.contact = [contact.to_dom() for contact in self.contacts]
        return xml


class IdFilter(DSCMS4Model):
    """Filter for the object IDs."""

    class Meta:
        table_name = "filter_id"

    chart = ForeignKeyField(
        RealEstates,
        column_name="chart",
        backref="id_filters",
        on_delete="CASCADE",
        lazy_load=False,
    )
    value = HTMLCharField(255)
    type = EnumField(IdTypes)

    def __call__(self, real_estate: Immobilie) -> bool:
        """Checks the filter against the respective real estate."""
        if self.type == IdTypes.INTERN:
            return self.value == real_estate.objektnr_intern

        if self.type == IdTypes.EXTERN:
            return self.value == real_estate.objektnr_extern

        if self.type == IdTypes.OPENIMMO:
            return self.value == real_estate.openimmo_obid

        raise ValueError("Unexpected ID type.")

    @classmethod
    def from_json(cls, json: dict, chart: RealEstates) -> IdFilter:
        """Creates a new entry from the
        dictionary for the respective chart.
        """
        record = super().from_json(json)
        record.chart = chart
        return record

    def to_dom(self) -> dom.IdFilter:
        """Returns an XML DOM of this model."""
        xml = dom.IdFilter()
        xml.value_ = self.value
        xml.type = self.type.value
        return xml


class ZipCodeFilter(DSCMS4Model):
    """Filter for real estate ZIP codes."""

    class Meta:
        table_name = "filter_zip_code"

    chart = ForeignKeyField(
        RealEstates,
        column_name="chart",
        backref="zip_code_filters",
        on_delete="CASCADE",
        lazy_load=False,
    )
    zip_code = HTMLCharField(255)
    # True: blacklist, False: whitelist.
    blacklist = BooleanField(default=False)

    def __call__(self, real_estate: Immobilie) -> bool:
        """Checks the filter against the respective real estate."""
        if self.blacklist:
            return real_estate.plz != self.zip_code

        return real_estate.plz == self.zip_code

    @classmethod
    def from_json(cls, json: dict, chart: RealEstates) -> ZipCodeFilter:
        """Creates a new record from the respective dictionary."""
        record = super().from_json(json)
        record.chart = chart
        return record

    @property
    def whitelist(self) -> bool:
        """Determines whether this is a whitelist record."""
        return not self.blacklist

    @whitelist.setter
    def whitelist(self, whitelist: bool):
        """Sets whether this is a whitelist record."""
        self.blacklist = not whitelist

    def to_dom(self) -> dom.ZipCodeFilter:
        """Returns an XML DOM of this model."""
        xml = dom.ZipCodeFilter()
        xml.zip_code = self.zip_code
        xml.blacklist = self.blacklist
        return xml


class Contact(Attachment):
    """Represents a real estate contact."""

    class Meta:
        table_name = "real_estate_contact"

    chart = ForeignKeyField(
        RealEstates,
        column_name="chart",
        backref="contacts",
        on_delete="CASCADE",
        lazy_load=False,
    )
    name = HTMLCharField(255)

    @classmethod
    def from_json(cls, json: dict, chart: RealEstates) -> Contact:
        """Creates a new record from the respective dictionary."""
        file = json.pop("file")
        record = super().from_json(json)
        record.chart = chart
        record.file = get_file(file)
        return record

    def to_json(self, *args, **kwargs) -> dict:
        """Returns a JSON representation of this record."""
        json = super().to_json(*args, **kwargs)
        return attachment_json(self.file, json=json)

    def to_dom(self) -> dom.RealEstateContact:
        """Returns an XML DOM of this record."""
        xml = dom.RealEstateContact()
        xml.name = self.name
        xml.image = attachment_dom(self.file)
        return xml
