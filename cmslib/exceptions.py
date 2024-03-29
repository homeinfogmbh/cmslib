"""Common ORM model exceptions."""

from peewee import Model


__all__ = [
    "AmbiguousBaseChart",
    "AmbiguousConfigurations",
    "CircularReference",
    "DifferentMenus",
    "InvalidChartType",
    "MissingMenu",
    "NoConfigurationFound",
    "OrphanedBaseChart",
]


class AmbiguousBaseChart(Exception):
    """Indicates that the respective base chart
    is referenced by more than one chart.
    """

    def __init__(self, base_chart: Model, *references: Model):
        references = frozenset(references)
        super().__init__(base_chart, references)
        self.base_chart = base_chart
        self.references = references

    def __str__(self):
        """Returns an appropriate message."""
        charts = ", ".join(str(chart) for chart in self.references)
        return f"Base chart #{self.base_chart.id} is ambiguous: {charts}."


class AmbiguousConfigurations(Exception):
    """Indicates that ambiguous configurations are defined for an object."""

    def __init__(self, level: int, index: int):
        super().__init__(level, index)
        self.level = level
        self.index = index


class CircularReference(Exception):
    """Indicates a circular reference within a tree structure."""

    def __init__(self, model: Model):
        super().__init__(model)
        self.model = model


class DifferentMenus(Exception):
    """Indicates that menu items belong to different menus."""

    def __init__(self, menu: Model, other: Model):
        super().__init__(menu, other)
        self.menu = menu
        self.other = other


class InvalidChartType(Exception):
    """Indicates that an invalid chart type was selected."""


class MissingMenu(Exception):
    """Indicates that a menu is missing for a menu item."""


class NoConfigurationFound(Exception):
    """Indicates that no configuration has been found."""


class OrphanedBaseChart(Exception):
    """Indicates that the respective base chart is orphaned."""

    def __init__(self, base_chart: Model):
        super().__init__(base_chart)
        self.base_chart = base_chart

    def __str__(self):
        """Returns an appropriate message."""
        return f"Base chart {self.base_chart.id} is orphaned."
