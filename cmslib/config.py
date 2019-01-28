"""DSCMS4 configuration."""

from logging import getLogger

from configlib import loadcfg


__all__ = ['CONFIG', 'LOGGER']


CONFIG = loadcfg('cmslib.conf')
LOGGER = getLogger('cmslib')
