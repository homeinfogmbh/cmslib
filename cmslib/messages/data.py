"""DSCMS4 data related messages."""

from wsgilib import JSONMessage


__all__ = [
    'INVALID_ID',
    'NO_ID_SPECIFIED',
    'CIRCULAR_REFERENCE',
    'INVALID_REFERENCE'
]


INVALID_ID = JSONMessage('Invalid ID.', status=400)
NO_ID_SPECIFIED = JSONMessage('No ID specified.', status=400)
CIRCULAR_REFERENCE = JSONMessage('Circular reference detected.', status=406)
INVALID_REFERENCE = JSONMessage('Invalid reference.', status=400)
