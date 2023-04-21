from django.db import models
from account.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True) 
    image = models.ImageField(null=True,blank=True,upload_to='posts')
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    body = models.TextField(blank=True,null=True)
    like_count = models.IntegerField(default=0)
    created= models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created']

class Likes(models.Model):
    user = models.IntegerField(null=True)
    post = models.IntegerField(null=True)





