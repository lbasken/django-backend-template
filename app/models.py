from django.db import models


class App(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField("test date")
    text = models.TextField(max_length=200)
