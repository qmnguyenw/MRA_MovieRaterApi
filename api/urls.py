from django.urls import path
from django.conf.urls import include, url
from rest_framework import routers
from .views import MovieViewSet, RatingViewSet, UserViewSet
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('movies', MovieViewSet)
router.register('ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]