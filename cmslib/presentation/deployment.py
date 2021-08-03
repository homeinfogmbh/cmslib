"""Content accumulation for digital signage deployment."""

from typing import Iterator, Union

from peewee import ModelSelect

from hwdb import Deployment
from mdb import Address

from cmslib import dom  # pylint: disable=E0611
from cmslib.orm.charts import BaseChart
from cmslib.orm.configuration import Configuration
from cmslib.orm.content.deployment import DeploymentBaseChart
from cmslib.orm.content.deployment import DeploymentConfiguration
from cmslib.orm.content.deployment import DeploymentMenu
from cmslib.orm.group import Group, GroupMemberDeployment
from cmslib.orm.menu import Menu
from cmslib.presentation.common import IndexedBaseChart, Presentation


__all__ = ['Presentation']


def address_to_dom(address: Address) -> dom.Address:
    """Returns an XML DOM binding for the address."""

    address_dom = dom.Address()
    address_dom.street = address.street
    address_dom.house_number = address.house_number
    address_dom.zip_code = address.zip_code
    address_dom.city = address.city
    return address_dom


def deployment_to_dom(deployment: Deployment) -> dom.Deployment:
    """Returns an XML DOM binding for the deployment."""

    deployment_dom = dom.Deployment()
    deployment_dom.address = address_to_dom(deployment.address)

    if deployment.lpt_address is not None:
        deployment_dom.lpt_address = address_to_dom(deployment.lpt_address)

    deployment_dom.id = deployment.id
    deployment_dom.customer = deployment.customer_id
    deployment_dom.type = deployment.type.value
    deployment_dom.connection = deployment.connection.value
    deployment_dom.testing = deployment.testing
    deployment_dom.scheduled = deployment.scheduled
    return deployment_dom


def get_deployment(deployment: Union[Deployment, int]) -> Deployment:
    """Returns a deep-joined deployment."""

    return Deployment.select(cascade=True).where(
        Deployment.id == deployment).get()


class Presentation(Presentation):   # pylint: disable=E0102
    """Accumulates content for a deployment."""

    def __init__(self, deployment: Deployment):     # pylint: disable=W0231
        """Sets the respective deployment."""
        self.deployment = get_deployment(deployment)

    @property
    def customer(self):
        """Returns the customer."""
        return self.deployment.customer

    def get_base_charts(self) -> Iterator[IndexedBaseChart]:
        """Selects charts directy attached to the deployment."""
        for base_chart in BaseChart.select(
                DeploymentBaseChart, cascade=True).join_from(
                BaseChart, DeploymentBaseChart).where(
                (DeploymentBaseChart.deployment == self.deployment)
                & (BaseChart.trashed == 0)):
            yield IndexedBaseChart(base_chart.deploymentbasechart.index,
                                   base_chart)

    def get_configurations(self) -> ModelSelect:
        """Selects directly attached configurations."""
        return Configuration.select(cascade=True).join_from(
            Configuration, DeploymentConfiguration).where(
            DeploymentConfiguration.deployment == self.deployment)

    def get_memberships(self) -> ModelSelect:
        """Selects groups this deployment is a member of."""
        return Group.select(cascade=True).join_from(
            Group, GroupMemberDeployment).where(
            GroupMemberDeployment.deployment == self.deployment)

    def get_menus(self) -> ModelSelect:
        """Selects menus of this deployment."""
        return Menu.select(cascade=True).join_from(Menu, DeploymentMenu).where(
            DeploymentMenu.deployment == self.deployment)

    def to_dom(self) -> dom.presentation:
        """Returns an XML DOM."""
        xml = super().to_dom()
        xml.deployment = deployment_to_dom(self.deployment)
        return xml

    def to_json(self) -> dict:
        """Returns a JSON-ish dict."""
        json = super().to_json()
        json['deployment'] = self.deployment.to_json(address=True)
        return json
