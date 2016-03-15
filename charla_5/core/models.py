from django.db import models

class Raspberry(models.Model):
    mac = models.CharField(max_length=20, unique=True)
    ip = models.GenericIPAddressField()
    hostname = models.CharField(max_length=20)

class Data(models.Model):
    name = models.CharField(max_length=20)
    value = models.FloatField()
    device = models.ForeignKey(Raspberry, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
