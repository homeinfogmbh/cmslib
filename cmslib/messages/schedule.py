"""Schedule related messages."""

from wsgilib import JSONMessage


__all__ = [
    'NO_SUCH_SCHEDULE',
    'SCHEDULE_ADDED',
    'SCHEDULE_PATCHED',
    'SCHEDULE_DELETED',
    'NO_BASE_CHART_SPECIFIED',
    'NO_SCHEDULE_SPECIFIED'
]


NO_SUCH_SCHEDULE = JSONMessage(
    'The specified schedule does not exist.', status=404)
SCHEDULE_ADDED = JSONMessage('The schedule has been added.', status=201)
SCHEDULE_PATCHED = JSONMessage('The schedule has been patched.', status=200)
SCHEDULE_DELETED = JSONMessage('The schedule has been deleted.', status=200)
NO_BASE_CHART_SPECIFIED = JSONMessage('No base chart specified.', status=400)
NO_SCHEDULE_SPECIFIED = JSONMessage('No schedule specified.', status=400)
