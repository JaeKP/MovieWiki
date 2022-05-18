from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/', views.user_profile_or_update_or_delete),
]
