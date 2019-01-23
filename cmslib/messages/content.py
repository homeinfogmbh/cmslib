"""Messages for content handlers."""

from cmslib.messages.facility import DSCMS4_MESSAGE


__all__ = [
    'NO_SUCH_CONTENT',
    'NO_TYPE_SPECIFIED',
    'INVALID_CONTENT_TYPE',
    'CONTENT_ADDED',
    'CONTENT_EXISTS',
    'CONTENT_PATCHED',
    'CONTENT_DELETED']


NO_SUCH_CONTENT = DSCMS4_MESSAGE('No such content.', status=404)
NO_TYPE_SPECIFIED = DSCMS4_MESSAGE('No type specified.', status=400)
INVALID_CONTENT_TYPE = DSCMS4_MESSAGE('Invalid content type.', status=400)
CONTENT_ADDED = DSCMS4_MESSAGE('Content added.', status=201)
CONTENT_EXISTS = DSCMS4_MESSAGE('Content already exists.', status=400)
CONTENT_PATCHED = DSCMS4_MESSAGE('Content patched.', status=200)
CONTENT_DELETED = DSCMS4_MESSAGE('Content deleted.', status=200)
