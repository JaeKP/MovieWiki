from django.urls import path
from . import views

urlpatterns = [
    # 게시판 전체 조회 및 글 작성
    path('', views.article_list_or_create),

    # 인기 게시판 (최근 30일 이내 인기글)
    path('popular/', views.article_list_popular),

    # 자유 게시판 (ArticleType 1)
    path('general/', views.article_list_general),

    # 영화 게시판 (ArticleType 2)
    path('movie/', views.article_list_movie),

    # 배우 게시판 (ArticleType 3)
    path('actor/', views.article_list_actor),

    # 게시판 상세 페이지 조회 및 수정, 삭제
    path('<int:article_id>/', views.article_detail_or_update_or_delete),

    # 게시판 상세 페이지 글 좋아요
    path('<int:article_id>/like/', views.article_like),

    # 게시판 상세글 댓글 생성
    path('<int:article_id>/comment/', views.comment_create),

    # 게시판 상세글 댓글 수정 및 삭제
    path('<int:article_id>/comment/<int:comment_id>/',
        views.comment_update_or_delete),

    # 게시판 댓글 좋아요
    path('<int:article_id>/comment/<int:comment_id>/like/', views.comment_like),

    # 게시글 검색
    path('search', views.search_article),
]
