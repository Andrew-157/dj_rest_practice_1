from django.contrib.auth.models import User
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer,\
    UserSerializer as BaseUserSerializer
from rest_framework import serializers
from stories.models import Story


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = [
            'id', 'username', 'email', 'password'
        ]


class StorySerializer(serializers.HyperlinkedModelSerializer):
    writer = serializers.ReadOnlyField(source='writer.username')

    class Meta:
        model = Story
        fields = [
            'url', 'id', 'title', 'content', 'writer', 'pub_date'
        ]


class UserSerializer(BaseUserSerializer):
    stories = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='story-detail',
        read_only=True
    )

    class Meta(BaseUserSerializer.Meta):
        fields = [
            'url', 'id', 'username', 'email', 'stories'
        ]
