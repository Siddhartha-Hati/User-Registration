from django.contrib import admin
from django.urls import path
from user.views import *
from myvideo.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',SignupPage, name='signup'),
    path('login/',LoginPage, name='login' ),
    path('home/',HomePage, name='home' ),
    path('logout/',LogoutPage,name='logout'),
    path('video/', video_list, name='video_list'),
    path('video/watch/<int:pk>/', watch_video, name='watch_video'),
    path('upload/', upload_video, name='upload_video'),
    path('video/edit/<int:pk>/', edit_video, name='edit_video'),
    path('video/delete/<int:pk>/', delete_video, name='delete_video'),
]
