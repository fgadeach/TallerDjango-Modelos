from django.db import models

# Create your models here.
from measurements.models import Measurement

class Alarm(models.Model):
    measurement = models.ManyToManyField(Measurement)

    def __str__(self):
        return '{}'.format(self.measurement)

