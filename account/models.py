from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    bio = models.TextField(max_length=250,blank=True,null=True)
    website = models.CharField(max_length=250,blank=True,null=True)
    avatar = models.ImageField(null=True,blank=True,default='default/avatar.svg',upload_to='profile')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

