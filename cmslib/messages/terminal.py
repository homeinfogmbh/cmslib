"""Terminal related messages."""

from cmslib.messages.facility import DSCMS4_MESSAGE


__all__ = ['NO_SUCH_TERMINAL']


NO_SUCH_TERMINAL = DSCMS4_MESSAGE(
    'The specified terminal does not exist.', status=404)
