"""Chart for polls."""

from enum import Enum

from peewee import ForeignKeyField, IntegerField

from peeweeplus import EnumField, HTMLCharField, HTMLTextField

from cmslib import dom
from cmslib.orm.charts.api import ChartMode, Chart
from cmslib.orm.common import UNCHANGED, DSCMS4Model


__all__ = ['Mode', 'Poll', 'Option']


class Mode(Enum):
    """Available poll modes."""

    SINGLE_CHOICE = 'single choice'
    MULTIPLE_CHOICE = 'multiple choice'


class Poll(Chart):
    """Chart to display a poll."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'chart_poll'

    text = HTMLTextField()
    mode = EnumField(Mode)

    @classmethod
    def from_json(cls, json, **kwargs):
        """Creates a new poll from JSON."""
        options = json.pop('options', ())
        transaction = super().from_json(json, **kwargs)

        for option in options:
            option = Option.from_json(option, transaction.primary)
            transaction.add(option)

        return transaction

    @property
    def options(self):
        """Returns sorted options."""
        return Option.select().where(Option.poll == self).order_by(
            Option.index)

    def _patch_options(self, transaction, json):
        """Patches the respective poll options."""
        if json == UNCHANGED:
            return

        options = {option.text: option for option in self.options}
        json_objects = {option.get('text'): option for option in json}
        processed = set()

        for text, option in options.items():
            processed.add(text)

            try:
                json_object = json_objects[text]
            except KeyError:
                transaction.delete(option)
            else:
                option.patch_json(json_object)
                transaction.add(option)

        for text, json_object in json_objects.items():
            if text not in processed:
                option = Option.from_json(json_object, self)
                transaction.add(option)

    def patch_json(self, json, **kwargs):
        """Patches the respective chart."""
        options = json.pop('options', UNCHANGED) or ()
        transaction = super().patch_json(json, **kwargs)
        self._patch_options(transaction, options)
        return transaction

    def to_json(self, mode=ChartMode.FULL, **kwargs):
        """Returns the dictionary representation of this chart's fields."""
        json = super().to_json(mode=mode, **kwargs)

        if mode == ChartMode.FULL:
            json['options'] = [
                option.to_json(fk_fields=False, autofields=True)
                for option in self.options.order_by(Option.index)]

        return json

    def to_dom(self, brief=False):
        """Returns an XML DOM of this chart."""
        if brief:
            return super().to_dom(dom.BriefChart)

        xml = super().to_dom(dom.Poll)
        xml.text = self.text
        xml.mode = self.mode.value
        xml.option = [option.to_dom() for option in self.options]
        return xml


class Option(DSCMS4Model):
    """An option for a poll."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'poll_option'

    poll = ForeignKeyField(
        Poll, column_name='poll', backref='options', on_delete='CASCADE')
    text = HTMLCharField(255)
    votes = IntegerField(default=0)
    index = IntegerField(default=0)

    @classmethod
    def from_json(cls, json, poll, **kwargs):
        """Creates the image from a JSON-ish dict."""
        record = super().from_json(json, **kwargs)
        record.poll = poll
        return record

    def vote(self, amount=1):
        """Adds votes."""
        self.votes += amount
        self.save()

    def to_dom(self):
        """Returns an XML DOM of this model."""
        xml = dom.PollOption(self.text)
        xml.id = self.id
        xml.votes = self.votes
        return xml
