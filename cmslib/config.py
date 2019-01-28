"""DSCMS4 configuration."""

from logging import getLogger

from configlib import loadcfg


__all__ = ['CONFIG', 'LOG_FORMAT', 'LOGGER']


CONFIG = loadcfg('cmslib.conf')
LOG_FORMAT = '[%(levelname)s] %(name)s: %(message)s'
LOGGER = getLogger('cmslib')
