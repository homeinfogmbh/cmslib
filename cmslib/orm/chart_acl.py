"""Chart type settings for the respective customers."""

from peewee import CharField

from cmslib.orm.common import CustomerModel


__all__ = ['ChartACL', 'MODELS']


class ChartACL(CustomerModel):
    """Access control list for charts that customers are allowed to use."""

    chart_type = CharField(255)

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


MODELS = (ChartACL,)
