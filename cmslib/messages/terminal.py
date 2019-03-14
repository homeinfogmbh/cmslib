"""Terminal related messages."""

from wsgilib import JSONMessage


__all__ = ['NO_SUCH_TERMINAL']


NO_SUCH_TERMINAL = JSONMessage(
    'The specified terminal does not exist.', status=404)
