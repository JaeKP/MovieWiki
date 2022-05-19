import requests
import json
import re
from django.http import JsonResponse  
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

TMDB_API_KEY =  '9a1be42b20cb9255e18beb22379b225e' 
BASE_URL = 'https://api.themoviedb.org/3/movie'
actor_pk = 1

def genre_country_data(request):
    GENRE_URL = 'https://api.themoviedb.org/3/genre/movie/list'
    response = requests.get(
        GENRE_URL,
        params={
            'api_key': TMDB_API_KEY,
            'language': 'ko-kr',            
        }
    ).json()

    for genre in response.get('genres'):
        Genres.objects.create(
            id=genre.get('id'),
            name=genre.get('name')
        )

    # ISO 3166-1 변환용 json
    with open("movies/fixtures/language_info.json", 'r', encoding="utf-8") as file:
        language_info = json.load(file)
    
    for country in language_info:
        ProductionCountry.objects.create(
            id=country.get('id'),
            name=country.get('name')
        )
    return JsonResponse(response)

def get_youtube_key(movie_dict):  
    movie_id = movie_dict.get('id')
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}/videos',
        params={
            'api_key': TMDB_API_KEY
        }
    ).json()
    for video in response.get('results'):
        if video.get('site') == 'YouTube':
            return video.get('key')
    return 'nothing'

def get_actors(movie):
    global actor_pk
    movie_id = movie.id
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}/credits',
        params={
            'api_key': TMDB_API_KEY,
            'language': 'ko-kr',
        }
    ).json()
    for person in response.get('cast'):
        if person.get('known_for_department') != 'Acting': continue
        actor_id = person.get('id')
        character_name = person.get('character')
        request_url_person = f'https://api.themoviedb.org/3/person/{actor_id}?api_key={TMDB_API_KEY}&language=ko-KR'
        response = requests.get(request_url_person).json()
        korean_name = 0
        for _name in response.get('also_known_as'):
            hanCount = len(re.findall(u'[\u3130-\u318F\uAC00-\uD7A3]+', _name))
            if hanCount:
                name = _name
                korean_name = 1
                break
        if korean_name == 0:
            name = response.get('name')
        if not Actor.objects.filter(pk=actor_id).exists():
            Actor.objects.create(
                id=response.get('id'),
                name=name,
                profile_path= response.get('profile_path'),
            )
        movie.actors.add(actor_id)
        character = Characters.objects.get(pk=actor_pk)
        character.character_name = character_name
        character.save()
        actor_pk += 1
        if movie.actors.count() == 5:
            break

def get_director(movie):
    movie_id = movie.id
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}/credits',
        params={
            'api_key': TMDB_API_KEY,
            'language': 'ko-kr',
        }
    ).json()
    for person in response.get('crew'):
        if person.get('job') != 'Director': continue
        director_id = person.get('id')
        request_url_person = f'https://api.themoviedb.org/3/person/{director_id}?api_key={TMDB_API_KEY}&language=ko-KR'
        response = requests.get(request_url_person).json()
        korean_name = 0
        for _name in response.get('also_known_as'):
            hanCount = len(re.findall(u'[\u3130-\u318F\uAC00-\uD7A3]+', _name))
            if hanCount:
                name = _name
                korean_name = 1
                break
        if korean_name == 0:
            name = response.get('name')
        if not Director.objects.filter(pk=director_id).exists():
            Director.objects.create(
                id=response.get('id'),
                name=name,
                profile_path= response.get('profile_path'),
            )
        movie.director.add(director_id)
        if movie.director.count() == 1:
            break
    
@api_view(['GET'])
def data(request):
    global country_pk
    with open("movies/fixtures/language_id_info.json", 'r', encoding="utf-8") as file:
        language_id_info = json.load(file)
    print('인기 영화 목록')
    print('--------------------------------------------------------------')
    cnt = 1
    
    for i in range(1, 21):

        # popular api
        request_url = f"{BASE_URL}/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()
        
        
        for movie_dict in movies.get('results'): 
            if not movie_dict.get('release_date'):
                continue 
            trailer_key = get_youtube_key(movie_dict)

            movie_id = movie_dict.get('id')

            movie_name = movie_dict.get('title') 
            print(f'#{cnt} {movie_name}')
            cnt+=1 
            
            # 디테일 api
            request_url_detail = f"{BASE_URL}/{movie_id}?api_key={TMDB_API_KEY}&language=ko-KR"
            movie_detail = requests.get(request_url_detail).json()

            # 비슷한 영화 api
            request_url_similar= f'{BASE_URL}/{movie_id}/similar?api_key={TMDB_API_KEY}&language=ko-KR&page=1'
            movie_similars = requests.get(request_url_similar).json()

            # 비슷한 영화 id
            similar_movies = []
            for similar in movie_similars.get('results'):
                similar_movies.append(similar.get('id'))
            
            if not Movie.objects.filter(pk=movie_detail.get('id')).exists():
                movie = Movie.objects.create(
                    id=movie_detail.get('id'),
                    title= movie_name,
                    released_date= movie_detail.get('release_date'),
                    popularity= movie_detail.get('popularity'),
                    vote_avg= movie_detail.get('vote_average'),
                    overview= movie_detail.get('overview'),
                    poster_path= movie_detail.get('poster_path'),
                    adult= movie_detail.get('adult'),
                    # 'production_countries': countries,
                    runtime= movie_detail.get('runtime'),
                    status= movie_detail.get('status'),
                    tagline= movie_detail.get('tagline'),
                    trailer_youtube_key= trailer_key,
                    movie_similar= similar_movies,
                )

            for genre_id in movie_dict.get('genre_ids', []):
                movie.genre_ids.add(genre_id)
            
            for country in movie_detail.get('production_countries'):
                country_name = country.get('iso_3166_1')
                if language_id_info.get(country_name.lower()):
                    country_id = language_id_info[country_name.lower()]
                else:
                    country_id = -1
                movie.production_countries.add(country_id)
            get_actors(movie)
            get_director(movie)


    return JsonResponse(movie)
