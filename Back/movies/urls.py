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
    # 영화 리뷰(인기도순)
    path('<int:movie_id>/review/', views.moviedetail_review_or_create),
    # 영화 리뷰 수정 및 삭제 
    path('<int:movie_id>/review/<int:review_id>/', views.moviedetail_review_update_delete),
    # 영화 리뷰 좋아요
    path('<int:movie_id>/review/<int:review_id>/like/', views.moviedetail_review_like),
    # 영화 리뷰(최신순)
    path('<int:movie_id>/review/latest/', views.moviedetail_review_latest_or_create),
    # 영화 리뷰(최신순) 수정 및 삭제
    path('<int:movie_id>/review/latest/<int:review_id>/', views.moviedetail_review_latest_update_delete),    
    # 영화 리뷰(최신순) 좋아요
    path('<int:movie_id>/review/latest/<int:review_id>/like/', views.moviedetail_review_latest_like),
    # 영화 타이틀 검색
    path('search/<str:q>/', views.search),
    # 장르 필터
    path('genre/<int:genre_id>/', views.genre_filter),
    # 국가 필터
    path('country/<int:country_id>/', views.country_filter),
    # 감독 필터
    path('director/<int:director_id>/', views.director_filter),
    # 배우 필터
    path('actor/<int:actor_id>/', views.actor_filter),
    # 년도 필터
    path('year/<int:year>/', views.year_filter),
    # 날씨
    path('weather/<str:area>/', views.weather),
    path('data/', views.data),
    path('basedata/', views.genre_country_data),

    # 영화 트레일러
    path('trailer/', views.movie_trailer_list),
]