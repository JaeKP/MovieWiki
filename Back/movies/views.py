import requests
from django.shortcuts import get_object_or_404
from .models import *
from .serializers.movie import MovieListSerializer, MovieSerializer
from .serializers.movie_review import MovieReviewSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count


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

@api_view(['POST'])
def moviedetail_like(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    user = request.user
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        serialzer = MovieSerializer(movie)
        return Response(serialzer.data)
    else:
        movie.like_users.add(user)
        serialzer = MovieSerializer(movie)
        return Response(serialzer.data)

@api_view(['GET', 'POST'])
def moviedetail_review_or_create(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    def moviedetail_review():
        review = movie.review.annotate(like_count=Count('like_users', distinct=True)).order_by('-like_count')
        serializer = MovieReviewSerializer(review, many=True)
        return Response(serializer.data)

    def moviedatail_review_create():
        serializer = MovieReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user_id=request.user, movie_id=movie)
            review = movie.review.annotate(like_count=Count('like_users', distinct=True)).order_by('-like_count')
            serializer = MovieReviewSerializer(review, many=True)
            return Response(serializer.data)

    if request.method == 'GET':
        return moviedetail_review()
    elif request.method == 'POST':
        return moviedatail_review_create()

@api_view(['PUT', 'DELETE'])
def moviedetail_review_update_delete(request, movie_id, review_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    review = get_object_or_404(MovieReview, pk=review_id)
    def moviedetail_review_update():
        if request.user == review.user_id:
            serializer = MovieReviewSerializer(instance=review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                review_list = movie.review.annotate(like_count=Count('like_users', distinct=True)).order_by('-like_count')
                serializer = MovieReviewSerializer(review_list, many=True)
                return Response(serializer.data)

    def moviedatail_review_delete():
        if request.user == review.user_id:
            review.delete()
            review_list = movie.review.annotate(like_count=Count('like_users', distinct=True)).order_by('-like_count')
            serializer = MovieReviewSerializer(review_list, many=True)
            return Response(serializer.data)

    if request.method == 'PUT':
        return moviedetail_review_update()
    elif request.method == 'DELETE':
        return moviedatail_review_delete()

@api_view(['POST'])
def moviedetail_review_like(request, movie_id, review_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    review = get_object_or_404(MovieReview, pk=review_id)
    user = request.user
    if review.like_users.filter(pk=user.pk).exists():
        review.like_users.remove(user)
        review_list = movie.review.annotate(like_count=Count('like_users', distinct=True)).order_by('-like_count')
        serializer = MovieReviewSerializer(review_list, many=True)
        return Response(serializer.data)
    else:
        review.like_users.add(user)
        review_list = movie.review.annotate(like_count=Count('like_users', distinct=True)).order_by('-like_count')
        serializer = MovieReviewSerializer(review_list, many=True)
        return Response(serializer.data)

@api_view(['GET','POST'])
def moviedetail_review_latest_or_create(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    def moviedetail_review_latest():
        review = movie.review.annotate(like_count=Count('like_users', distinct=True)).order_by('-created_at')
        serializer = MovieReviewSerializer(review, many=True)
        return Response(serializer.data)

    def moviedatail_review_latest_create():
        serializer = MovieReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user_id=request.user, movie_id=movie)
            review = movie.review.annotate(like_count=Count('like_users', distinct=True)).order_by('-created_at')
            serializer = MovieReviewSerializer(review, many=True)
            return Response(serializer.data)

    if request.method == 'GET':
        return moviedetail_review_latest()
    elif request.method == 'POST':
        return moviedatail_review_latest_create()

@api_view(['PUT', 'DELETE'])
def moviedetail_review_latest_update_delete(request, movie_id, review_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    review = get_object_or_404(MovieReview, pk=review_id)
    def moviedetail_review_latest_update():
        if request.user == review.user_id:
            serializer = MovieReviewSerializer(instance=review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                review_list = movie.review.annotate(like_count=Count('like_users', distinct=True)).order_by('-created_at')
                serializer = MovieReviewSerializer(review_list, many=True)
                return Response(serializer.data)

    def moviedatail_review_latest_delete():
        if request.user == review.user_id:
            review.delete()
            review_list = movie.review.annotate(like_count=Count('like_users', distinct=True)).order_by('-created_at')
            serializer = MovieReviewSerializer(review_list, many=True)
            return Response(serializer.data)

    if request.method == 'PUT':
        return moviedetail_review_latest_update()
    elif request.method == 'DELETE':
        return moviedatail_review_latest_delete()

@api_view(['POST'])
def moviedetail_review_latest_like(request, movie_id, review_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    review = get_object_or_404(MovieReview, pk=review_id)
    user = request.user
    if review.like_users.filter(pk=user.pk).exists():
        review.like_users.remove(user)
        review_list = movie.review.annotate(like_count=Count('like_users', distinct=True)).order_by('-created_at')
        serializer = MovieReviewSerializer(review_list, many=True)
        return Response(serializer.data)
    else:
        review.like_users.add(user)
        review_list = movie.review.annotate(like_count=Count('like_users', distinct=True)).order_by('-created_at')
        serializer = MovieReviewSerializer(review_list, many=True)
        return Response(serializer.data)

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