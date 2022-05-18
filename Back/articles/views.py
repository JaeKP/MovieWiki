from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article, ArticleComment
from .serializers.article import ArticleListSerializer, ArticleSerializer
from .serializers.article_comment import ArticleCommentSerializer
from django.utils import timezone
from datetime import timedelta


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


@api_view(['GET'])
def article_list_popular(reqeust):
    now = timezone.now()
    # 최근 1주일 게시글, 좋아요 순으로 나열
    articles = Article.objects.filter(
        created_at__range=[now-timedelta(days=6), now]
    ).annotate(
        like_count=Count('like_users', distinct=True)
    ).order_by('-like_count')
    serializers = ArticleListSerializer(articles, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def article_list_general(request):
    articles = Article.objects.filter(
        article_type=1
    ).annotate(
        like_count=Count('like_users', distinct=True)
    ).order_by('-pk')
    serialzers = ArticleListSerializer(articles, many=True)
    return Response(serialzers.data)


@api_view(['GET'])
def article_list_movie(request):
    articles = Article.objects.filter(
        article_type=2
    ).annotate(
        like_count=Count('like_users', distinct=True)
    ).order_by('-pk')
    serialzers = ArticleListSerializer(articles, many=True)
    return Response(serialzers.data)


@api_view(['GET'])
def article_list_actor(request):
    articles = Article.objects.filter(
        article_type=3
    ).annotate(
        like_count=Count('like_users', distinct=True)
    ).order_by('-pk')
    serialzers = ArticleListSerializer(articles, many=True)
    return Response(serialzers.data)


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
            serializers = ArticleSerializer(
                instance=article, data=request.data)
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


@api_view(['POST'])
def comment_create(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    serializers = ArticleCommentSerializer(data=request.data)
    if serializers.is_valid(raise_exception=True):
        serializers.save(user=request.user, article=article)
        comments = article.comment.all()
        serializers = ArticleCommentSerializer(comments, many=True)
        return Response(serializers.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def comment_update_or_delete(request, article_id, comment_id):
    comment = get_object_or_404(ArticleComment, pk=comment_id)
    article = get_object_or_404(Article, pk=article_id)

    def comment_update():
        if request.user == comment.user:
            serializers = ArticleCommentSerializer(
                instance=comment, data=request.data)
            if serializers.is_valid(raise_exception=True):
                serializers.save()
                comments = article.comment.all()
                serializers = ArticleCommentSerializer(comments, many=True)
                return Response(serializers.data)

    def comment_delete():
        if request.user == comment.user:
            comment.delete()
            comments = article.comment.all()
            serializers = ArticleCommentSerializer(comments, many=True)
            return Response(serializers.data, status=status.HTTP_204_NO_CONTENT)

    if request.method == 'PUT':
        return comment_update()
    elif request.method == 'DELETE':
        return comment_delete()


@api_view(['POST'])
def comment_like(request, article_id, comment_id):
    comment = get_object_or_404(ArticleComment, pk=comment_id)
    user = request.user
    if comment.like_users.filter(pk=user.pk).exists():
        comment.like_users.remove(user)
        serializers = ArticleCommentSerializer(comment)
        return Response(serializers.data)
    else:
        comment.like_users.add(user)
        serializers = ArticleCommentSerializer(comment)
        return Response(serializers.data)
