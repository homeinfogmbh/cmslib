"""Content accumulation for digital signage deployment."""

from typing import Iterable, Iterator, Union

from hwdb import Deployment
from mdb import Address, Customer, Company

from cmslib import dom  # pylint: disable=E0611
from cmslib.exceptions import NoConfigurationFound
from cmslib.orm.charts import BaseChart
from cmslib.orm.configuration import Configuration
from cmslib.orm.content.deployment import DeploymentBaseChart
from cmslib.orm.content.deployment import DeploymentConfiguration
from cmslib.orm.content.deployment import DeploymentMenu
from cmslib.orm.group import Group, GroupMemberDeployment
from cmslib.orm.menu import Menu
from cmslib.presentation.common import PresentationMixin


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

    return Deployment.select(Deployment, Customer, Company, Address).join(
        Customer).join(Company).join_from(
        Deployment, Address, on=Deployment.address == Address.id).where(
        Deployment.id == deployment).get()


class Presentation(PresentationMixin):
    """Accumulates content for a deployment."""

    def __init__(self, deployment: Deployment):
        """Sets the respective deployment."""
        self.deployment = get_deployment(deployment)
        self.cache = {}

    @property
    def customer(self) -> Customer:
        """Returns the respective customer."""
        return self.deployment.customer

    @property
    def base_charts(self) -> Iterable[DeploymentBaseChart]:
        """Yields charts directy attached to the deployment."""
        return DeploymentBaseChart.select().join(BaseChart).where(
            (DeploymentBaseChart.deployment == self.deployment)
            & (BaseChart.trashed == 0)).order_by(DeploymentBaseChart.index)

    @property
    def configuration(self) -> Configuration:
        """Returns the deployment's configuration."""
        try:
            return Configuration.select(cascade=True).join_from(
                Configuration, DeploymentConfiguration).where(
                DeploymentConfiguration.deployment == self.deployment).get()
        except Configuration.DoesNotExist:
            raise NoConfigurationFound() from None

    @property
    def groups(self) -> Iterator[Group]:
        """Yields groups this deployment is a member of."""
        for gms in GroupMemberDeployment.select().where(
                GroupMemberDeployment.deployment == self.deployment):
            yield gms.group

    @property
    def menus(self) -> Iterator[Menu]:
        """Yields menus of this deployment."""
        yield from Menu.select().join(DeploymentMenu).where(
            DeploymentMenu.deployment == self.deployment)

    def to_dom(self) -> dom.presentation:
        """Returns an XML DOM."""
        xml = super().to_dom()
        xml.customer = self.deployment.customer_id  # XXX: application hack.
        xml.deployment = deployment_to_dom(self.deployment)
        return xml

    def to_json(self) -> dict:
        """Returns a JSON-ish dict."""
        json = super().to_json()
        json['deployment'] = self.deployment.to_json(address=True)
        return json
