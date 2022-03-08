"""Chart for polls."""

from __future__ import annotations
from enum import Enum
from typing import Union

from peewee import ForeignKeyField, IntegerField, Select

from peeweeplus import EnumField, HTMLCharField, HTMLTextField, Transaction

from cmslib import dom
from cmslib.orm.charts.api import ChartMode, Chart
from cmslib.orm.common import UNCHANGED, DSCMS4Model


__all__ = ['Mode', 'Poll', 'Option']


DomModel = Union[dom.BriefChart, dom.Poll]


class Mode(Enum):
    """Available poll modes."""

    SINGLE_CHOICE = 'single choice'
    MULTIPLE_CHOICE = 'multiple choice'


class Poll(Chart):
    """Chart to display a poll."""

    class Meta:
        table_name = 'chart_poll'

    text = HTMLTextField()
    mode = EnumField(Mode)

    @classmethod
    def from_json(cls, json: dict, **kwargs) -> Transaction:
        """Creates a new poll from JSON."""
        options = json.pop('options', ())
        transaction = super().from_json(json, **kwargs)

        for option in options:
            transaction.add(Option.from_json(option, transaction.primary))

        return transaction

    @property
    def sorted_options(self) -> Select:
        """Returns sorted options."""
        return self.options.order_by(Option.index)

    def _patch_options(self, transaction: Transaction, json: dict) -> None:
        """Patches the respective poll options."""
        if json == UNCHANGED:
            return

        options = {option.text: option for option in self.sorted_options}
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

    def patch_json(self, json: dict, **kwargs) -> Transaction:
        """Patches the respective chart."""
        options = json.pop('options', UNCHANGED) or ()
        transaction = super().patch_json(json, **kwargs)
        self._patch_options(transaction, options)
        return transaction

    def to_json(self, mode: ChartMode = ChartMode.FULL, **kwargs) -> dict:
        """Returns the dictionary representation of this chart's fields."""
        json = super().to_json(mode=mode, **kwargs)

        if mode == ChartMode.FULL:
            json['options'] = [
                option.to_json(fk_fields=False, autofields=True)
                for option in self.sorted_options
            ]

        return json

    def to_dom(self, brief: bool = False) -> DomModel:
        """Returns an XML DOM of this chart."""
        if brief:
            return super().to_dom(dom.BriefChart)

        xml = super().to_dom(dom.Poll)
        xml.text = self.text
        xml.mode = self.mode.value
        xml.option = [option.to_dom() for option in self.sorted_options]
        return xml


class Option(DSCMS4Model):
    """An option for a poll."""

    class Meta:
        table_name = 'poll_option'

    poll = ForeignKeyField(
        Poll, column_name='poll', backref='options', on_delete='CASCADE',
        lazy_load=False
    )
    text = HTMLCharField(255)
    votes = IntegerField(default=0)
    index = IntegerField(default=0)

    @classmethod
    def from_json(cls, json: dict, poll: Poll, **kwargs) -> Option:
        """Creates the image from a JSON-ish dict."""
        record = super().from_json(json, **kwargs)
        record.poll = poll
        return record

    def vote(self, amount: int = 1) -> None:
        """Adds votes."""
        self.votes += amount
        self.save()

    def to_dom(self) -> dom.PollOption:
        """Returns an XML DOM of this model."""
        xml = dom.PollOption(self.text)
        xml.id = self.id
        xml.votes = self.votes
        return xml
