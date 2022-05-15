from django.db import transaction
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from .models import Comment, Movie, Rating


class RatingSerializer(serializers.Serializer):
    Source = serializers.CharField(max_length=100, source="source")
    Value = serializers.CharField(max_length=100, source="value")


class MovieInputSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)


class MovieSerializer(serializers.Serializer):
    Title = serializers.CharField(max_length=100, source="title")
    Year = serializers.CharField(max_length=100, source="year")
    Rated = serializers.CharField(max_length=100, source="rated")
    Released = serializers.CharField(max_length=100, source="released")
    Runtime = serializers.CharField(max_length=100, source="runtime")
    Genre = serializers.CharField(max_length=100, source="genre")
    Director = serializers.CharField(max_length=100, source="director")
    Writer = serializers.CharField(max_length=1000, source="writer")
    Actors = serializers.CharField(max_length=1000, source="actors")
    Plot = serializers.CharField(max_length=1000, source="plot")
    Language = serializers.CharField(max_length=100, source="language")
    Country = serializers.CharField(max_length=100, source="country")
    Awards = serializers.CharField(max_length=100, source="awards")
    Poster = serializers.CharField(max_length=1000, source="poster")
    Metascore = serializers.CharField(max_length=100, source="metascore")
    imdbRating = serializers.CharField(max_length=100, source="imdb_rating")
    imdbVotes = serializers.CharField(max_length=100, source="imdb_votes")
    imdbID = serializers.CharField(max_length=100, source="imdb_id")
    Type = serializers.CharField(max_length=100, source="type")
    DVD = serializers.CharField(max_length=100, source="dvd")
    BoxOffice = serializers.CharField(max_length=100, source="box_office")
    Production = serializers.CharField(max_length=100, source="production")
    Website = serializers.CharField(max_length=100, source="website")
    Ratings = RatingSerializer(many=True, source="ratings")

    @transaction.atomic
    def save(self):
        rating_data = self.validated_data.pop("ratings")
        movie = Movie.objects.create(**self.validated_data)
        ratings = [Rating(**data, movie=movie) for data in rating_data]
        Rating.objects.bulk_create(ratings)
        return movie


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class CommentBodySerializer(serializers.Serializer):
    movie = serializers.IntegerField(required=True)
    body = serializers.CharField(required=True)
