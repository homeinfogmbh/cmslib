"""Presentation related messages."""

from wsgilib import JSONMessage


__all__ = ['AMBIGUOUS_CONFIGURATIONS', 'NO_CONFIGURATION_ASSIGNED']


AMBIGUOUS_CONFIGURATIONS = JSONMessage(
    'Ambiguous assignment of configurations.', status=400)
NO_CONFIGURATION_ASSIGNED = JSONMessage(
    'No configuration assigned.', status=400)
