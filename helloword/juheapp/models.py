from django.db import models

# Create your models here.
class User(models.Model):
    openid = models.CharField(max_length=64,unique=True)
    nickname = models.CharField(max_length=64)
    citys = models.TextField(default=[])
    stocks = models.TextField(default=[])
    constellations = models.TextField(default=[])
    cithabc = models.TextField(default=[])
