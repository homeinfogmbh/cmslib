"""Charts related messages."""

from wsgilib import JSONMessage


__all__ = ['SETTINGS_SAVED']


SETTINGS_SAVED = JSONMessage('Settings saved.', status=200)
