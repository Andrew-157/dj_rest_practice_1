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


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = [
            'id', 'content', 'rating', 'pub_date',
        ]

    def create(self, validated_data):
        reviewer_id = self.context['reviewer_id']
        story_id = self.context['story_id']
        return Review.objects.create(reviewer_id=reviewer_id,
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

    class Meta:
        model = Story
        fields = [
            'url', 'id', 'title', 'content', 'writer', 'pub_date',  'reviews'
        ]
