from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import User, Trail, Review
from .serializers import UserSerializer, TrailSerializer, ReviewSerializer

# Create your views here.

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny,]

class TrailView(viewsets.ModelViewSet):
    queryset = Trail.objects.all()
    serializer_class = TrailSerializer

class ReviewView(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ProfileView(viewsets.ViewSet):
    queryset = User.objects.all()
    def list(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)