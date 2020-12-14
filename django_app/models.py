from django.db import models
from django.contrib.auth.models import User, AbstractUser

class User(AbstractUser):
    full_name = models.CharField(max_length=50, null=True)
    experience = models.CharField(max_length=50, null=True)
    age = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.username

class Trail(models.Model):
    trail_name = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=50, null=True)
    difficulty = models.CharField(max_length=50, null=True)
    length = models.CharField(max_length=50, null=True)
    elevation = models.CharField(max_length=50, null=True)
    route_type = models.CharField(max_length=50, null=True)
    users = models.ManyToManyField(User, related_name='users', through='Review')

    def __str__(self):
        return self.trail_name

class Review(models.Model):
    rating = models.CharField(max_length=50, null=True)
    review = models.CharField(max_length=300, null=True)
    trail = models.ForeignKey(Trail, blank=True, null=True, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True, null=True, related_name='reviews', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'