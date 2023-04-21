from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from stories.models import Story, Review
from stories.serializers import StorySerializer, UserSerializer, ReviewSerializer
from stories.permissions import IsWriterOrReadOnly, IsReviewerOrReadOnly


class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.select_related('writer').all()
    serializer_class = StorySerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsWriterOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)


class WriterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsReviewerOrReadOnly
    ]

    def get_queryset(self):
        return Review.objects.filter(story=self.kwargs['story_pk'])

    def get_serializer_context(self):
        return {
            'request': self.request,
            'writer_id': self.request.user.id,
            'story_id': self.kwargs['story_pk']
        }
