"""Charts related messages."""

from cmslib.messages.facility import DSCMS4_MESSAGE


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
    'CHART_TYPE_ADDED']


CHART_DATA_INCOMPLETE = DSCMS4_MESSAGE('Chart data is incomplete.', status=400)
CHART_DATA_INVALID = DSCMS4_MESSAGE('Chart data is invalid.', status=400)
NO_CHART_TYPE_SPECIFIED = DSCMS4_MESSAGE(
    'No chart type specified.', status=422)
INVALID_CHART_TYPE = DSCMS4_MESSAGE(
    'Invalid chart type specified.', status=406)
NO_CHART_ID_SPECIFIED = DSCMS4_MESSAGE('No chart ID specified.', status=422)
NO_SUCH_CHART = DSCMS4_MESSAGE(
    'The specified chart does not exist.', status=404)
NO_SUCH_BASE_CHART = DSCMS4_MESSAGE(
    'The specified base chart does not exist.', status=404)
CHART_ADDED = DSCMS4_MESSAGE('The chart has been added.', status=201)
CHART_DELETED = DSCMS4_MESSAGE('The chart has been deleted.', status=200)
CHART_PATCHED = DSCMS4_MESSAGE('The chart has been patched.', status=200)
CHART_TYPE_ADDED = DSCMS4_MESSAGE('The chart type has been added.', status=201)
