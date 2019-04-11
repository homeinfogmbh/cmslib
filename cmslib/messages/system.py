"""Terminal related messages."""

from wsgilib import JSONMessage


__all__ = ['NO_SUCH_SYSTEM']


NO_SUCH_SYSTEM = JSONMessage(
    'The specified system does not exist.', status=404)
