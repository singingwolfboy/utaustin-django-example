from django.contrib.auth.models import User
from rest_framework import serializers
from tweeter.models import Tweet


class UserSerializer(serializers.ModelSerializer):
    bio = serializers.SerializerMethodField()

    def get_bio(self, obj):
        return obj.profile.bio

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "bio")


class TweetSerializer(serializers.ModelSerializer):
    creator = UserSerializer()

    class Meta:
        model = Tweet
        fields = ('content', 'creator', 'created_at')
