from rest_framework import serializers


class TweetSerializer(serializers.Serializer):
    content = serializers.CharField()
    creator = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField()

    def get_creator(self, obj):
        return obj.creator.username
