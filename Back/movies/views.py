from django.shortcuts import get_list_or_404, get_object_or_404
from .models import *
from .serializers.movie import MovieListSerializer, MovieSerializer, MovieGenreListSerializer
from .serializers.actor import ActorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def movieList_info(request):
    movielist = get_list_or_404(Movie)
    serializer = MovieListSerializer(movielist, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def moviedetail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def search(request, q):
    results = Movie.objects.filter(title__icontains = q)
    serializer = MovieListSerializer(results, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    # .replace(" ", "")


@api_view(['GET'])
def genre_filter(request, genre_id):
    movies = Movie.objects.filter(genre_ids=genre_id).order_by('-popularity')
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def country_filter(request, country_id):
    movies = Movie.objects.filter(production_countries=country_id).order_by('-popularity')
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)