from rest_framework import serializers
from instagram.models import Feed


class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = ['id', 'content', 'image', 'profile_image', 'user_id', 'like_count']
