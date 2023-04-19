from django.urls import path, include
from rest_framework import routers
from stories import views


class StoriesApiRoot(routers.APIRootView):
    pass


class DefaultRouter(routers.DefaultRouter):
    APIRootView = StoriesApiRoot


router = DefaultRouter()
router.register(r'stories', views.StoryViewSet, basename='story')


urlpatterns = [
    path('', include(router.urls))
]
urlpatterns = router.urls
