"""Common ORM models."""

from __future__ import annotations
from typing import Union

from flask import has_request_context
from peewee import ForeignKeyField, Model, ModelSelect

from his import CUSTOMER
from mdb import Address, Company, Customer
from peeweeplus import MySQLDatabase, JSONModel

from cmslib.config import CONFIG, LOGGER
from cmslib.messages.data import INVALID_REFERENCE


__all__ = [
    'UNCHANGED',
    'DATABASE',
    'DSCMS4Model',
    'CustomerModel'
]


UNCHANGED = object()    # Sentinel object for unchanged JSON fields.
DATABASE = MySQLDatabase.from_config(CONFIG['db'])


class DSCMS4Model(JSONModel):
    """Base Model for the DSCMS4 database."""

    class Meta:     # pylint: disable=C0115,R0903
        database = DATABASE
        schema = database.database

    def __str__(self):
        """Returns the models's ID and class."""
        cls = type(self)
        return f'{self.id}@{cls.__name__}'


class CustomerModel(DSCMS4Model):
    """Entity that relates to a customer."""

    customer = ForeignKeyField(
        Customer, column_name='customer', lazy_load=False)

    def __str__(self):
        """Returns the models's ID and class."""
        cls = type(self)
        return f'{self.id}:{self.customer_id}@{cls.__name__}'

    @classmethod
    def from_json(cls, json: dict, *, customer: Customer = None,
                  **kwargs) -> CustomerModel:
        """Creates a new record from the provided
        JSON-ish dictionary for a customer.

        If a customer is not specified and a flask request
        context exists, the current HIS customer will be used.
        """
        if customer is not None:
            LOGGER.warning('Explicitely set customer to: %s.', customer)
        elif has_request_context():
            customer = CUSTOMER.id
        else:
            raise TypeError('No customer specified.')

        record = super().from_json(json, **kwargs)
        record.customer = customer
        return record

    @classmethod
    def select(cls, *args, cascade: bool = False, **kwargs) -> ModelSelect:
        """Selects records."""
        if not cascade:
            return super().select(*args, **kwargs)

        return super().select(
            *{cls, Customer, Company, Address, *args}, **kwargs).join(
            Customer).join(Company).join(Address)

    def get_peer(self, record_or_id: Union[Model, int]) -> Model:
        """Ensures that the provided record or ID is of the same
        model and for the same customer as this record itself.
        """
        if record_or_id is None:
            return None

        cls = type(self)

        if isinstance(record_or_id, cls):
            if record_or_id.customer == self.customer:
                return record_or_id

            raise INVALID_REFERENCE

        try:
            return cls.get(
                (cls.id == record_or_id) & (cls.customer == self.customer))
        except cls.DoesNotExist:
            raise INVALID_REFERENCE from None
