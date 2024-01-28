from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('list',BookView)
router.register('genre',GenreView)
router.register('review',ReviewView)

urlpatterns = [
    path('',include(router.urls))
]