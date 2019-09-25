"""Common preview functions."""

from cmslib.exceptions import AmbiguousConfigurationsError
from cmslib.exceptions import NoConfigurationFound
from cmslib.messages.presentation import NO_CONFIGURATION_ASSIGNED
from cmslib.messages.presentation import AMBIGUOUS_CONFIGURATIONS
from his.messages.request import INVALID_CONTENT_TYPE
from previewlib import FileAccessToken

from wsgilib import ACCEPT, JSON, XML


__all__ = ['make_response']


def make_response(presentation):
    """Creates a response for the respective presentation."""

    headers = FileAccessToken.headers_for_presentation(presentation)

    if  'application/xml' in ACCEPT or '*/*' in ACCEPT:
        try:
            return XML(presentation.to_dom(), headers=headers)
        except AmbiguousConfigurationsError:
            return AMBIGUOUS_CONFIGURATIONS
        except NoConfigurationFound:
            return NO_CONFIGURATION_ASSIGNED

    if 'application/json' in ACCEPT:
        return JSON(presentation.to_json(), headers=headers)

    return INVALID_CONTENT_TYPE
