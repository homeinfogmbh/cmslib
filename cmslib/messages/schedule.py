"""Schedule related messages."""

from wsgilib import JSONMessage


__all__ = [
    'NO_SUCH_SCHEDULE',
    'SCHEDULE_ADDED',
    'SCHEDULE_PATCHED',
    'SCHEDULE_DELETED'
]


NO_SUCH_SCHEDULE = JSONMessage(
    'The specified schedule does not exist.', status=404)
SCHEDULE_ADDED = JSONMessage('The schedule has been added.', status=201)
SCHEDULE_PATCHED = JSONMessage('The schedule has been patched.', status=200)
SCHEDULE_DELETED = JSONMessage('The schedule has been deleted.', status=200)
