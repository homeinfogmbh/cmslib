"""Presentation related messages."""

from cmslib.messages.facility import DSCMS4_MESSAGE


__all__ = ['AMBIGUOUS_CONFIGURATIONS', 'NO_CONFIGURATION_ASSIGNED']


AMBIGUOUS_CONFIGURATIONS = DSCMS4_MESSAGE(
    'Ambiguous assignment of configurations.', status=400)
NO_CONFIGURATION_ASSIGNED = DSCMS4_MESSAGE(
    'No configuration assigned.', status=400)
