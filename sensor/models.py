from django.db import models

class Sensor(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    installation_date = models.DateField()
    status = models.CharField(max_length=50)

class Data(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    pm25 = models.FloatField()
    pm10 = models.FloatField()
    co2 = models.FloatField()

class Alert(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    description = models.TextField()
