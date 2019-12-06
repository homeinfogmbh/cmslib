"""Configurations i.e. colors, tickers and brightness
settings for the digital signage presentation.
"""
from contextlib import suppress
from datetime import datetime
from enum import Enum

from peewee import BooleanField
from peewee import CharField
from peewee import ForeignKeyField
from peewee import IntegerField
from peewee import SmallIntegerField
from peewee import TextField
from peewee import TimeField

from peeweeplus import EnumField

from cmslib import dom
from cmslib.attachments import attachment_dom
from cmslib.orm.common import DSCMS4Model, CustomerModel
from cmslib.orm.transaction import Transaction


__all__ = [
    'TIME_FORMAT',
    'MODELS',
    'Colors',
    'Configuration',
    'Background',
    'Ticker',
    'Backlight'
]


TIME_FORMAT = '%H:%M'


def percentage(value):
    """Restricts a number to 0-100 %."""

    value = round(value)

    if 0 <= value <= 100:
        return value

    raise ValueError(f'Invalid percentage: {value}.')


class Font(Enum):
    """Available fonts."""

    VERDANA = 'verdana'
    ARIAL = 'arial'
    LATO = 'lato'
    SPARKASSE = 'sparkasse'
    NETTOO = 'nettoo'
    MUSEO = 'museo'
    SEGOE = 'segoe'


class Design(Enum):
    """Available designs."""

    THREE_D = '3d'
    NEWS = 'news'
    FLAT = 'flat'
    HD = 'hd'
    AIR = 'air'


class TickerTypes(Enum):
    """Valid ticker types."""

    TEXT = 'text'
    RSS = 'RSS'
    STOCK_PRICES = 'stock prices'


class Colors(DSCMS4Model):
    """Colors of a configuration."""

    header = IntegerField()
    header_background = IntegerField()
    background_left = IntegerField()
    background_right = IntegerField()
    ticker = IntegerField()
    ticker_background = IntegerField()
    clock = IntegerField()
    title = IntegerField()
    text = IntegerField()
    text_background = IntegerField()

    def to_dom(self):
        """Returns an XML DOM of the model."""
        xml = dom.Colors()
        xml.header = self.header
        xml.header_background = self.header_background
        xml.background_left = self.background_left
        xml.background_right = self.background_right
        xml.ticker = self.ticker
        xml.ticker_background = self.ticker_background
        xml.clock = self.clock
        xml.title = self.title
        xml.text = self.text
        xml.text_background = self.text_background
        return xml


class Configuration(CustomerModel):
    """Customer configuration for charts."""

    name = CharField(255)
    description = CharField(255, null=True)
    font = EnumField(Font)
    portrait = BooleanField(default=False)
    touch = BooleanField()
    design = EnumField(Design)
    effects = BooleanField()
    ticker_speed = SmallIntegerField()
    colors = ForeignKeyField(Colors, column_name='colors')
    title_size = SmallIntegerField()
    text_size = SmallIntegerField()
    logo = IntegerField(null=True)
    dummy_picture = IntegerField(null=True)
    hide_cursor = BooleanField(default=True)
    rotation = SmallIntegerField(default=0)
    email_form = BooleanField()
    volume = SmallIntegerField()
    text_bg_transparent = BooleanField(default=False)

    @classmethod
    def from_json(cls, json, **kwargs):
        """Creates a new configuration from the provided
        dictionary for the respective customer.
        """
        colors = json.pop('colors', None)
        backgrounds = json.pop('backgrounds', None)
        tickers = json.pop('tickers', ())
        backlight = json.pop('backlight', None)
        configuration = super().from_json(json, **kwargs)
        transaction = Transaction()
        transaction.add(configuration)
        configuration.update_colors(transaction, colors)
        configuration.update_backgrounds(
            transaction, backgrounds, delete=False)
        configuration.update_tickers(transaction, tickers, delete=False)
        configuration.update_backlights(transaction, backlight, delete=False)
        return transaction

    @property
    def files(self):
        """Returns a set od IDs of files used by the configuration."""
        files = set()

        if self.logo is not None:
            files.add(self.logo)

        for background in self.backgrounds:
            files.add(background.image)

        if self.dummy_picture is not None:
            files.add(self.dummy_picture)

        return files

    @property
    def backlight_dict(self):
        """Returns a backlight settings dictionary for this configuration."""
        backlights = {}

        for backlight in self.backlights:
            with suppress(ValueError):
                backlights.update(backlight.to_json())

        return backlights

    def update_colors(self, transaction, colors):
        """Updates the respective colors."""
        if colors:
            try:
                self.colors.patch_json(colors)
            except Colors.DoesNotExist:
                self.colors = Colors.from_json(colors)

            transaction.add(self.colors, left=True)

    def update_backgrounds(self, transaction, backgrounds, *, delete):
        """Updates the related backgrounds."""
        if delete:
            for background in self.backgrounds:
                transaction.delete(background)

        if backgrounds:
            for background in backgrounds:
                background = Background(configuration=self, image=background)
                transaction.add(background)

    def update_tickers(self, transaction, tickers, *, delete):
        """Updates the respective ticker records."""
        if delete:
            for ticker in self.tickers:
                transaction.delete(ticker)

        if tickers:
            for json in tickers:
                ticker = Ticker.from_json(json, self)
                transaction.add(ticker)

    def update_backlights(self, transaction, backlights, *, delete):
        """Updates the respective backlight records."""
        if delete:
            for backlight in self.backlights:
                transaction.delete(backlight)

        if backlights:
            for time, brightness in backlights.items():
                time = datetime.strptime(time, TIME_FORMAT).time()
                json = {'time': time, 'brightness': brightness}
                backlight = Backlight.from_json(json, self)
                transaction.add(backlight)

    def patch_json(self, json, **kwargs):
        """Patches the configuration with a JSON-ish dict."""
        transaction = Transaction()
        transaction.add(self)

        try:
            colors = json.pop('colors')
        except KeyError:
            pass
        else:
            self.update_colors(transaction, colors)

        try:
            backgrounds = json.pop('backgrounds')
        except KeyError:
            pass
        else:
            self.update_backgrounds(transaction, backgrounds, delete=True)

        try:
            tickers = json.pop('tickers')
        except KeyError:
            pass
        else:
            self.update_tickers(transaction, tickers, delete=True)

        backlight = json.pop('backlight', None)
        self.update_backlights(transaction, backlight, delete=True)
        super().patch_json(json, **kwargs)
        return transaction

    def to_json(self, cascade=False, **kwargs):
        """Converts the configuration into a JSON-like dictionary."""
        json = super().to_json(**kwargs)
        json['backgrounds'] = [
            background.image for background in self.backgrounds]

        if cascade:
            json['colors'] = self.colors.to_json(
                autofields=False, fk_fields=False)
            json['tickers'] = [
                ticker.to_json(autofields=False, fk_fields=False)
                for ticker in self.tickers]
            json['backlight'] = self.backlight_dict

        return json

    def to_dom(self):
        """Returns an XML DOM of the configuration."""
        xml = dom.Configuration()
        xml.name = self.name
        xml.description = self.description
        xml.font = self.font.value
        xml.portrait = self.portrait
        xml.touch = self.touch
        xml.design = self.design.value
        xml.effects = self.effects
        xml.ticker_speed = self.ticker_speed
        xml.colors = self.colors.to_dom()
        xml.title_size = self.title_size
        xml.text_size = self.text_size
        xml.logo = attachment_dom(self.logo)
        xml.dummy_picture = attachment_dom(self.dummy_picture)
        xml.hide_cursor = self.hide_cursor
        xml.rotation = self.rotation
        xml.email_form = self.email_form
        xml.volume = self.volume / 100
        xml.text_bg_transparent = self.text_bg_transparent
        xml.background = [
            attachment_dom(background.image)
            for background in self.backgrounds]
        xml.ticker = [ticker.to_dom() for ticker in self.tickers]
        xml.backlight = [backlight.to_dom() for backlight in self.backlights]
        return xml

    def delete_instance(self):
        """Deletes this instance."""
        colors = self.colors
        result = super().delete_instance()
        colors.delete_instance()
        return result


class Background(DSCMS4Model):
    """Background images for configurations."""

    configuration = ForeignKeyField(
        Configuration, column_name='configuration', backref='backgrounds',
        on_delete='CASCADE')
    image = IntegerField()


class Ticker(DSCMS4Model):
    """Ticker."""

    configuration = ForeignKeyField(
        Configuration, column_name='configuration', backref='tickers',
        on_delete='CASCADE')
    type_ = EnumField(TickerTypes, column_name='type')
    content = TextField()

    @classmethod
    def from_json(cls, json, configuration, **kwargs):
        """Creates a new ticker from the respective dictionary."""
        ticker = super().from_json(json, **kwargs)
        ticker.configuration = configuration
        return ticker

    def to_dom(self):
        """Returns an XML DOM of the model."""
        xml = dom.Ticker()
        xml.type = self.type_.value
        xml.content_ = self.content     # xml.content is reserved by PyXB.
        return xml


class Backlight(DSCMS4Model):
    """Backlight beightness settings of the respective configuration."""

    configuration = ForeignKeyField(
        Configuration, column_name='configuration', backref='backlights',
        on_delete='CASCADE')
    time = TimeField()
    brightness = SmallIntegerField()   # Brightness in percent.

    @classmethod
    def from_json(cls, json, configuration, **kwargs):
        """Yields new records from the provided JSON-ish dictionary."""
        backlight = super().from_json(json, **kwargs)
        backlight.configuration = configuration
        return backlight

    @property
    def percent(self):
        """Returns the percentage as an integer."""
        return percentage(self.brightness)

    @percent.setter
    def percent(self, brightness):
        """Sets the percentage."""
        self.brightness = percentage(brightness)

    def to_json(self):
        """Returns the backlight as dictionary."""
        return {self.time.strftime(TIME_FORMAT): self.percent}

    def to_dom(self):
        """Returns an XML DOM of the model."""
        xml = dom.Backlight()
        xml.time = self.time
        xml.brightness = self.brightness
        return xml


MODELS = (Colors, Configuration, Ticker, Backlight)
