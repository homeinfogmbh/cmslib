"""DOM utilities."""

from hisfs import File

from cmslib.dom import Attachment   # pylint: disable=E0401,E0611


__all__ = ['attachment_dom']


def attachment_dom(ident, format=None, index=None, schedule=None):
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
    xml.format = format
    xml.index = index

    if schedule is not None:
        xml.schedule = schedule.to_dom()

    return xml
