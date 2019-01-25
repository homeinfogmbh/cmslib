"""Content accumulation for terminals."""

from cmslib.exceptions import NoConfigurationFound
from cmslib.orm.charts import BaseChart
from cmslib.orm.configuration import Configuration
from cmslib.orm.content.terminal import TerminalBaseChart
from cmslib.orm.content.terminal import TerminalConfiguration
from cmslib.orm.content.terminal import TerminalMenu
from cmslib.orm.group import GroupMemberTerminal
from cmslib.orm.menu import Menu
from cmslib.presentation.common import PresentationMixin


__all__ = ['Presentation']


class Presentation(PresentationMixin):
    """Accumulates content for a terminal."""

    def __init__(self, terminal):
        """Sets the respective terminal."""
        self.terminal = terminal
        self.cache = {}

    @property
    def customer(self):
        """Returns the respective customer."""
        return self.terminal.customer

    @property
    def base_charts(self):
        """Yields charts directy attached to the terminal."""
        return TerminalBaseChart.select().join(BaseChart).where(
            (TerminalBaseChart.terminal == self.terminal)
            & (BaseChart.trashed == 0)).order_by(TerminalBaseChart.index)

    @property
    def configuration(self):
        """Returns the terminal's configuration."""
        try:
            return Configuration.select().join(TerminalConfiguration).where(
                TerminalConfiguration.terminal == self.terminal).get()
        except Configuration.DoesNotExist:
            raise NoConfigurationFound()

    @property
    def groups(self):
        """Yields groups this terminal is a member of."""
        for gmt in GroupMemberTerminal.select().where(
                GroupMemberTerminal.terminal == self.terminal):
            yield gmt.group

    @property
    def menus(self):
        """Yields menus of this terminal."""
        yield from Menu.select().join(TerminalMenu).where(
            TerminalMenu.terminal == self.terminal)
