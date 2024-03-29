"""Content assigned to deployments."""

from __future__ import annotations

from peewee import JOIN, ForeignKeyField, IntegerField, Select

from hwdb import Deployment
from mdb import Address, Company, Customer

from cmslib.orm.charts import BaseChart, Chart
from cmslib.orm.common import DSCMS4Model
from cmslib.orm.configuration import Configuration
from cmslib.orm.menu import Menu


__all__ = ["DeploymentBaseChart", "DeploymentConfiguration", "DeploymentMenu", "MODELS"]


class DeploymentContent(DSCMS4Model):
    """Common abstract content mapping."""

    deployment = ForeignKeyField(
        Deployment, column_name="deployment", on_delete="CASCADE", lazy_load=False
    )

    @classmethod
    def select(cls, *args, cascade: bool = False) -> Select:
        """Selects records."""
        if not cascade:
            return super().select(*args)

        deployment_address = Address.alias()
        lpt_address = Address.alias()
        return (
            super()
            .select(
                cls,
                Deployment,
                Customer,
                Company,
                Address,
                deployment_address,
                lpt_address,
                *args,
            )
            .join_from(cls, Deployment)
            .join(Customer)
            .join(Company)
            .join(Address, join_type=JOIN.LEFT_OUTER)
            .join_from(
                Deployment,
                deployment_address,
                on=Deployment.address == deployment_address.id,
            )
            .join_from(
                Deployment,
                lpt_address,
                on=Deployment.lpt_address == lpt_address.id,
                join_type=JOIN.LEFT_OUTER,
            )
        )


class DeploymentBaseChart(DeploymentContent):
    """Association of a base chart with a Deployment."""

    class Meta:
        table_name = "deployment_base_chart"

    base_chart = ForeignKeyField(
        BaseChart, column_name="base_chart", on_delete="CASCADE", lazy_load=False
    )
    index = IntegerField(default=0)

    @classmethod
    def from_json(
        cls, json: dict, deployment: Deployment, base_chart: BaseChart, **kwargs
    ) -> DeploymentBaseChart:
        """Creates a new group base chart."""
        record = super().from_json(json, **kwargs)
        record.deployment = deployment
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
        return (
            super()
            .select(
                cls,
                BaseChart,
                base_chart_customer,
                base_chart_company,
                base_chart_address,
                *args,
                cascade=True,
            )
            .join_from(cls, BaseChart)
            .join(base_chart_customer)
            .join(base_chart_company)
            .join(base_chart_address, join_type=JOIN.LEFT_OUTER)
        )

    @property
    def chart(self) -> Chart:
        """Returns the respective chart."""
        return self.base_chart.chart


class DeploymentConfiguration(DeploymentContent):
    """Association of a configuration with a Deployment."""

    class Meta:
        table_name = "deployment_configuration"

    configuration = ForeignKeyField(
        Configuration, column_name="configuration", on_delete="CASCADE", lazy_load=False
    )

    @classmethod
    def select(cls, *args, cascade: bool = False) -> Select:
        """Selects records."""
        if not cascade:
            return super().select(*args)

        configuration_customer = Customer.alias()
        configuration_company = Company.alias()
        configuration_address = Address.alias()
        return (
            super()
            .select(
                cls,
                Configuration,
                configuration_customer,
                configuration_company,
                configuration_address,
                *args,
                cascade=True,
            )
            .join_from(cls, Configuration)
            .join(configuration_customer)
            .join(configuration_company)
            .join(configuration_address, join_type=JOIN.LEFT_OUTER)
        )


class DeploymentMenu(DeploymentContent):
    """Association of a menu with a Deployment."""

    class Meta:
        table_name = "deployment_menu"

    menu = ForeignKeyField(
        Menu, column_name="menu", on_delete="CASCADE", lazy_load=False
    )

    @classmethod
    def select(cls, *args, cascade: bool = False) -> Select:
        """Selects records."""
        if not cascade:
            return super().select(*args)

        menu_customer = Customer.alias()
        menu_company = Company.alias()
        menu_address = Address.alias()
        return (
            super()
            .select(
                cls,
                Menu,
                menu_customer,
                menu_company,
                menu_address,
                *args,
                cascade=True,
            )
            .join_from(cls, Menu)
            .join(menu_customer)
            .join(menu_company)
            .join(menu_address, join_type=JOIN.LEFT_OUTER)
        )


MODELS = (DeploymentBaseChart, DeploymentConfiguration, DeploymentMenu)
