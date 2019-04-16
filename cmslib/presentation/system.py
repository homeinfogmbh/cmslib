"""Content accumulation for digital signage systems."""

from cmslib.exceptions import NoConfigurationFound
from cmslib.orm.charts import BaseChart
from cmslib.orm.configuration import Configuration
from cmslib.orm.content.system import SystemBaseChart
from cmslib.orm.content.system import SystemConfiguration
from cmslib.orm.content.system import SystemMenu
from cmslib.orm.group import GroupMemberSystem
from cmslib.orm.menu import Menu
from cmslib.presentation.common import PresentationMixin


__all__ = ['Presentation']


class Presentation(PresentationMixin):
    """Accumulates content for a system."""

    def __init__(self, system):
        """Sets the respective system."""
        self.system = system
        self.cache = {}

    @property
    def customer(self):
        """Returns the respective customer."""
        return self.system.deployment.customer

    @property
    def base_charts(self):
        """Yields charts directy attached to the system."""
        return SystemBaseChart.select().join(BaseChart).where(
            (SystemBaseChart.system == self.system)
            & (BaseChart.trashed == 0)).order_by(SystemBaseChart.index)

    @property
    def configuration(self):
        """Returns the system's configuration."""
        try:
            return Configuration.select().join(SystemConfiguration).where(
                SystemConfiguration.system == self.system).get()
        except Configuration.DoesNotExist:
            raise NoConfigurationFound()

    @property
    def groups(self):
        """Yields groups this system is a member of."""
        for gms in GroupMemberSystem.select().where(
                GroupMemberSystem.system == self.system):
            yield gms.group

    @property
    def menus(self):
        """Yields menus of this system."""
        yield from Menu.select().join(SystemMenu).where(
            SystemMenu.system == self.system)

    def to_dom(self):
        """Returns an XML DOM."""
        xml = super().to_dom()
        xml.system = self.system.id
        return xml

    def to_json(self):
        """Returns a JSON-ish dict."""
        json = super().to_json()
        json['system'] = self.system.id
        return json
