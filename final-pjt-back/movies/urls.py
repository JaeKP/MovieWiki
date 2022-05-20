from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    # 인기 영화 리스트
    path('list/', views.popular_movie_list_info),
    # 영화 상세 정보
    path('<int:movie_id>/', views.moviedetail),
    # 영화 좋아요
    path('<int:movie_id>/like/', views.moviedetail_like),
    # 영화 리뷰 조회 작성
    path('review', views.moviedetail_review_or_create),
    # 영화 리뷰 수정, 삭제, 좋아요
    path('reviewDetail', views.moviedetail_review_update_or_delete_or_like),
    # 영화 검색 (타입: actor, director, title)
    path('search', views.search),
    # 필터 (타입: genre, country, director, actor, year,weather)
    path('filter', views.movie_filter),
    # 영화 트레일러
    path('trailer/', views.movie_trailer_list),
    # latest: 최근에 개봉한 영화 , interest: 최근 관심 , season: 계절 추천
    path('recommendation/<str:type>/', views.recommendation),

    # 데이터 베이스 구축용
    path('data/', views.data),
    path('basedata/', views.genre_country_data),
]