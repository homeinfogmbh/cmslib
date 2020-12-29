"""Common preview functions."""

from typing import Union

from his.messages.request import INVALID_CONTENT_TYPE
from previewlib import FileAccessToken
from wsgilib import ACCEPT, JSON, JSONMessage, XML

from cmslib.exceptions import AmbiguousConfigurationsError
from cmslib.exceptions import NoConfigurationFound
from cmslib.messages.presentation import NO_CONFIGURATION_ASSIGNED
from cmslib.messages.presentation import AMBIGUOUS_CONFIGURATIONS
from cmslib.presentation.common import PresentationMixin


__all__ = ['Response', 'make_response']


Response = Union[JSON, JSONMessage, XML]


def make_response(presentation: PresentationMixin) -> Response:
    """Creates a response for the respective presentation."""

    file_preview_token = FileAccessToken.token_for_presentation(presentation)

    if  'application/xml' in ACCEPT or '*/*' in ACCEPT:
        try:
            presentation = presentation.to_dom()
        except AmbiguousConfigurationsError:
            return AMBIGUOUS_CONFIGURATIONS
        except NoConfigurationFound:
            return NO_CONFIGURATION_ASSIGNED

        presentation.file_preview_token = file_preview_token.hex
        return XML(presentation)

    if 'application/json' in ACCEPT:
        json = presentation.to_json()
        json['filePreviewToken'] = file_preview_token.hex
        return JSON(json)

    return INVALID_CONTENT_TYPE
