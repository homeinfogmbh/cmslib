"""Content accumulation for digital signage deployment."""

from cmslib.exceptions import NoConfigurationFound
from cmslib.orm.charts import BaseChart
from cmslib.orm.configuration import Configuration
from cmslib.orm.content.deployment import DeploymentBaseChart
from cmslib.orm.content.deployment import DeploymentConfiguration
from cmslib.orm.content.deployment import DeploymentMenu
from cmslib.orm.group import GroupMemberDeployment
from cmslib.orm.menu import Menu
from cmslib.presentation.common import PresentationMixin


__all__ = ['Presentation']


class Presentation(PresentationMixin):
    """Accumulates content for a deployment."""

    def __init__(self, deployment):
        """Sets the respective deployment."""
        self.deployment = deployment
        self.cache = {}

    @property
    def customer(self):
        """Returns the respective customer."""
        return self.deployment.customer

    @property
    def base_charts(self):
        """Yields charts directy attached to the deployment."""
        return DeploymentBaseChart.select().join(BaseChart).where(
            (DeploymentBaseChart.deployment == self.deployment)
            & (BaseChart.trashed == 0)).order_by(DeploymentBaseChart.index)

    @property
    def configuration(self):
        """Returns the deployment's configuration."""
        try:
            return Configuration.select().join(DeploymentConfiguration).where(
                DeploymentConfiguration.deployment == self.deployment).get()
        except Configuration.DoesNotExist:
            raise NoConfigurationFound()

    @property
    def groups(self):
        """Yields groups this deployment is a member of."""
        for gms in GroupMemberDeployment.select().where(
                GroupMemberDeployment.deployment == self.deployment):
            yield gms.group

    @property
    def menus(self):
        """Yields menus of this deployment."""
        yield from Menu.select().join(DeploymentMenu).where(
            DeploymentMenu.deployment == self.deployment)

    def to_dom(self):
        """Returns an XML DOM."""
        xml = super().to_dom()
        xml.deployment = self.deployment.id
        return xml

    def to_json(self):
        """Returns a JSON-ish dict."""
        json = super().to_json()
        json['deployment'] = self.deployment.id
        return json
