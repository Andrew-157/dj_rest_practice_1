from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from stories.models import Story
from stories.serializers import StorySerializer, UserSerializer
from stories.permissions import IsWriterOrReadOnly


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
