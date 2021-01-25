"""Content accumulation for groups."""

from typing import Iterator

from cmslib import dom  # pylint: disable=E0611
from cmslib.orm.group import Group
from cmslib.presentation.common import Presentation


__all__ = ['Presentation']


class Presentation(Presentation):   # pylint: disable=E0102,W0223
    """Accumulates content for a group."""

    def __init__(self, group: Group):
        """Sets the respective group."""
        super().__init__(group.customer)
        self.group = group

    def get_memberships(self) -> Iterator[Group]:
        """Yields this group itself."""
        yield self.group

    def to_dom(self) -> dom.presentation:
        """Returns an XML DOM."""
        xml = super().to_dom()
        xml.group = self.group.id
        return xml

    def to_json(self) -> dict:
        """Returns a JSON-ish dict."""
        json = super().to_json()
        json['group'] = self.group.id
        return json
