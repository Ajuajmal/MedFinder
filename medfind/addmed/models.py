from django.conf import settings
from django.db import models
from django.utils import timezone


class addmed(models.Model):
    store = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default="")
    name = models.CharField(max_length=200, default="")
    brand = models.CharField(max_length=200,default="")
    stock=models.IntegerField(default=0)
    updated_date = models.DateTimeField(default=timezone.now)
    exp_date = models.DateTimeField(blank=True, null=True,default=timezone.now)

    def cocpublish(self):
        self.exp_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
