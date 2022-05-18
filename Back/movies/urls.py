from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    # 영화 리스트
    path('list/', views.movieList_info),
    # 영화 상세 정보
    path('<int:movie_id>/', views.moviedetail),
    # 영화 타이틀 검색
    path('search/<str:q>/', views.search),
    # 장르 선별
    path('genre/<int:genre_id>/', views.genre_filter),
    # 국가 선별
    path('country/<int:country_id>/', views.country_filter),
]