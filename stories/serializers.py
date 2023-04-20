from django.contrib.auth.models import User
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer,\
    UserSerializer as BaseUserSerializer
from stories.models import Story, Review


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = [
            'id', 'username', 'email', 'password'
        ]


class StorySerializer(serializers.HyperlinkedModelSerializer):
    # writer = serializers.ReadOnlyField(source='writer.username')
    writer = serializers.HyperlinkedRelatedField(
        view_name='writer-detail', read_only=True)

    class Meta:
        model = Story
        fields = [
            'url', 'id', 'title', 'content', 'writer', 'pub_date'
        ]


class UserSerializer(BaseUserSerializer):

    stories = serializers.HyperlinkedRelatedField(
        many=True, view_name='story-detail', read_only=True
    )

    class Meta(BaseUserSerializer.Meta):
        fields = [
            'id', 'username', 'email', 'stories'
        ]


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    reviewer = serializers.HyperlinkedRelatedField(
        view_name='writer-detail', read_only=True
    )
    story = serializers.HyperlinkedRelatedField(
        view_name='story-detail', read_only=True
    )

    class Meta:
        model = Review
        fields = [
            'url', 'id', 'content', 'story', 'reviewer', 'rating', 'pub_date'
        ]
