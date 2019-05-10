"""Deployment related messages."""

from wsgilib import JSONMessage


__all__ = ['NO_SUCH_DEPLOYMENT']


NO_SUCH_DEPLOYMENT = JSONMessage(
    'The specified deployment does not exist.', status=404)
