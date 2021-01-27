"""Per-customer Settings regarding this CMS itself.
Not to be confused with "configuration".
"""
from __future__ import annotations

from peewee import BooleanField

from mdb import Customer

from cmslib.orm.common import CustomerModel


__all__ = ['Settings']


class Settings(CustomerModel):
    """Per-customer CMS settings.
    All fields should have default values.
    """

    testing = BooleanField(default=False)   # Show testing deployments.
    trashed = BooleanField(default=False)   # Select trashed charts.

    @classmethod
    def for_customer(cls, customer: Customer) -> Settings:
        """Returns an XML DOM of the model."""
        try:
            return cls.get(cls.customer == customer)
        except cls.DoesNotExist:
            return cls(customer=customer)


MODELS = (Settings,)
