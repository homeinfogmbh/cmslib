"""Group messages."""

from wsgilib import JSONMessage


__all__ = [
    'NO_SUCH_GROUP',
    'NO_SUCH_MEMBER_TYPE',
    'NO_SUCH_MEMBER',
    'GROUP_ADDED',
    'GROUP_PATCHED',
    'GROUP_DELETED',
    'MEMBER_ADDED',
    'MEMBER_DELETED']


NO_SUCH_GROUP = JSONMessage('The specified group does not exist.', status=404)
NO_SUCH_MEMBER_TYPE = JSONMessage(
    'The specified member type does not exist.', status=404)
NO_SUCH_MEMBER = JSONMessage(
    'The group does not contain the specified member.', status=404)
GROUP_ADDED = JSONMessage('The group has been added.', status=201)
GROUP_PATCHED = JSONMessage('The group has been patched.', status=200)
GROUP_DELETED = JSONMessage('The group has been deleted.', status=200)
MEMBER_ADDED = JSONMessage(
    'The specified member has been added to the group.', status=201)
MEMBER_DELETED = JSONMessage(
    'The specified member has been removed from the group.', status=200)
