"""Charts related messages."""

from cmslib.messages.facility import DSCMS4_MESSAGE


__all__ = ['SETTINGS_SAVED']


SETTINGS_SAVED = DSCMS4_MESSAGE('Settings saved.', status=200)
