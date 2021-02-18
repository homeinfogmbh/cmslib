"""DOM utilities."""

from typing import Union

from filedb import File as FileDBFile
from hisfs import File

from cmslib.dom import Attachment   # pylint: disable=E0401,E0611


__all__ = ['attachment_dom', 'attachment_json']


def ensure_file(file: Union[File, int]) -> File:
    """Ensures a joined file."""

    if isinstance(file, File) and isinstance(file.file, FileDBFile):
        return file

    return File.select(File, FileDBFile).join(FileDBFile).where(
        File.id == file).get()


# pylint: disable=W0622
def attachment_dom(file: Union[File, int, None], format: str = None,
                   index: int = None) -> Attachment:
    """Returns an attachment for the respective file ID."""

    if file is None:
        return None

    file = ensure_file(file)
    xml = Attachment()
    xml.id = file.id
    xml.mimetype = file.mimetype
    xml.filename = file.name
    xml.sha256sum = file.sha256sum
    xml.size = file.size
    xml.format = format
    xml.index = index
    return xml


def attachment_json(file: File, json: dict = None) -> dict:
    """Returns a JSON-ish representation of the attachment."""

    if file is None:
        return json

    file = ensure_file(file)
    result = file.to_json()

    if json:
        result.update(json)

    return result
