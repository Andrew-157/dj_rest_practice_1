from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from stories import views


router = DefaultRouter()
router.register(r'stories', views.StoryViewSet, basename='story')
router.register(r'writers', views.WriterViewSet, basename='writer')

stories_router = routers.NestedDefaultRouter(
    router, r'stories', lookup='story')
stories_router.register(r'reviews', views.ReviewViewSet,
                        basename='story-reviews')


urlpatterns = router.urls + stories_router.urls
