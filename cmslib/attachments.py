"""DOM utilities."""

from hisfs import File

from cmslib.dom import Attachment   # pylint: disable=E0401,E0611


__all__ = ['attachment_dom', 'attachment_json']


# pylint: disable=W0622
def attachment_dom(file_id, format=None, index=None):
    """Returns an attachment for the respective file ID."""

    if file_id is None:
        return None

    try:
        file = File[file_id]
    except File.DoesNotExist:
        return None

    xml = Attachment()
    xml.id = file.id
    xml.mimetype = file.metadata.mimetype
    xml.filename = file.name
    xml.sha256sum = file.metadata.sha256sum
    xml.size = file.metadata.size
    xml.format = format
    xml.index = index
    return xml


def attachment_json(file_id, json=None, format=None, index=None):
    """Returns a JSON-ish representation of the attachment."""

    if file_id is None:
        return json

    try:
        file = File[file_id]
    except File.DoesNotExist:
        return json

    file_data = file.to_json(skip={'file'})

    if json:
        file_data.update(json)

    if format is not None:
        file_data['format'] = format

    if index is not None:
        file_data['index'] = index

    return file_data
