from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters, mixins, status, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from .client import (MovieAPIConnectionException, MovieAPINotFoundException,
                     fetch_movie)
from .models import Comment, Movie
from .serializers import (CommentSerializer, MovieInputSerializer,
                          MovieSerializer)


class MovieViewSet(
    viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin
):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["id"]

    @swagger_auto_schema(request_body=MovieInputSerializer)
    def create(self, request):
        input_serialiser = MovieInputSerializer(data=request.data)
        input_serialiser.is_valid(raise_exception=True)

        try:
            data = fetch_movie(input_serialiser.validated_data["title"])
        except MovieAPIConnectionException as msg:
            return Response({"detail": "Something went wrong"})
        except MovieAPINotFoundException as exc:
            raise NotFound(detail=exc.args[0])

        if Movie.objects.filter(title=data["Title"]).exists():
            movie = Movie.objects.get(title=data["Title"])
            serializer = self.serializer_class(movie)
            return Response(serializer.data)

        serializer = self.serializer_class(data=data)

        if not serializer.is_valid():
            msg = "Problem with serializing data from external API"
            return Response(
                data={"detail": msg}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        data = serializer.data
        serializer.save()
        return Response(data)


class CommentViewSet(
    viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin
):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("movie",)
    ordering_fields = ["movie"]

    @swagger_auto_schema(request_body=CommentSerializer)
    def create(self, request):
        input_serialiser = CommentSerializer(data=request.data)
        input_serialiser.is_valid(raise_exception=True)
        if input_serialiser.is_valid():
            input_serialiser.save()
            return Response(input_serialiser.data)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
