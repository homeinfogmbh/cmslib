"""DOM utilities."""

from hisfs import File

from cmslib.dom import Attachment   # pylint: disable=E0401,E0611


__all__ = ['attachment_dom', 'attachment_json']


# pylint: disable=W0622
def attachment_dom(file, format=None, index=None):
    """Returns an attachment for the respective file ID."""

    if file is None:
        return None

    try:
        file = File[file]
    except File.DoesNotExist:
        return None

    xml = Attachment()
    xml.id = file
    xml.mimetype = file.mimetype
    xml.filename = file.name
    xml.sha256sum = file.sha256sum
    xml.size = file.size
    xml.format = format
    xml.index = index
    return xml


def attachment_json(file, json=None):
    """Returns a JSON-ish representation of the attachment."""

    if file is None:
        return json

    try:
        file = File[file]
    except File.DoesNotExist:
        return json

    file_data = {
        'mimetype': file.mimetype,
        'filename': file.name,
        'sha256sum': file.sha256sum,
        'size': file.size
    }

    file_data.update(json)
    return file_data
