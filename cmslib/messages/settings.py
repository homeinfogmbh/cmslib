"""Charts related messages."""

from cmslib.messages.common import DSCMS4Message


__all__ = ['SettingsSaved']


class SettingsSaved(DSCMS4Message):
    """Indicates that the respective settings have been saved."""

    STATUS = 200
