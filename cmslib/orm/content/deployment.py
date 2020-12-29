"""Content assigned to deployments."""

from __future__ import annotations

from peewee import ForeignKeyField, IntegerField

from hwdb import Deployment

from cmslib.orm.charts import BaseChart, Chart, ChartMode
from cmslib.orm.common import DSCMS4Model
from cmslib.orm.configuration import Configuration
from cmslib.orm.menu import Menu


__all__ = [
    'DeploymentBaseChart',
    'DeploymentConfiguration',
    'DeploymentMenu',
    'MODELS']


class DeploymentContent(DSCMS4Model):
    """Common abstract content mapping."""

    deplyoment = ForeignKeyField(
        Deployment, column_name='deployment', on_delete='CASCADE')


class DeploymentBaseChart(DeploymentContent):
    """Association of a base chart with a Deployment."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'deployment_base_chart'

    base_chart = ForeignKeyField(
        BaseChart, column_name='base_chart', on_delete='CASCADE')
    index = IntegerField(default=0)

    @classmethod
    def from_json(cls, json: dict, deployment: Deployment,
                  base_chart: BaseChart, **kwargs) -> DeploymentBaseChart:
        """Creates a new group base chart."""
        record = super().from_json(json, **kwargs)
        record.deployment = deployment
        record.base_chart = base_chart
        return record

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


class DeploymentConfiguration(DeploymentContent):
    """Association of a configuration with a Deployment."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'deployment_configuration'

    configuration = ForeignKeyField(
        Configuration, column_name='configuration', on_delete='CASCADE')

    def to_json(self) -> dict:
        """Returns a JSON-ish dict."""
        return {'id': self.id, 'configuration': self.configuration_id}


class DeploymentMenu(DeploymentContent):
    """Association of a menu with a Deployment."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'deployment_menu'

    menu = ForeignKeyField(Menu, column_name='menu', on_delete='CASCADE')

    def to_json(self) -> dict:
        """Returns a JSON-ish dict."""
        return {'id': self.id, 'menu': self.menu_id}


MODELS = (DeploymentBaseChart, DeploymentConfiguration, DeploymentMenu)
