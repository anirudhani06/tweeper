from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Post,Category
# Register your models here.

admin.site.register(Post)
admin.site.register(Category)



admin.site.unregister(Group)