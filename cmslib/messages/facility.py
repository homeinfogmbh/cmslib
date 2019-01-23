"""DSCMS4 message facility."""

from his.messages.facility import HIS_MESSAGE_FACILITY


__all__ = ['DSCMS4_MESSAGE']


DSCMS4_MESSAGE_DOMAIN = HIS_MESSAGE_FACILITY.domain('cmslib')
DSCMS4_MESSAGE = DSCMS4_MESSAGE_DOMAIN.message
