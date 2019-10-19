from django.db import models
from django.utils import timezone


class Parent(models.Model):

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.created_at.isoformat()


class Child(models.Model):

    created_at = models.DateTimeField(default=timezone.now)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    def __str__(self):
        return self.created_at.isoformat()
