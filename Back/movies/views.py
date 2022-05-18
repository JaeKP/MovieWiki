import requests
import json
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import *
from .serializers.movie import MovieListSerializer, MovieSerializer, MovieGenreListSerializer
from .serializers.actor import ActorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def popular_movie_list_info(request):
    movielist = Movie.objects.order_by('-popularity')[:10]
    serializer = MovieListSerializer(movielist, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def moviedetail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def search(request, q):
    results = Movie.objects.filter(title__icontains = q)[:10]
    serializer = MovieListSerializer(results, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    # .replace(" ", "")


@api_view(['GET'])
def genre_filter(request, genre_id):
    movies = Movie.objects.filter(genre_ids=genre_id).order_by('-popularity')[:10]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def country_filter(request, country_id):
    movies = Movie.objects.filter(production_countries=country_id).order_by('-popularity')[:10]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def director_filter(request, director_id):
    movies = Movie.objects.filter(director=director_id).order_by('-popularity')[:10]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def actor_filter(request, actor_id):
    movies = Movie.objects.filter(actors=actor_id).order_by('-popularity')[:10]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def year_filter(request, year):
    movies = Movie.objects.filter(released_date__startswith=year).order_by('-popularity')[:10]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def weather(request, area):
    API_KEY = "5d654e5750cf87fe1521ba1afb50a11a"
    area_data = {'서울': ( 37.56667, 126.97806),
            '인천': ( 37.469221, 126.573234),
            '광주': ( 35.15972, 126.85306),
            '대구': ( 35.798838, 128.583052),
            '울산': ( 35.519301, 129.239078),
            '대전': ( 36.321655, 127.378953),
            '부산': ( 35.198362, 129.053922),
            '경기': ( 37.567167, 127.190292),
            '강원': ( 37.555837, 128.209315),
            '충남': ( 36.557229, 126.779757),
            '충북': ( 36.628503, 127.929344),
            '경북': ( 36.248647, 128.664734),
            '경남': ( 35.259787, 128.664734),
            '전북': ( 35.716705, 127.144185),
            '전남': ( 34.819400, 126.893113),
            '제주': ( 33.364805, 126.542671)}
    lat, lon = area_data[area]
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    weather_data = requests.get(url).json()
    weather = weather_data.get("weather")[0].get("main")

    Weather_condition_codes = {
        'Thunderstorm': 53, 'Rain': 53, 'Drizzle': 18, 'Clouds': 18, 'Clear': 10402, 'Snow': 10751,
    }
    if Weather_condition_codes.get(weather):
        genre_id = Weather_condition_codes.get(weather)
    else:
        genre_id = 80
    
    movies = Movie.objects.filter(genre_ids=genre_id).order_by('-popularity')[:10]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)