"""Common chart data."""

from enum import Enum
from typing import NamedTuple


__all__ = ['CHARTS']


CHARTS = {}


class CheckResult(NamedTuple):
    """Chart check result."""

    orphans: frozenset
    ambiguous: frozenset


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
