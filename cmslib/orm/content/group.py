"""Content assigned to groups."""

from __future__ import annotations

from peewee import JOIN, ForeignKeyField, IntegerField, Select

from mdb import Address, Company, Customer

from cmslib.orm.charts import BaseChart, Chart
from cmslib.orm.common import DSCMS4Model
from cmslib.orm.configuration import Configuration
from cmslib.orm.group import Group
from cmslib.orm.menu import Menu


__all__ = [
    'GroupBaseChart',
    'GroupConfiguration',
    'GroupMenu',
    'MODELS'
]


class _GroupContent(DSCMS4Model):
    """Common abstract content mapping."""

    group = ForeignKeyField(Group, column_name='group', on_delete='CASCADE')

    @classmethod
    def select(cls, *args, cascade: bool = False) -> Select:
        """Selects records."""
        if not cascade:
            return super().select(*args)

        return super().select(*{
            cls, Group, Customer, Company, Address, *args
        }).join_from(
            cls, Group).join(Customer).join(Company).join(
            Address, join_type=JOIN.LEFT_OUTER
        )


class GroupBaseChart(_GroupContent):
    """Association of a base chart with a group."""

    class Meta:
        table_name = 'group_base_chart'

    base_chart = ForeignKeyField(
        BaseChart, column_name='base_chart', on_delete='CASCADE'
    )
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
    def select(cls, *args, cascade: bool = False) -> Select:
        """Selects records."""
        if not cascade:
            return super().select(*args)

        base_chart_customer = Customer.alias()
        base_chart_company = Company.alias()
        base_chart_address = Address.alias()
        return super().select(*{
            cls, BaseChart, base_chart_customer, base_chart_company,
            base_chart_address, *args
        }).join_from(
            cls, BaseChart).join(
            base_chart_customer).join(
            base_chart_company).join(
            base_chart_address, join_type=JOIN.LEFT_OUTER
        )

    @property
    def chart(self) -> Chart:
        """Returns the respective chart."""
        return self.base_chart.chart


class GroupConfiguration(_GroupContent):
    """Association of a configuration with a group."""

    class Meta:
        table_name = 'group_configuration'

    configuration = ForeignKeyField(
        Configuration, column_name='configuration', on_delete='CASCADE'
    )

    @classmethod
    def select(cls, *args, cascade: bool = False) -> Select:
        """Selects records."""
        if not cascade:
            return super().select(*args)

        configuration_customer = Customer.alias()
        configuration_company = Company.alias()
        configuration_address = Address.alias()
        return super().select(*{
            cls, Configuration, configuration_customer, configuration_company,
            configuration_address, *args
        }).join_from(
            cls, Configuration).join(
            configuration_customer).join(
            configuration_company).join(
            configuration_address, join_type=JOIN.LEFT_OUTER
        )


class GroupMenu(_GroupContent):
    """Association of a menu with a group."""

    class Meta:
        table_name = 'group_menu'

    menu = ForeignKeyField(Menu, column_name='menu', on_delete='CASCADE')

    @classmethod
    def select(cls, *args, cascade: bool = False) -> Select:
        """Selects records."""
        if not cascade:
            return super().select(*args)

        menu_customer = Customer.alias()
        menu_company = Company.alias()
        menu_address = Address.alias()
        return super().select(*{
            cls, Menu, menu_customer, menu_company, menu_address, *args
        }).join_from(
            cls, Menu).join(
            menu_customer).join(
            menu_company).join(
            menu_address, join_type=JOIN.LEFT_OUTER
        )


MODELS = (GroupBaseChart, GroupConfiguration, GroupMenu)
