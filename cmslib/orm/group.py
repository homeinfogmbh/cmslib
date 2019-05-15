"""ORM model to represent groups."""

from peewee import CharField, ForeignKeyField, IntegerField, TextField

from his.messages.data import MISSING_KEY_ERROR, INVALID_KEYS
from terminallib import Deployment

from cmslib.functions.deployment import get_deployment
from cmslib.messages.data import CIRCULAR_REFERENCE
from cmslib.orm.common import DSCMS4Model, CustomerModel


__all__ = ['MODELS', 'Group', 'GroupMemberDeployment']


class Group(CustomerModel):
    """Groups of 'clients' that can be assigned content."""

    name = CharField(255)
    description = TextField(null=True)
    parent = ForeignKeyField(
        'self', column_name='parent', null=True, backref='children')
    index = IntegerField(default=0)

    @classmethod
    def from_json(cls, json, **kwargs):
        """Creates a group from a JSON-ish dictionary."""
        parent = json.pop('parent', None)
        record = super().from_json(json, **kwargs)
        record.set_parent(parent)
        return record

    @property
    def root(self):
        """Determines whether this group is on the root level."""
        return self.parent is None

    @property
    def childrens_children(self):
        """Recursively yields this group's
        children in a depth-first search.
        """
        for child in self.children:
            for childs_child in child.childrens_children:
                yield childs_child

    @property
    def json_tree(self):
        """Returns the tree for this group."""
        json = self.to_json(parent=False)
        json['children'] = [child.json_tree for child in self.children]
        return json

    def set_parent(self, parent):
        """Changes the parent reference of the group."""
        if parent is not None:
            parent = self.get_peer(parent)

            if parent == self or parent in self.childrens_children:
                raise CIRCULAR_REFERENCE

        self.parent = parent

    def patch_json(self, json, **kwargs):
        """Creates a group from a JSON-ish dictionary."""
        try:
            parent = json.pop('parent')
        except KeyError:
            pass
        else:
            self.set_parent(parent)

        super().patch_json(json, **kwargs)

    def to_json(self, parent=True, **kwargs):
        """Converts the group to a JSON-ish dictionary."""
        json = super().to_json(**kwargs)

        if parent:
            if self.parent is None:
                json['parent'] = None
            else:
                json['parent'] = self.parent.id
        else:
            json.pop('parent', None)

        return json

    def delete_instance(self, *args, **kwargs):
        """Deletes the respective instance from the group hierarchy
        setting all child's parent reference to this groups parent.
        """
        for child in self.children:
            child.set_parent(self.parent)
            child.save()

        return super().delete_instance(*args, **kwargs)


class GroupMemberDeployment(DSCMS4Model):
    """Deployments as members in groups."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'group_member_deployment'

    group = ForeignKeyField(Group, column_name='group', on_delete='CASCADE')
    deployment = ForeignKeyField(
        Deployment, column_name='deployment', on_delete='CASCADE')
    index = IntegerField(default=0)

    @classmethod
    def from_json(cls, json, group):
        """Creates a member for the given group
        from the respective JSON-ish dictionary.
        """
        try:
            deployment = json.pop('deployment')
        except KeyError:
            raise MISSING_KEY_ERROR.update(keys=['deployment'])

        deployment = get_deployment(deployment)
        index = json.pop('index', 0)

        if json:
            raise INVALID_KEYS.update(keys=tuple(json))

        return cls(group=group, deployment=deployment, index=index)

    def to_json(self):
        """Returns a JSON-ish dict."""
        return {
            'id': self.id,
            'index': self.index,
            'group': self.group.id,
            'deployment': self.deployment.id}


MODELS = (Group, GroupMemberDeployment)
