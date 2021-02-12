from django.urls import path, include, re_path

from . import views


app_name = 'kbase'
urlpatterns = [

    path('winn-jumps', views.winn_jumps, name='winn-jumps'),

]
