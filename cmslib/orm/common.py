"""Common ORM models."""

from __future__ import annotations
from logging import getLogger
from typing import Optional, Union

from flask import has_request_context
from peewee import JOIN, ForeignKeyField, ModelSelect

from his import CUSTOMER
from mdb import Address, Company, Customer
from peeweeplus import MySQLDatabaseProxy, JSONModel


__all__ = [
    'UNCHANGED',
    'DATABASE',
    'DSCMS4Model',
    'CustomerModel',
    'TreeNode'
]


DATABASE = MySQLDatabaseProxy('dscms4', 'cmslib.conf')
LOGGER = getLogger(__file__)
UNCHANGED = object()    # Sentinel object for unchanged JSON fields.


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
        Customer, column_name='customer', on_delete='CASCADE', lazy_load=False)

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

        args = {cls, Customer, Company, Address, *args}
        return super().select(*args, **kwargs).join(Customer).join(
            Company).join(Address, join_type=JOIN.LEFT_OUTER)


class TreeNode(CustomerModel):
    """Base class for customer-oriented tree structures."""

    @classmethod
    def from_json(
            cls,
            json: dict,
            customer: Union[Customer, int],
            parent: Optional[Union[TreeNode, int]] = None,
            **kwargs
    ) -> TreeNode:
        """Creates a group from a JSON-ish dictionary."""
        record = super().from_json(json, **kwargs)
        record.customer = customer
        record.set_parent(parent)
        return record

    def delete_instance(self, *args, **kwargs) -> int:
        """Deletes the respective instance from the group hierarchy
        setting all child's parent reference to this groups parent.
        """
        for child in self.children:
            child.parent = self.parent
            child.save()

        return super().delete_instance(*args, **kwargs)

    def set_parent(self, parent: Optional[Union[TreeNode, int]]) -> None:
        """Changes the parent reference of the group."""
        if parent is None:
            self.parent = None
            return

        if not isinstance(parent, cls := type(self)):
            parent = cls.select().where(
                (cls.id == parent) & (cls.customer == self.customer)
            ).get()

        self.parent = parent

    def patch_json(self, json: dict, **kwargs) -> None:
        """Creates a group from a JSON-ish dictionary."""
        try:
            parent = json.pop('parent')
        except KeyError:
            pass
        else:
            self.set_parent(parent)

        super().patch_json(json, **kwargs)

    def to_json(self, parent: bool = True, **kwargs) -> dict:
        """Converts the group to a JSON-ish dictionary."""
        json = super().to_json(**kwargs)

        if parent:
            if self.parent is None:
                json['parent'] = None
            else:
                json['parent'] = self.parent_id
        else:
            json.pop('parent', None)

        return json
