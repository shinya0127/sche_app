from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Sche(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    sche_date = models.DateTimeField(default=datetime.now)
    place = models.CharField(max_length=50, null=True, blank=True)
    repeatition = models.CharField(max_length=5, null=True, blank=True)
    notification = models.DateTimeField(null=True, blank=True)
    memo = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class Meta:
    ordering = ["sche_date"]