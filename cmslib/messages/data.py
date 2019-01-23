"""DSCMS4 data related messages."""

from cmslib.messages.facility import DSCMS4_MESSAGE


__all__ = [
    'INVALID_ID',
    'NO_ID_SPECIFIED',
    'CIRCULAR_REFERENCE',
    'INVALID_REFERENCE']


INVALID_ID = DSCMS4_MESSAGE('Invalid ID.', status=400)
NO_ID_SPECIFIED = DSCMS4_MESSAGE('No ID specified.', status=400)
CIRCULAR_REFERENCE = DSCMS4_MESSAGE('Circular reference detected.', status=406)
INVALID_REFERENCE = DSCMS4_MESSAGE('Invalid reference.', status=400)
