from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class ArticleType(models.Model):
    name=models.CharField(max_length=10)

class Article(models.Model):
    article_type = models.ForeignKey(ArticleType, on_delete=models.CASCADE, related_name="article")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="article")
    like_users = models.ManyToManyField(User, related_name="like_articles")
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ArticleComment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comment")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment")
    like_users = models.ManyToManyField(User, related_name="like_comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



