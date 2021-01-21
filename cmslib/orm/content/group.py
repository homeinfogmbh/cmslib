"""Content assigned to groups."""

from __future__ import annotations

from peewee import ForeignKeyField, IntegerField, ModelSelect

from mdb import Address, Company, Customer

from cmslib.orm.charts import BaseChart, Chart, ChartMode
from cmslib.orm.common import DSCMS4Model
from cmslib.orm.configuration import Configuration
from cmslib.orm.group import Group
from cmslib.orm.menu import Menu


__all__ = [
    'GroupBaseChart',
    'GroupConfiguration',
    'GroupMenu',
    'MODELS']


class _GroupContent(DSCMS4Model):
    """Common abstract content mapping."""

    group = ForeignKeyField(Group, column_name='group', on_delete='CASCADE')

    @classmethod
    def select(cls, *args, cascade: bool = False, **kwargs) -> ModelSelect:
        """Selects records."""
        if not cascade:
            return super().select(*args, **kwargs)

        args = {cls, Group, Customer, Company, Address}
        return super().select(*args, **kwargs).join_from(
            cls, Group).join(Customer).join(Company).join(Address)


class GroupBaseChart(_GroupContent):
    """Association of a base chart with a group."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'group_base_chart'

    base_chart = ForeignKeyField(
        BaseChart, column_name='base_chart', on_delete='CASCADE')
    index = IntegerField(default=0)

    @classmethod
    def from_json(cls, json: dict, group: Group, base_chart: BaseChart,
                  **kwargs) -> GroupBaseChart:
        """Creates a new group base chart."""
        record = super().from_json(json, **kwargs)
        record.group = group
        record.base_chart = base_chart
        return record

    @classmethod
    def select(cls, *args, cascade: bool = False, **kwargs) -> ModelSelect:
        """Selects records."""
        if not cascade:
            return super().select(*args, **kwargs)

        base_chart_customer = Customer.alias()
        base_chart_company = Company.alias()
        base_chart_address = Address.alias()
        args = {
            cls, BaseChart, base_chart_customer, base_chart_company,
            base_chart_address
        }
        return super().select(*args, **kwargs).join_from(
            cls, BaseChart).join(base_chart_customer).join(
            base_chart_company).join(base_chart_address)

    @property
    def chart(self) -> Chart:
        """Returns the respective chart."""
        return self.base_chart.chart

    def to_json(self) -> dict:
        """Returns a JSON-ish dict."""
        return {
            'id': self.id,
            'chart': self.chart.to_json(mode=ChartMode.BRIEF),
            'index': self.index
        }


class GroupConfiguration(_GroupContent):
    """Association of a configuration with a group."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'group_configuration'

    configuration = ForeignKeyField(
        Configuration, column_name='configuration', on_delete='CASCADE')

    @classmethod
    def select(cls, *args, cascade: bool = False, **kwargs) -> ModelSelect:
        """Selects records."""
        if not cascade:
            return super().select(*args, **kwargs)

        configuration_customer = Customer.alias()
        configuration_company = Company.alias()
        configuration_address = Address.alias()
        args = {
            cls, Configuration, configuration_customer, configuration_company,
            configuration_address
        }
        return super().select(*args, **kwargs).join_from(
            cls, Configuration).join(configuration_customer).join(
            configuration_company).join(configuration_address)

    def to_json(self) -> dict:
        """Returns a JSON-ish dict."""
        return {'id': self.id, 'configuration': self.configuration_id}


class GroupMenu(_GroupContent):
    """Association of a menu with a group."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'group_menu'

    menu = ForeignKeyField(Menu, column_name='menu', on_delete='CASCADE')

    @classmethod
    def select(cls, *args, cascade: bool = False, **kwargs) -> ModelSelect:
        """Selects records."""
        if not cascade:
            return super().select(*args, **kwargs)

        menu_customer = Customer.alias()
        menu_company = Company.alias()
        menu_address = Address.alias()
        args = {cls, Menu, menu_customer, menu_company, menu_address}
        return super().select(*args, **kwargs).join_from(
            cls, Menu).join(menu_customer).join(menu_company).join(
            menu_address)

    def to_json(self) -> dict:
        """Returns a JSON-ish dict."""
        return {'id': self.id, 'menu': self.menu_id}


MODELS = (GroupBaseChart, GroupConfiguration, GroupMenu)
