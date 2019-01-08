"""Terminal related messages."""

from cmslib.messages.common import DSCMS4Message


__all__ = ['NoSuchTerminal']


class NoSuchTerminal(DSCMS4Message):
    """Indicates that the respective terminal does not exist."""

    STATUS = 404
