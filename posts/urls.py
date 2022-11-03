from django.urls import path
from . views import (
    admin_posts_list_user_view,
    admin_posts_create_view,
    posts_detail_view,
    posts_list_user_view,
    posts_list_view,
    )
urlpatterns = [
    path('',posts_list_view, name='post_list'),
    path('user/<str:user>',posts_list_user_view, name='post_list_user'),
    path('dashboard',admin_posts_list_user_view, name='admin_post_list_user'),
    path('dashboard/create',admin_posts_create_view, name='admin_post_create'),
    path('<slug:slug>',posts_detail_view, name='post_detail'),
    ]
