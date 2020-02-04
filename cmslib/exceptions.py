"""Common ORM model exceptions."""


__all__ = [
    'OrphanedBaseChart',
    'AmbiguousBaseChart',
    'AmbiguousConfigurationsError',
    'NoConfigurationFound'
]


class CMSLibError(Exception):
    """Base class for exceptions within the DSCMS4."""


class OrphanedBaseChart(CMSLibError):
    """Indicates that the respective base chart is orphaned."""

    def __init__(self, base_chart):
        """Sets the base chart."""
        super().__init__(base_chart)
        self.base_chart = base_chart

    def __str__(self):
        """Returns an appropriate message."""
        return f'Base chart {self.base_chart.id} is orphaned.'


class AmbiguityError(CMSLibError):
    """Indicates an error due to ambiguous information."""


class AmbiguousBaseChart(AmbiguityError):
    """Indicates that the respective base chart
    is referenced by more than one chart.
    """

    def __init__(self, base_chart, references):
        """Sets the respective base chart and referencing charts."""
        super().__init__(base_chart, references)
        self.base_chart = base_chart
        self.references = references

    def __str__(self):
        """Returns an appropriate message."""
        charts = ', '.join(str(chart) for chart in self.references)
        return f'Base chart #{self.base_chart.id} is ambiguous: {charts}.'


class AmbiguousConfigurationsError(AmbiguityError):
    """Indicates that ambiguous configurations are defined for an object."""

    def __init__(self, level, index):
        """Sets the level and its index."""
        super().__init__(level, index)
        self.level = level
        self.index = index


class NoConfigurationFound(CMSLibError):
    """Indicates that no configuration has been found."""
