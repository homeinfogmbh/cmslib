"""ORM-related functions."""

from cmslib.orm.group import GroupMemberDeployment


__all__ = ['deployment_groups']


def deployment_groups(deployment):
    """Yields all groups the given deployment is a member of."""

    condition = GroupMemberDeployment.deployment == deployment

    for gmd in GroupMemberDeployment.select().where(condition):
        yield gmd.group
        yield from gmd.group.parents
