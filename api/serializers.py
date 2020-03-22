from rest_framework import serializers
from .models import Movie, Rating
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

'''
serializer convert data to json and vice versa
'''
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        # password cannot show and always require
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
    
    # create user and validate data, create token 
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        token = Token.objects.create(user=user)
        return user

    # custom validate (optional)
    # def validate_password(self, value):
    #     if value.isalnum()==True:
    #         raise serializers.ValidationError('password must have atleast one special character.')
    #     return value

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'no_of_ratings', 'avg_rating')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'stars', 'user', 'movie')