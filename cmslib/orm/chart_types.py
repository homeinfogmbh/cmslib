"""Chart type settings for the respective customers."""

from peewee import CharField

from cmslib.orm.charts import CHARTS
from cmslib.orm.common import CustomerModel


__all__ = ['ChartType', 'MODELS']


class ChartType(CustomerModel):
    """Represents a chart type this customer can use."""

    chart_type = CharField(255)

    @property
    def chart_class(self):
        """Returns the respective chart type's class."""
        return CHARTS[self.chart_type]

    @chart_class.setter
    def chart_class(self, chart_class):
        """Sets the respective chart type by its class."""
        for name, cls in CHARTS.items():
            if cls == chart_class:
                self.chart_type = name
                break

    @classmethod
    def can_use(cls, customer, chart_class):
        """Determines whether the respective
        user may use the given chart class.
        """
        try:
            cls.get(
                (cls.customer == customer)
                & (cls.chart_type == chart_class.__name__))
        except cls.DoesNotExist:
            return False

        return True


MODELS = (ChartType,)
