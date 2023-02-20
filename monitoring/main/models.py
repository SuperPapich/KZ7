from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    vote = models.IntegerField(null=True)
