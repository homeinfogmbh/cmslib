"""DOM utilities."""

from hisfs import File

from cmslib.dom import Attachment   # pylint: disable=E0401,E0611


__all__ = ['attachment_dom', 'attachment_json']


# pylint: disable=W0622
def attachment_dom(file: File, format: str = None,
                   index: int = None) -> Attachment:
    """Returns an attachment for the respective file ID."""

    if file is None:
        return None

    metadata = file.metadata
    xml = Attachment()
    xml.id = file.id
    xml.mimetype = metadata.mimetype
    xml.filename = file.name
    xml.sha256sum = metadata.sha256sum
    xml.size = metadata.size
    xml.format = format
    xml.index = index
    return xml


def attachment_json(file: File, json: dict = None) -> dict:
    """Returns a JSON-ish representation of the attachment."""

    if file is None:
        return json

    result = file.to_json(fk_fields=False)

    if json:
        result.update(json)

    return result
