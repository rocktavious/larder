import datetime

from django.db import models
from django.utils import timezone
from django_pint import fields as pint_fields
from .settings import UNITS

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    amount = pint_fields.QuantityField('cup', unit_choices=UNITS.keys())
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    def is_expired(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Ingredient, self).save(*args, **kwargs)

    def __str__(self):
        return "'{0}' of '{1}'".format(self.amount, self.name)