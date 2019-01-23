"""Preview related messages."""

from cmslib.messages.facility import DSCMS4_MESSAGE


__all__ = ['UNAUTHORIZED', 'INVALID_TOKEN_TYPE', 'NO_SUCH_OBJECT']


UNAUTHORIZED = DSCMS4_MESSAGE('Preview not allowed.', status=401)
INVALID_TOKEN_TYPE = DSCMS4_MESSAGE('Invalid token type.', status=400)
NO_SUCH_OBJECT = DSCMS4_MESSAGE('No such preview object.', status=404)
