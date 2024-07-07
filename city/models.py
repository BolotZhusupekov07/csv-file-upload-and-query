from django.db import models

from csv_process.models import CSVFile


class City(models.Model):
    csv_file = models.ForeignKey(CSVFile, models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    population = models.IntegerField()
    established_at = models.DateTimeField()
