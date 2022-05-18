from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path('list/', views.movieList_info),
    path('<int:movie_id>/', views.moviedetail),
    path('genre/<str:q>/', views.genre_list),

]