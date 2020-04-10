from django.urls import path, include, re_path

from . import views


app_name = 'posts'
urlpatterns = [    
    path('', views.HomePageView.as_view(), name='home'),
    path('add/', views.CreatePostView.as_view(), name='add_post')
]
