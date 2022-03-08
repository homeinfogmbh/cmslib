"""Chart type settings for the respective customers."""

from typing import Type

from peewee import CharField

from mdb import Customer

from cmslib.orm.common import CustomerModel
from cmslib.orm.charts.api.chart import Chart


__all__ = ['ChartACL', 'MODELS']


class ChartACL(CustomerModel):
    """Access control list for charts that customers are allowed to use."""

    class Meta:
        table_name = 'chart_acl'

    chart_type = CharField(255)

    @classmethod
    def can_use(cls, customer: Customer, chart_class: Type[Chart]) -> bool:
        """Determines whether the respective
        user may use the given chart class.
        """
        condition = cls.customer == customer
        condition &= cls.chart_type == chart_class.__name__

        try:
            cls.get(condition)
        except cls.DoesNotExist:
            return False

        return True


MODELS = (ChartACL,)
