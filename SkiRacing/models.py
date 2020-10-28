from django.db import models

# Create your models here.


class Competition(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    date = models.DateField()
    country = models.CharField(max_length=50)
    distance = models.FloatField()
    type = models.CharField(max_length=50)
    other_info = models.TextField


class Racer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=40)
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=20)
    age = models.IntegerField()
    height = models.FloatField()
    weight = models.FloatField()


class Race(models.Model):
    id = models.IntegerField(primary_key=True)
    racer_id = models.ForeignKey(Racer, on_delete=models.CASCADE)
    competition_id = models.ForeignKey(Competition, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    total_time = models.DateTimeField()
    start_time = models.DateTimeField()


class Checkpoint(models.Model):
    id = models.IntegerField(primary_key=True)
    race_id = models.ForeignKey(Race, on_delete=models.CASCADE)
    distance = models.FloatField()
    time = models.DateTimeField()
    number = models.IntegerField()
