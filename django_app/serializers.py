from rest_framework import serializers
from .models import User, Trail, Review
from django.contrib.auth.hashers import make_password

class TrailObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trail
        fields = ('id', 'city', 'state', 'country', 'name', 'unique_id', 'directions', 'lat', 'lon', 'description', 'thumbnail', 'length', 'url')

class UserObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'full_name', 'experience', 'age')

class ReviewObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'trail')

class UserSerializer(serializers.ModelSerializer):
    reviews = ReviewObjectSerializer(many=True, required=False)
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'full_name', 'experience', 'age', 'reviews')

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            password = make_password(validated_data['password']),
            email = validated_data['email'],
            full_name = validated_data['full_name'],
            experience = validated_data['experience'],
            age = validated_data['age']
        )

        user.save()

        return user

class TrailSerializer(serializers.ModelSerializer):
    users = UserObjectSerializer(many=True)
    reviews = ReviewObjectSerializer(many=True)

    class Meta:
        model = Trail
        fields = ('id', 'city', 'state', 'country', 'name', 'unique_id', 'directions', 'lat', 'lon', 'description', 'thumbnail', 'length', 'url', 'users', 'reviews')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'rating', 'review', 'user', 'trail')