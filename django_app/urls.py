from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('users', views.UserView)
router.register('trails', views.TrailView)
router.register('reviews', views.ReviewView)
router.register('profile', views.ProfileView)

urlpatterns = [
    path('', include(router.urls))
]