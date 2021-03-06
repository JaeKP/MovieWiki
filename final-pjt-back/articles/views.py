from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article, ArticleComment
from .serializers.article import ArticleListSerializer, ArticleSerializer, SearchArticleSerializer
from .serializers.article_comment import ArticleCommentSerializer
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q


@api_view(['GET', 'POST'])
def article_list_or_create(request):
    # 게시글 전체 조회
    def article_list():
        # 좋아요 유저 수 column추가
        articles = Article.objects.annotate(
            like_count=Count('like_users', distinct=True)
        ).order_by('-pk')
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    # 게시글 생성
    def article_create():
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user_id=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        return article_list()
    elif request.method == 'POST':
        return article_create()



@api_view(['GET'])
def search_article(request):
    query = request.GET.get('query', None)
    title = request.GET.getlist('title', None)
    content = request.GET.getlist('content', None)
    nickname = request.GET.get('nickname', None)
    type = request.GET.get('type')
    now = timezone.now()
    if query:
        q=Q()
        if title:
            q |= Q(title__icontains = query)
        if content:
            q |= Q(content__icontains = query)
        if nickname:
            q |= Q(user_id__nickname__icontains=query)
        if type == "all":
            results = Article.objects.filter(q).order_by('-pk')
        elif type == "popular":
            results = Article.objects.filter(q).filter(created_at__range=[now-timedelta(days=6), now]).annotate(like_count=Count('like_users', distinct=True)).order_by('-like_count')
        else:
            results = Article.objects.filter(q).filter(article_type=type).order_by('-pk')
    else:
        if type == "all":
            results = Article.objects.order_by('-pk')
        elif type == "popular":
            results = Article.objects.filter(created_at__range=[now-timedelta(days=6), now]).annotate(like_count=Count('like_users', distinct=True)).order_by('-like_count')
        else:
            results = Article.objects.filter(article_type=type).order_by('-pk')

    serializer = ArticleListSerializer(results, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)




@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_or_update_or_delete(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    # 게시글 상세 페이지
    def article_detail():
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    # 게시글 수정
    def article_update():
        if request.user == article.user_id:
            serializer = ArticleSerializer(
                instance=article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)


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
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    else:
        article.like_users.add(user)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    serializer = ArticleCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, article=article)
        comments = article.comment.all()
        serializer = ArticleCommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def comment_update_or_delete(request, article_id, comment_id):
    comment = get_object_or_404(ArticleComment, pk=comment_id)
    article = get_object_or_404(Article, pk=article_id)

    def comment_update():
        if request.user == comment.user:
            serializer = ArticleCommentSerializer(
                instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                comments = article.comment.all()
                serializer = ArticleCommentSerializer(comments, many=True)
                return Response(serializer.data)

    def comment_delete():
        if request.user == comment.user:
            comment.delete()
            comments = article.comment.all()
            serializer = ArticleCommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    if request.method == 'PUT':
        return comment_update()
    elif request.method == 'DELETE':
        return comment_delete()


@api_view(['POST'])
def comment_like(request, article_id, comment_id):
    comment = get_object_or_404(ArticleComment, pk=comment_id)
    article = get_object_or_404(Article, pk=article_id)
    user = request.user
    if comment.like_users.filter(pk=user.pk).exists():
        comment.like_users.remove(user)
        comments = article.comment.all()
        serializer = ArticleCommentSerializer(comments, many=True)
        return Response(serializer.data)
    else:
        comment.like_users.add(user)
        comments = article.comment.all()
        serializers = ArticleCommentSerializer(comments, many=True)
        return Response(serializers.data)



