from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

UserModel = settings.AUTH_USER_MODEL

# Create your models here.
class User(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    nickname = models.CharField(max_length=10)
    region = models.CharField(max_length=10)
    profile_image =  models.ImageField(upload_to='uploads/%Y/%m/%d', blank=True, null=True)
    search_keyword = models.JSONField(null=True)



class UserUploadImage(models.Model):
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE, related_name="upload_image")
    profile_image = models.ImageField(upload_to="temporary/uploads/%Y/%m/%d", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
