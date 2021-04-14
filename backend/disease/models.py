from django.db import models

# Create your models here.
class Treatment(models.Model):
    A = models.CharField(max_length=44)
    B = models.CharField(max_length=73)
    C = models.CharField(max_length=67)
    D = models.CharField(max_length=78)
    E = models.CharField(max_length=58)


class Meta:
    db.table = "sheet1"