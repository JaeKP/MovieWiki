from django.contrib import admin
from .models import ArticleType, Article, ArticleComment
# Register your models here.

admin.site.register(Article)
admin.site.register(ArticleComment)
admin.site.register(ArticleType)

