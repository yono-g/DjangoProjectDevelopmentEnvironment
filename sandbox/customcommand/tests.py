import factory
import factory.fuzzy
from datetime import timedelta
from django.core.management import call_command
from django.utils import timezone
from django.test import TestCase
from io import StringIO

from sandbox.customcommand.models import (
    AccessLog
)


class AccessLogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AccessLog

    url = 'http://example.com/path/to/dummy'
    ip_address = '127.0.0.1'
    user_agent = 'dummy'
    referrer = 'http://example.com/path/to/dummy'
    accessed_at = factory.fuzzy.FuzzyDateTime(timezone.now() - timedelta(days=30))


class ExampleCommandTest(TestCase):

    def setUp(self):
        access_logs = AccessLogFactory.create_batch(100)

    def test_command(self):
        from_date = (timezone.now() - timedelta(days=30)).date().isoformat()
        out = StringIO()
        call_command('example', from_date, stdout=out)
        self.assertIn('done', out.getvalue())
