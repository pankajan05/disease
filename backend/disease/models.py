from django.db import models


# Create your models here.
class Treatment(models.Model):
    A = models.IntegerField(primary_key=True)
    B = models.CharField(max_length=44)
    C = models.CharField(max_length=73)
    D = models.CharField(max_length=67)
    E = models.CharField(max_length=78)
    F = models.CharField(max_length=58,default='')

    class Meta:
        db_table = "sheet1"


class Prediction(models.Model):
    name = models.CharField(max_length=100, default='')
    symptom1 = models.CharField(max_length=100, default='')
    symptom2 = models.CharField(max_length=100, default='')
    symptom3 = models.CharField(max_length=100, default='')
    prediction = models.CharField(max_length=100, default='')

    class Meta:
        db_table = "prediction"
