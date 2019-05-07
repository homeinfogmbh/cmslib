"""Customer <> Chart mappings to allow
customers to use the respective charts.
"""

from peewee import CharField

from cmslib.orm.charts import Chart
from cmslib.orm.common import CustomerModel


__all__ = ['CustomerChart', 'MODELS']


MAX_LEN = max(len(name) for name in Chart.types.keys())


class CustomerChart(CustomerModel):
    """A customer <> Chart mapping."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'customer_chart'

    chart = CharField(MAX_LEN)

    @classmethod
    def can_use(cls, customer, chart):
        """Determines whether the customer can use the respective chart."""
        try:
            cls.get((cls.customer == customer) & (cls.chart == chart.__name__))
        except cls.DoesNotExist:
            return False

        return True


MODELS = (CustomerChart,)
