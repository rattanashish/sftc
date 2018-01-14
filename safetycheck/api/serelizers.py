from rest_framework import serializers

from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name =validated_data['first_name'],

        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ('username','email','password','first_name','last_name','id')

class user_bacserelizer(serializers.ModelSerializer):

    class Meta:
        model = user_bac_video
        fields = ('bac_level','user_video','timestamp')