from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Actor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    profile_path = models.TextField(null=True)


class Director(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    profile_path = models.TextField(null=True)


class Genres(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=True)


class ProductionCountry(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=True)


class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, null=True)
    genre_ids = models.ManyToManyField(Genres, related_name="movies")
    overview = models.TextField(null=True)
    released_date = models.DateField(null=True)
    vote_avg = models.FloatField(null=True)
    tagline = models.TextField(null=True)
    status = models.CharField(max_length=50, null=True)
    runtime = models.IntegerField(default=120, null=True, blank=True)
    trailer_youtube_key = models.TextField(null=True)
    director = models.ManyToManyField(Director, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies' ,through='Characters')
    poster_path = models.TextField(null=True)
    production_countries = models.ManyToManyField(ProductionCountry, related_name='movies', through='MovieCountry')
    adult = models.BooleanField(null=True)
    popularity = models.FloatField(null=True)
    like_users = models.ManyToManyField(User, related_name='like_movies')
    movie_similar = models.JSONField(blank=True)

    
class MovieCountry(models.Model):
    id = models.IntegerField(primary_key=True)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE,  related_name='country_name')
    country_id = models.ForeignKey(ProductionCountry, on_delete=models.CASCADE,  related_name='country_name')
    country_name = models.CharField(max_length=100, null=True)


class Characters(models.Model):
    id = models.IntegerField(primary_key=True)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE,  related_name='characters_id')
    actor_id = models.ForeignKey(Actor, on_delete=models.CASCADE,  related_name='characters_id')
    character_name = models.CharField(max_length=100, null=True)


class MovieReview(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="review")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review")
    like_users = models.ManyToManyField(User, related_name='like_reviews')
    content = models.TextField()
    spoiler = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)