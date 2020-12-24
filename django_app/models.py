from django.db import models
from django.contrib.auth.models import User, AbstractUser

class User(AbstractUser):
    full_name = models.CharField(max_length=50, null=True)
    experience = models.CharField(max_length=50, null=True)
    age = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.username

class Trail(models.Model):
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=50, null=True)
    unique_id = models.IntegerField(null=True)
    directions = models.CharField(max_length=1000, null=True)
    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)
    description = models.CharField(max_length=2500, null=True)
    thumbnail = models.CharField(max_length=700, null=True)
    length = models.CharField(max_length=50, null=True)
    url = models.CharField(max_length=250, null=True)
    users = models.ManyToManyField(User, related_name='users', through='Review')

    def __str__(self):
        return self.name

class Review(models.Model):
    rating = models.CharField(max_length=50, null=True)
    review = models.CharField(max_length=300, null=True)
    trail = models.ForeignKey(Trail, blank=True, null=True, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True, null=True, related_name='reviews', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'