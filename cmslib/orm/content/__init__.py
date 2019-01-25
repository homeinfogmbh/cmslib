"""Content mappings.

This package provides modules to map
content on so-called "clients".
"""
from cmslib.orm.content import comcat_account, group, terminal


__all__ = ['MODELS']


MODELS = comcat_account.MODELS, group.MODELS + terminal.MODELS
