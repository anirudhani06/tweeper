from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('post/<int:post_id>/',views.post,name='post'),
    path('create-post',views.create_post,name='create-post'),
    path('delete-post/<int:post_id>/',views.delete_post,name='delete-post'),
    path('update-post/<int:post_id>/',views.update_post,name='update-post'),
    path('like-post',views.like_post,name='like-post'),
]
