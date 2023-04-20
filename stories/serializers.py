from rest_framework import serializers
from stories.models import Story


class StorySerializer(serializers.HyperlinkedModelSerializer):
    writer = serializers.ReadOnlyField(source='writer.username')

    class Meta:
        model = Story
        fields = [
            'url', 'id', 'title', 'content', 'writer', 'pub_date'
        ]
