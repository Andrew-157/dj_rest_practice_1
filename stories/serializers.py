from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_nested.relations import NestedHyperlinkedRelatedField
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer,\
    UserSerializer as BaseUserSerializer
from stories.models import Story, Review


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = [
            'id', 'username', 'email', 'password'
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

    story = serializers.HyperlinkedRelatedField(
        view_name='story-detail', read_only=True
    )
    writer = serializers.HyperlinkedRelatedField(
        view_name='writer-detail', read_only=True
    )

    class Meta:
        model = Review
        fields = [
            'id', 'content', 'rating', 'pub_date', 'story', 'writer'
        ]

    def create(self, validated_data):
        writer_id = self.context['writer_id']
        story_id = self.context['story_id']
        return Review.objects.create(writer_id=writer_id,
                                     story_id=story_id,
                                     **validated_data)


class StorySerializer(serializers.HyperlinkedModelSerializer):
    writer = serializers.HyperlinkedRelatedField(
        view_name='writer-detail', read_only=True)

    reviews = NestedHyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='story-review-detail',
        parent_lookup_kwargs={
            'story_pk': 'story__pk'
        }
    )
    rating = serializers.HyperlinkedIdentityField(
        view_name='story-rating', read_only=True
    )

    class Meta:
        model = Story
        fields = [
            'url', 'id', 'title', 'content', 'writer', 'pub_date', 'reviews', 'rating'
        ]
