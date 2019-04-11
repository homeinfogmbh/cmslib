"""Content assigned to Systems."""

from peewee import ForeignKeyField, IntegerField

from terminallib import System

from cmslib.orm.charts import ChartMode, BaseChart
from cmslib.orm.common import DSCMS4Model
from cmslib.orm.configuration import Configuration
from cmslib.orm.menu import Menu


__all__ = [
    'SystemBaseChart',
    'SystemConfiguration',
    'SystemMenu',
    'MODELS']


class _SystemContent(DSCMS4Model):
    """Common abstract content mapping."""

    system = ForeignKeyField(System, column_name='system', on_delete='CASCADE')


class SystemBaseChart(_SystemContent):
    """Association of a base chart with a System."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'system_base_chart'

    base_chart = ForeignKeyField(
        BaseChart, column_name='base_chart', on_delete='CASCADE')
    index = IntegerField(default=0)

    @classmethod
    def from_json(cls, json, System, base_chart, **kwargs):
        """Creates a new group base chart."""
        record = super().from_json(json, **kwargs)
        record.System = System
        record.base_chart = base_chart
        return record

    @property
    def chart(self):
        """Returns the respective chart."""
        return self.base_chart.chart

    def to_json(self):
        """Returns a JSON-ish dict."""
        return {
            'id': self.id,
            'chart': self.chart.to_json(mode=ChartMode.BRIEF),
            'index': self.index}


class SystemConfiguration(_SystemContent):
    """Association of a configuration with a System."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'system_configuration'

    configuration = ForeignKeyField(
        Configuration, column_name='configuration', on_delete='CASCADE')

    def to_json(self):
        """Returns a JSON-ish dict."""
        return {'id': self.id, 'configuration': self.configuration_id}


class SystemMenu(_SystemContent):
    """Association of a menu with a System."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'system_menu'

    menu = ForeignKeyField(Menu, column_name='menu', on_delete='CASCADE')

    def to_json(self):
        """Returns a JSON-ish dict."""
        return {'id': self.id, 'menu': self.menu_id}


MODELS = (SystemBaseChart, SystemConfiguration, SystemMenu)
