from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:username>/', views.user_profile_or_update_or_delete),

    # 이미지 파일을 업로드 하지 않고 유저 정보를 수정하는 경우 
    path('onlyprofile/<str:username>/', views.only_user_profile_update),

    # 이미지 업로드할 경우, 정보수정창에 보이게 하기 위함
    path('temporary/profile/<str:username>/', views.temporary_user_upload_image),
]
