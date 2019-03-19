"""Terminal related functions."""

from his import CUSTOMER
from terminallib import Terminal

from cmslib.messages.terminal import NO_SUCH_TERMINAL


__all__ = ['get_terminal', 'with_terminal']


def get_terminal(tid):
    """Returns the respective terminal."""

    try:
        return Terminal.get(
            (Terminal.tid == tid) & (Terminal.customer == CUSTOMER.id))
    except Terminal.DoesNotExist:
        raise NO_SUCH_TERMINAL


def with_terminal(function):
    """Converts a TID into a terminal."""

    def wrapper(tid, *args, **kwargs):
        """Wraps the function."""
        return function(get_terminal(tid), *args, **kwargs)

    return wrapper
