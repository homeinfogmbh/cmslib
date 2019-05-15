"""Content mappings.

This package provides modules to map
content on so-called "clients".
"""
from cmslib.orm.content import deployment, group


__all__ = ['MODELS']


MODELS = deployment.MODELS + group.MODELS
