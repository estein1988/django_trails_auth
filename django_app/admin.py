from django.contrib import admin
from .models import User, Trail, Review

# Register your models here.
admin.site.register(User)
admin.site.register(Trail)
admin.site.register(Review)