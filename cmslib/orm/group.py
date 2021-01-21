"""ORM model to represent groups."""

from __future__ import annotations
from typing import Iterator, Union

from peewee import ForeignKeyField, IntegerField, ModelSelect

from hwdb import Deployment
from mdb import Address, Company, Customer
from peeweeplus import HTMLCharField, HTMLTextField

from cmslib.exceptions import CircularReference
from cmslib.functions.deployment import get_deployment
from cmslib.orm.common import DSCMS4Model, CustomerModel


__all__ = ['MODELS', 'Group', 'GroupMemberDeployment']


class Group(CustomerModel):
    """Groups of 'clients' that can be assigned content."""

    name = HTMLCharField(255)
    description = HTMLTextField(null=True)
    parent = ForeignKeyField(
        'self', column_name='parent', null=True, backref='children',
        lazy_load=True)
    index = IntegerField(default=0)

    @classmethod
    def from_json(cls, json: dict, **kwargs) -> Group:
        """Creates a group from a JSON-ish dictionary."""
        parent = json.pop('parent', None)
        record = super().from_json(json, **kwargs)
        record.set_parent(parent)
        return record

    @property
    def root(self) -> bool:
        """Determines whether this group is on the root level."""
        return self.parent is None

    @property
    def ordered_children(self) -> ModelSelect:
        """Yields the children in order."""
        if self.id is None:
            return ()

        return self._children.order_by(type(self).index)

    @property
    def tree(self) -> Iterator[Group]:
        """Recursively yields this group's
        children in a depth-first search.
        """
        yield self

        for child in self.ordered_children:
            yield from child.tree

    @property
    def parents(self) -> Iterator[Group]:
        """Yields all parents."""
        if self.parent is None:
            return

        yield self.parent
        yield from self.parent.parents

    @property
    def json_tree(self) -> dict:
        """Returns the tree for this group."""
        json = self.to_json(parent=False)
        json['children'] = [child.json_tree for child in self.ordered_children]
        return json

    def set_parent(self, parent: Union[Group, int, None]) -> None:
        """Changes the parent reference of the group."""
        if parent is None:
            self.parent = None
            return

        if not isinstance(parent, Group):
            cls = type(self)
            condition = (cls.id == parent) & (cls.customer == self.customer)
            parent = cls.select().where(condition).get()

        if parent in self.tree:
            raise CircularReference(parent)

        self.parent = parent

    def patch_json(self, json: dict, **kwargs) -> None:
        """Creates a group from a JSON-ish dictionary."""
        try:
            parent = json.pop('parent')
        except KeyError:
            pass
        else:
            self.set_parent(parent)

        super().patch_json(json, **kwargs)

    def to_json(self, parent: bool = True, **kwargs) -> dict:
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

    def delete_instance(self, *args, **kwargs) -> int:
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

    group = ForeignKeyField(
        Group, column_name='group', on_delete='CASCADE', lazy_load=False)
    deployment = ForeignKeyField(
        Deployment, column_name='deployment', on_delete='CASCADE',
        lazy_load=False)
    index = IntegerField(default=0)

    @classmethod
    def from_json(cls, json: dict, group: Group) -> GroupMemberDeployment:
        """Creates a member for the given group
        from the respective JSON-ish dictionary.
        """
        deployment = get_deployment(json.pop('deployment'))
        index = json.pop('index', 0)
        return cls(group=group, deployment=deployment, index=index)

    @classmethod
    def select(cls, *args, cascade: bool = False, **kwargs) -> ModelSelect:
        """Selects records."""
        if not cascade:
            return super().select(*args, **kwargs)

        deployment_customer = Customer.alias()
        deployment_company = Company.alias()
        args = {
            cls, Group, Customer, Company, Deployment, deployment_customer,
            deployment_company, *args}
        return super().select(*args, cascade=cascade, **kwargs).join_from(
            cls, Group).join(Customer).join(Company).join_from(
            cls, Deployment).join_from(Deployment, deployment_customer).join(
            deployment_company).join_from(
            Deployment, Address, on=Deployment.address == Address.id)

    def to_json(self) -> dict:
        """Returns a JSON-ish dict."""
        return {
            'id': self.id,
            'index': self.index,
            'group': self.group.id,
            'deployment': self.deployment.id
        }


MODELS = (Group, GroupMemberDeployment)
