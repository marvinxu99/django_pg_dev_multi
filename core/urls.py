from django.urls import path, include, re_path

from . import views


app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('core_code_builder/', views.core_code_builder, name='core_code_builder'),
]
