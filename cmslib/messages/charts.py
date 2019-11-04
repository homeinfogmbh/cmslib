"""Charts related messages."""

from wsgilib import JSONMessage


__all__ = [
    'CHART_DATA_INCOMPLETE',
    'CHART_DATA_INVALID',
    'NO_CHART_TYPE_SPECIFIED',
    'INVALID_CHART_TYPE',
    'NO_CHART_ID_SPECIFIED',
    'NO_SUCH_CHART',
    'NO_SUCH_BASE_CHART',
    'CHART_ADDED',
    'CHART_DELETED',
    'CHART_PATCHED',
    'CHART_TYPE_ADDED',
    'CHART_TYPE_DELETED',
    'NO_SUCH_CHART_TYPE'
]


CHART_DATA_INCOMPLETE = JSONMessage('Chart data is incomplete.', status=400)
CHART_DATA_INVALID = JSONMessage('Chart data is invalid.', status=400)
NO_CHART_TYPE_SPECIFIED = JSONMessage('No chart type specified.', status=422)
INVALID_CHART_TYPE = JSONMessage('Invalid chart type specified.', status=406)
NO_CHART_ID_SPECIFIED = JSONMessage('No chart ID specified.', status=422)
NO_SUCH_CHART = JSONMessage('The specified chart does not exist.', status=404)
NO_SUCH_BASE_CHART = JSONMessage(
    'The specified base chart does not exist.', status=404)
CHART_ADDED = JSONMessage('The chart has been added.', status=201)
CHART_DELETED = JSONMessage('The chart has been deleted.', status=200)
CHART_PATCHED = JSONMessage('The chart has been patched.', status=200)
CHART_TYPE_ADDED = JSONMessage('The chart type has been added.', status=201)
CHART_TYPE_DELETED = JSONMessage(
    'The chart type has been deleted.', status=200)
NO_SUCH_CHART_TYPE = JSONMessage(
    'The specified chart type does not exist.', status=404)
