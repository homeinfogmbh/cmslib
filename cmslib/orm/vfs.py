"""Virtual file system."""

from __future__ import annotations

from peewee import JOIN, ForeignKeyField, ModelSelect

from peeweeplus import HTMLCharField

from cmslib.orm.charts import BaseChart
from cmslib.orm.common import DSCMS4Model, TreeNode


__all__ = ['MODELS', 'DirectoryNotEmpty', 'Directory', 'ContentChart']


class DirectoryNotEmpty(Exception):
    """Indicates that the directory is not empty."""


class Directory(TreeNode):
    """File system directory."""

    name = HTMLCharField(255)
    parent = ForeignKeyField(
        'self', column_name='parent', null=True, backref='children',
        lazy_load=False)

    @classmethod
    def select(cls, *args, cascade: bool = False, **kwargs) -> ModelSelect:
        """Selects directories."""
        if not cascade:
            return super().select(*args, **kwargs)

        child = cls.alias()
        args = {cls, *args, child, ContentChart}
        return cls.select(*args, **kwargs).join(
            child, on=child.parent == cls.id,
            join_type=JOIN.LEFT_OUTER).join_from(
            cls, ContentChart, on=ContentChart.directory == cls.id,
            join_type=JOIN.LEFT_OUTER)

    @property
    def empty(self) -> bool:
        """Checks whether the director is empty."""
        cls = type(self)

        if cls.select().where(cls.parent == self):
            return False

        if ContentChart.select().where(ContentChart.directory == self):
            return False

        return True

    def add_base_chart(self, base_chart: BaseChart):
        """Adds a base chart to the directory."""
        try:
            return self.charts.get(ContentChart.base_chart == base_chart)
        except ContentChart.DoesNotExist:
            content_chart = ContentChart(directory=self, base_chart=base_chart)
            content_chart.save()
            return content_chart

    def remove_base_chart(self, base_chart: BaseChart):
        """Removes a base chart from the directory."""
        for content_chart in self.charts.where(
                ContentChart.base_chart == base_chart):
            content_chart.delete_instance()

    def delete_instance(self, *args, **kwargs) -> int:
        """Deletes the respective instance from the group hierarchy
        setting all child's parent reference to this groups parent.
        """
        if self.empty:
            return super().delete_instance(*args, **kwargs)

        raise DirectoryNotEmpty()


class ContentChart(DSCMS4Model):
    """Deployments as members in groups."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'content_chart'

    directory = ForeignKeyField(
        Directory, column_name='directory', backref='charts',
        on_delete='CASCADE', lazy_load=False)
    base_chart = ForeignKeyField(
        BaseChart, column_name='base_chart', on_delete='CASCADE',
        lazy_load=False)


MODELS = (Directory, ContentChart)
