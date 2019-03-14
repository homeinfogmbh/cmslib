"""Configuration related messages."""

from wsgilib import JSONMessage


__all__ = [
    'NO_SUCH_CONFIGURATION',
    'CONFIGURATION_ADDED',
    'CONFIGURATION_PATCHED',
    'CONFIGURATION_DELETED']


NO_SUCH_CONFIGURATION = JSONMessage('No such configuration.', status=404)
CONFIGURATION_ADDED = JSONMessage('Configuration has been added.', status=201)
CONFIGURATION_PATCHED = JSONMessage(
    'Configuration has been patched.', status=200)
CONFIGURATION_DELETED = JSONMessage(
    'Configuration has been deleted.', status=200)
