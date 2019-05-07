"""Object-relational mappings.

This package provides the CMS's database models.
"""
from sys import stderr

from cmslib.orm import charts
from cmslib.orm import content
from cmslib.orm import chart_types
from cmslib.orm import configuration
from cmslib.orm import group
from cmslib.orm import menu
from cmslib.orm import preview
from cmslib.orm import settings


__all__ = ['create_tables']


# Order matters here!
MODELS = (
    charts.MODELS + configuration.MODELS + group.MODELS + menu.MODELS
    + content.MODELS + chart_types.MODELS + preview.MODELS + settings.MODELS)


def create_tables(fail_silently=True):
    """Create the respective tables."""

    for model in MODELS:
        try:
            model.create_table(fail_silently=fail_silently)
        except Exception as error:  # pylint: disable=W0703
            print('Could not create table for model "{}":\n{}.'.format(
                model, error), file=stderr)
