"""Common chart data."""

from enum import Enum
from collections import namedtuple
from logging import getLogger


__all__ = ['CHARTS', 'LOGGER']


CHARTS = {}
LOGGER = getLogger(__file__)


CheckResult = namedtuple('CheckResult', ('orphans', 'ambiguous'))


class Transitions(Enum):
    """Effects available for chart transition effects."""

    FADE_IN = 'fade-in'
    MOSAIK = 'mosaik'
    SLIDE_IN = 'slide-in'
    RANDOM = 'random'


class ChartMode(Enum):
    """JSON serialization modes."""

    FULL = 'full'
    BRIEF = 'brief'
    ANON = 'anon'
