"""DOM utilities."""

from hisfs import File

from cmslib.dom import Attachment   # pylint: disable=E0401,E0611


__all__ = ['attachment_dom', 'attachment_json']


def attachment_dom(ident, format=None, index=None):     # pylint: disable=W0622
    """Returns an attachment for the respective file ID."""

    if ident is None:
        return None

    try:
        file = File[ident]
    except File.DoesNotExist:
        return None

    xml = Attachment()
    xml.id = file.id
    xml.mimetype = file.mimetype
    xml.filename = file.name
    xml.sha256sum = file.sha256sum
    xml.size = file.size
    xml.format = format
    xml.index = index
    return xml


def attachment_json(ident, json=None):
    """Returns a JSON-ish representation of the attachment."""

    if ident is None:
        return json

    try:
        file = File[ident]
    except File.DoesNotExist:
        return json

    file_data = {
        'id': file.id,
        'mimetype': file.mimetype,
        'filename': file.name,
        'sha256sum': file.sha256sum,
        'size': file.size,
        'format': file.format,
        'index': file.index,
    }

    file_data.update(json)
    return file_data
