from collections import defaultdict
from datetime import (
    date,
    datetime
)
from django.core.management.base import (
    BaseCommand,
    CommandError
)
from django.utils.timezone import localtime

from sandbox.customcommand.models import (
    AccessLog,
    Statistics
)


def valid_date(s: str) -> datetime:
    try:
        return datetime.strptime(s, '%Y-%m-%d').astimezone()
    except ValueError:
        raise CommandError('Not a valid date: %s' % s)


class Command(BaseCommand):
    help = 'Tally daily page views from access logs.'

    def add_arguments(self, parser):
        parser.add_argument('from_date', type=valid_date)

    def handle(self, *args, **options):
        from_date_localized = localtime(options['from_date'])

        access_logs_iter = AccessLog.objects\
            .filter(accessed_at__gte=from_date_localized)\
            .order_by('accessed_at')\
            .iterator()

        page_view_daily = defaultdict(int)
        for access_log in access_logs_iter:
            page_view_daily[str(access_log.accessed_date)] += 1

        for date in page_view_daily:
            self.stdout.write('%s=%d' % (date, page_view_daily[date]))
            Statistics.objects.create(date=date, page_view=page_view_daily[date])

        self.stdout.write('done')

"""
-- by SQL
-- timezone?
SELECT
    DATE_FORMAT(access_at, 'YYYY-MM-DD'),
    COUNT(*)
FROM
    access_logs
WHERE
    accessed_at >= :from_date
GROUP BY
    DATE_FORMAT(access_at, 'YYYY-MM-DD')
;
"""
