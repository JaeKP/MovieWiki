import requests
import json
import re
from django.http import JsonResponse  
from django.shortcuts import get_object_or_404
from .models import *
from .serializers.movie import MovieListSerializer, MovieSerializer, MovieTrailerSerializer
from .serializers.movie_review import MovieReviewSerializer
from .serializers.actor import ActorDetailSerializer
from .serializers.directors import DirectorDetailSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from django.db.models import Q
from django.utils import timezone
from datetime import timedelta


@api_view(['GET'])
def popular_movie_list_info(request):
    movielist = Movie.objects.order_by('-popularity')[:21]
    serializer = MovieListSerializer(movielist, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# 영화 상세 페이지
@api_view(['GET'])
def moviedetail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)

# 영화 상세 페이지 좋아요
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

# 영화 상세 페이지 리뷰
# filter_type: 1 => 인기순
# filter_type: 2 => 최신순 
@api_view(['GET', 'POST'])
def moviedetail_review_or_create(request):
    movie_id = request.GET.get('movie_id')
    filter_type  = request.GET.get('type')
    movie = get_object_or_404(Movie, pk=movie_id) 
    def moviedetail_review():
        if filter_type == 1: 
            review = movie.review.annotate(like_count=Count('like_users', distinct=True)).order_by('-like_count')
        else : 
            review = movie.review.annotate(like_count=Count('like_users', distinct=True)).order_by('-created_at')
        serializer = MovieReviewSerializer(review, many=True)
        return Response(serializer.data)

    def moviedatail_review_create():
        serializer = MovieReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user_id=request.user, movie_id=movie)
            if filter_type == 1: 
                review = movie.review.annotate(like_count=Count('like_users', distinct=True)).order_by('-like_count')
            else: 
                review = movie.review.annotate(like_count=Count('like_users', distinct=True)).order_by('-created_at')
            serializer = MovieReviewSerializer(review, many=True)
            return Response(serializer.data)

    if request.method == 'GET':
        return moviedetail_review()
    elif request.method == 'POST':
        return moviedatail_review_create()

@api_view(['POST', 'PUT', 'DELETE'])
def moviedetail_review_update_or_delete_or_like(request):
    movie_id = request.GET.get('movie_id')
    filter_type  = request.GET.get('type')
    review_id  = request.GET.get('review_id')
    movie = get_object_or_404(Movie, pk=movie_id)
    review = get_object_or_404(MovieReview, pk=review_id)

    # 좋아요
    def moviedetail_like():
        user = request.user
        if review.like_users.filter(pk=user.pk).exists():
            review.like_users.remove(user)
            if filter_type == 1: 
                review_list = movie.review.annotate(like_count=Count('like_users', distinct=True)).order_by('-like_count')
            else: 
                review_list = movie.review.annotate(like_count=Count('like_users', distinct=True)).order_by('-created_at')
            serializer = MovieReviewSerializer(review_list, many=True)
            return Response(serializer.data)
        else:
            review.like_users.add(user)
            if filter_type == 1: 
                review_list = movie.review.annotate(like_count=Count('like_users', distinct=True)).order_by('-like_count')
            else: 
                review_list = movie.review.annotate(like_count=Count('like_users', distinct=True)).order_by('-created_at')
            serializer = MovieReviewSerializer(review_list, many=True)
            return Response(serializer.data)
    
    # 업데이트
    def moviedetail_review_update():
        if request.user == review.user_id:
            serializer = MovieReviewSerializer(instance=review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                if filter_type == 1: 
                    review_list = movie.review.annotate(like_count=Count('like_users', distinct=True)).order_by('-like_count')
                else: 
                    review_list = movie.review.annotate(like_count=Count('like_users', distinct=True)).order_by('-created_at')
                serializer = MovieReviewSerializer(review_list, many=True)
                return Response(serializer.data)

    # 삭제
    def moviedatail_review_delete():
        if request.user == review.user_id:
            review.delete()
            if filter_type == 1: 
                review_list = movie.review.annotate(like_count=Count('like_users', distinct=True)).order_by('-like_count')
            else: 
                review_list = movie.review.annotate(like_count=Count('like_users', distinct=True)).order_by('-created_at')
            serializer = MovieReviewSerializer(review_list, many=True)
            return Response(serializer.data)

    if request.method == 'POST':
        return moviedetail_like()
    elif request.method == 'PUT':
        return moviedetail_review_update()
    elif request.method == 'DELETE':
        return moviedatail_review_delete()


# 트레일러 게시판
@api_view(['GET'])
def movie_trailer_list(reuquest):
    movie = Movie.objects.filter(~Q(trailer_youtube_key='nothing') ,popularity__gt=99).order_by('?')
    serializer = MovieTrailerSerializer(movie, many=True)
    return Response(serializer.data)    

# 검색 기능
@api_view(['GET'])
def search(request):
    query = request.GET.get('query')
    filter_type = request.GET.get('type')

    if filter_type == 'title':
        results = Movie.objects.filter(title__icontains = query)[:21]
        serializer = MovieListSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif filter_type == 'actor':
        results = Actor.objects.filter(name__icontains = query)[:21]
        serializer = ActorDetailSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif filter_type == 'director':
        results = Director.objects.filter(name__icontains = query)[:21]
        serializer = DirectorDetailSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

def weather(area):
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
        return Weather_condition_codes.get(weather)
    else:
        return 80


# 종류별 필터
@api_view(['GET'])
def movie_filter(request):
    query = request.GET.get('query')
    filter_type = request.GET.get('type')

    if filter_type == 'genre':
        movies = Movie.objects.filter(genre_ids=query).order_by('-popularity')[:21]
    elif filter_type == 'country':
        movies = Movie.objects.filter(production_countries=query).order_by('-popularity')[:21]
    elif filter_type == 'director':
        movies = Movie.objects.filter(director=query).order_by('-popularity')[:21]
    elif filter_type == 'actor':
        movies = Movie.objects.filter(actors=query).order_by('-popularity')[:21]
    elif filter_type == 'year':
        movies = Movie.objects.filter(released_date__startswith=query).order_by('-popularity')[:21]
    elif filter_type == 'weather':
        genre_id = weather(query)
        movies = Movie.objects.filter(genre_ids=genre_id).order_by('-popularity')[:21]

    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



# 추천기능 (데이터 20개 뽑기)
@api_view(['GET'])
def recommendation(request, type):
    # 영화 추천1. 최근에 개봉한 영화 
    # 최근 50일 이내 인기도순으로 정렬
    if type == 'latest':
        now = timezone.now()
        movies = Movie.objects.filter(released_date__range=[now-timedelta(days=50), now]).order_by('-popularity')[:21]
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

    # 영화 추천2. 요즘 제일 관심받는 영화 (최근 30일 이내 작성한 리뷰 수가 많은 영화)
    elif type == 'interest':
        now = timezone.now()
        movies = Movie.objects.annotate(
            review_count=Count(
                'review', distinct=True, filter = Q(
                    review__created_at__range=[now-timedelta(days=30), now]
                    ))).order_by('-review_count')[:21]
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    
    # 영화 추천3. 계절 추천 영화
    # 봄: 로맨스, 여름: 공포, 가을:모험 , 겨울: 판타지
    # 인기 99 이상 랜덤
    elif type == 'season':
        now = int(timezone.now().strftime('%m'))
        if now == 3 or now == 4 or now == 5:
            season = 'spring'
        elif now == 6 or now == 7 or now == 8:
            season = 'summer'
        elif now == 9 or now == 10 or now == 12:
            season = 'fall'
        else:
            season = 'winter'
        season_code = {
            'spring': 10749, 'summer': 27, 'fall': 12, 'winter': 14
        }
        genre_id = season_code.get(season)
        movies = Movie.objects.filter(genre_ids=genre_id, popularity__gt=99).order_by('?')[:21]
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    
    # 영화 추천 10. 같은 나이대의 유저가 좋아요한 랭크
    elif type == 'age':
        movies = Movie.objects.annotate(
            like_users_count=Count(
                'like_users', distinct=True, filter = Q(
                    like_users__age__range=[request.user.age -3, request.user.age + 3]
                    ))).order_by('-like_users_count')[:21]
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


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
    try:
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
    except:
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
        if not person.get('character'): continue 
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
    
    for i in range(70, 501):

        # popular api
        request_url = f"{BASE_URL}/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()
        
        
        for movie_dict in movies.get('results'): 
            print(movie_dict.get('title'))
            
            if not movie_dict.get('release_date'):
                continue 
            if not movie_dict.get('overview'):
                continue
            if not movie_dict.get('poster_path'):
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
                if not similar.get('release_date'):
                    continue 
                if not similar.get('overview'):
                    continue
                if not similar.get('poster_path'):
                    continue
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
