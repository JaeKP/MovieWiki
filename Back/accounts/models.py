from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class User(AbstractUser):
    age = models.IntegerField()
    nickname = models.CharField(max_length=10)
    region = models.CharField(max_length=10)
    profile_image =  models.TextField(null=True)
    search_keyword = ArrayField(models.CharField(max_length=20, null=True), size=5)