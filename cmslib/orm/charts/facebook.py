"""Facebook charts and associated data."""

from datetime import datetime, timedelta

from peewee import BooleanField
from peewee import CharField
from peewee import ForeignKeyField
from peewee import IntegerField
from peewee import SmallIntegerField

from ferengi.facebook import FACEBOOK

from cmslib import dom
from cmslib.orm.charts.common import ChartMode, Chart
from cmslib.orm.common import UNCHANGED, DSCMS4Model


__all__ = ['Facebook', 'Account']


class Facebook(Chart):
    """Facebook data chart."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'chart_facebook'

    font_size_title = SmallIntegerField(default=26)
    title_color = IntegerField(default=0x000000)
    font_size_text = SmallIntegerField(default=26)
    text_color = IntegerField(default=0x000000)
    ken_burns = BooleanField(default=False)

    @classmethod
    def from_json(cls, json, **kwargs):
        """Creates a new quotes chart from the
        dictionary for the respective customer.
        """
        accounts = json.pop('accounts', ())
        transaction = super().from_json(json, **kwargs)

        for account in accounts:
            account = Account.from_json(account, transaction.chart)
            transaction.add(account)

        return transaction

    def patch_json(self, json, **kwargs):
        """Creates a new quotes chart from the
        dictionary for the respective customer.
        """
        try:
            accounts = json.pop('accounts')
        except KeyError:
            accounts = UNCHANGED

        transaction = super().patch_json(json, **kwargs)

        if accounts is not UNCHANGED:
            for account in self.accounts:
                transaction.delete(account)

            for account in accounts:
                account = Account.from_json(account, transaction.chart)
                transaction.add(account)

        return transaction

    def to_json(self, mode=ChartMode.FULL, **kwargs):
        """Returns a JSON-ish dictionary."""
        json = super().to_json(mode=mode, **kwargs)

        if mode == ChartMode.FULL:
            json['accounts'] = [
                account.to_json(skip=('chart', 'id'))
                for account in self.accounts]

        return json

    def to_dom(self, brief=False):
        """Returns an XML DOM of this chart."""
        if brief:
            return super().to_dom(dom.BriefChart)

        xml = super().to_dom(dom.Facebook)
        xml.font_size_title = self.font_size_title
        xml.title_color = self.title_color
        xml.font_size_text = self.font_size_text
        xml.text_color = self.text_color
        xml.ken_burns = self.ken_burns
        xml.account = [account.to_dom() for account in self.accounts]
        return xml


class Account(DSCMS4Model):
    """Facebook account settings."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'facebook_account'

    chart = ForeignKeyField(
        Facebook, column_name='chart', backref='accounts', on_delete='CASCADE')
    facebook_id = CharField(255)
    recent_days = SmallIntegerField(default=14)
    max_posts = SmallIntegerField(default=10)
    name = CharField(255, null=True)

    @classmethod
    def from_json(cls, json, chart, **kwargs):
        """Creates a new facebook account for the provided
        facebook chart from the respective distionary.
        """
        account = super().from_json(json, **kwargs)
        account.chart = chart
        return account

    @property
    def since(self):
        """Returns the datetime of the first post."""
        return datetime.now() - timedelta(days=self.recent_days)

    @property
    def posts(self):
        """Yields posts."""
        return FACEBOOK.get_posts(
            self.facebook_id, limit=self.max_posts, since=self.since)

    def to_dom(self):
        """Returns an XML DOM of this model."""
        xml = dom.FacebookAccount()
        xml.facebook_id = self.facebook_id
        xml.recent_days = self.recent_days
        xml.max_posts = self.max_posts
        xml.name = self.name
        return xml
