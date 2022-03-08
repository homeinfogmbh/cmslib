"""ORM model to represent groups."""

from __future__ import annotations

from peewee import ForeignKeyField, IntegerField, Select

from hwdb import Deployment
from mdb import Address, Company, Customer
from peeweeplus import HTMLCharField, HTMLTextField

from cmslib.orm.common import DSCMS4Model, TreeNode


__all__ = ['MODELS', 'Group', 'GroupMemberDeployment']


class Group(TreeNode):
    """Groups of 'clients' that can be assigned content."""

    name = HTMLCharField(255)
    description = HTMLTextField(null=True)
    parent = ForeignKeyField(
        'self', column_name='parent', null=True, backref='children',
        lazy_load=True
    )
    index = IntegerField(default=0)


class GroupMemberDeployment(DSCMS4Model):
    """Deployments as members in groups."""

    class Meta:
        table_name = 'group_member_deployment'

    group = ForeignKeyField(
        Group, column_name='group', on_delete='CASCADE', lazy_load=False
    )
    deployment = ForeignKeyField(
        Deployment, column_name='deployment', on_delete='CASCADE',
        lazy_load=False
    )
    index = IntegerField(default=0)

    @classmethod
    def from_json(
            cls, json: dict, group: Group, deployment: Deployment
    ) -> GroupMemberDeployment:
        """Creates a member for the given group
        from the respective JSON-ish dictionary.
        """
        record = super().from_json(json)
        record.group = group
        record.deployment = deployment
        return record

    @classmethod
    def select(cls, *args, cascade: bool = False) -> Select:
        """Selects records."""
        if not cascade:
            return super().select(*args)

        deployment_customer = Customer.alias()
        deployment_company = Company.alias()
        return super().select(
            cls, Group, Customer, Company, Deployment, deployment_customer,
            deployment_company, *args
        ).join_from(
            cls, Group).join(Customer).join(Company).join_from(
            cls, Deployment).join_from(Deployment, deployment_customer).join(
            deployment_company).join_from(
            Deployment, Address, on=Deployment.address == Address.id
        )

    def to_json(self) -> dict:
        """Returns a JSON-ish dict."""
        return {
            'id': self.id,
            'index': self.index,
            'group': self.group.id,
            'deployment': self.deployment.id
        }


MODELS = (Group, GroupMemberDeployment)
