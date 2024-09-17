from django.db import models


class Item(models.Model):
    DoesNotExist = None
    objects = None
    title = models.CharField(max_length=200)
    date = models.DateTimeField("test date")
    description = models.TextField(max_length=200)
