from django.db import models
from django.utils import timezone


class AccessLog(models.Model):

    url = models.CharField(max_length=1000)
    ip_address = models.CharField(max_length=100)
    user_agent = models.CharField(max_length=400)
    referrer = models.CharField(max_length=1000)
    accessed_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.accessed_at.isoformat()

    @property
    def accessed_date(self):
        return self.accessed_at.date()


class Statistics(models.Model):

    date = models.DateField()
    page_view = models.IntegerField()
