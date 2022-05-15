from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, MovieViewSet

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("comments", CommentViewSet)

urlpatterns = [
    # path("movies", MoviesView.as_view(), name="MoviesView"),
    path("", include(router.urls)),
    # path("comments", CommentsView.as_view(), name="CommentsView"),
]
