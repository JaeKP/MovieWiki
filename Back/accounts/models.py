from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    nickname = models.CharField(max_length=10)
    region = models.CharField(max_length=10)
    profile_image =  models.ImageField(upload_to='uploads/%Y/%m/%d', blank=True)
    search_keyword = models.JSONField(null=True)