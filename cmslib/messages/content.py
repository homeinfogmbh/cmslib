"""Messages for content handlers."""

from wsgilib import JSONMessage


__all__ = [
    'NO_SUCH_CONTENT',
    'NO_TYPE_SPECIFIED',
    'INVALID_CONTENT_TYPE',
    'CONTENT_ADDED',
    'CONTENT_EXISTS',
    'CONTENT_PATCHED',
    'CONTENT_DELETED']


NO_SUCH_CONTENT = JSONMessage('No such content.', status=404)
NO_TYPE_SPECIFIED = JSONMessage('No type specified.', status=400)
INVALID_CONTENT_TYPE = JSONMessage('Invalid content type.', status=400)
CONTENT_ADDED = JSONMessage('Content added.', status=201)
CONTENT_EXISTS = JSONMessage('Content already exists.', status=400)
CONTENT_PATCHED = JSONMessage('Content patched.', status=200)
CONTENT_DELETED = JSONMessage('Content deleted.', status=200)
