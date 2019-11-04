"""Database transactions."""

from collections import deque


__all__ = ['Transaction']


class Transaction(deque):
    """Handles a list of records in-order for atomic transactions."""

    def get_instance_of(self, typ):
        """Returns the first chart."""
        for _, item in self:
            if isinstance(item, typ):
                return item

        return None

    def add(self, record, *, left=False):
        """Adds the record as to be added."""
        item = (True, record)

        if left:
            return self.appendleft(item)

        return self.append(item)

    def delete(self, record, *, left=False):
        """Adds the record as to be deleted."""
        item = (False, record)

        if left:
            return self.appendleft(item)

        return self.append(item)

    def commit(self):
        """Saves / deletes the respective records."""
        for save, record in self:
            if save:
                record.save()
            else:
                record.delete_instance()
