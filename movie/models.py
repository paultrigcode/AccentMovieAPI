from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    rated = models.CharField(max_length=100)
    released = models.CharField(max_length=100)
    runtime = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    writer = models.CharField(max_length=1000)
    actors = models.CharField(max_length=1000)
    plot = models.CharField(max_length=1000)
    language = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    awards = models.CharField(max_length=100)
    poster = models.CharField(max_length=1000)
    metascore = models.CharField(max_length=100)
    imdb_rating = models.CharField(max_length=100)
    imdb_votes = models.CharField(max_length=100)
    imdb_id = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    dvd = models.CharField(max_length=100)
    box_office = models.CharField(max_length=100)
    production = models.CharField(max_length=100)
    website = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} (id: {self.id})"


class Rating(models.Model):
    source = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="ratings")

    def __str__(self):
        return f"Rating from {self.source} to {self.movie.title})"


class Comment(models.Model):
    body = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f" Comment for {self.movie_id} (id: {self.movie.id}): {self.body}"
