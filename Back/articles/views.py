from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.models import Count
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article
from .serializers.article import ArticleListSerializer, ArticleSerializer

@api_view(['GET', 'POST'])
def article_list_or_create(request):
    # 게시글 전체 조회
    def article_list():
        # 좋아요 유저 수 column추가
        articles = Article.objects.annotate(
            like_count=Count('like_users', distinct=True)
        ).order_by('-pk')
        serializers = ArticleListSerializer(articles, many=True)
        return Response(serializers.data)
    
    # 게시글 생성
    def article_create():
        serializers = ArticleSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save(user_id=request.user)
            return Response(serializers.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        return article_list()
    elif request.method == 'POST':
        return article_create()

@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_or_update_or_delete(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    # 게시글 상세 페이지
    def article_detail():
        serializers = ArticleSerializer(article)
        return Response(serializers.data)
    
    # 게시글 수정
    def article_update():
        if request.user == article.user_id:
            serializers = ArticleSerializer(instance=article, data=request.data)
            if serializers.is_valid(raise_exception=True):
                serializers.save()
                return Response(serializers.data)

    # 게시글 삭제
    def article_delete():
        if request.user == article.user_id:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        return article_detail()
    elif request.method == 'PUT':
        return article_update()
    elif request.method == 'DELETE':
        return article_delete()

# 게시글 좋아요
@api_view(['POST'])
def article_like(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    user = request.user
    if article.like_users.filter(pk=user.pk).exists():
        article.like_users.remove(user)
        serializers = ArticleSerializer(article)
        return Response(serializers.data)
    else:
        article.like_users.add(user)
        serializers = ArticleSerializer(article)
        return Response(serializers.data)

def comment_create(request, article_id):
    pass

def comment_update_or_delete(request, article_id, comment_id):
    pass

def comment_like(request, article_id, comment_id):
    pass