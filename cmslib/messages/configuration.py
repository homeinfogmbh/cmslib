"""Configuration related messages."""

from cmslib.messages.facility import DSCMS4_MESSAGE


__all__ = [
    'NO_SUCH_CONFIGURATION',
    'CONFIGURATION_ADDED',
    'CONFIGURATION_PATCHED',
    'CONFIGURATION_DELETED']


NO_SUCH_CONFIGURATION = DSCMS4_MESSAGE('No such configuration.', status=404)
CONFIGURATION_ADDED = DSCMS4_MESSAGE(
    'Configuration has been added.', status=201)
CONFIGURATION_PATCHED = DSCMS4_MESSAGE(
    'Configuration has been patched.', status=200)
CONFIGURATION_DELETED = DSCMS4_MESSAGE(
    'Configuration has been deleted.', status=200)
