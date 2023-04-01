
from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)


class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,unique=True)
    url=models.URLField()

class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    date=models.DateField()
class Country(models.Model):
    country_name=models.CharField(max_length=100,primary_key=True)
    country_code=models.IntegerField()
    country_fav_place=models.CharField(max_length=100)
class Capital(models.Model):
    Country_name=models.ForeignKey(Country,on_delete=models.CASCADE)
    capital_name=models.CharField(max_length=100)
    capital_code=models.IntegerField()





