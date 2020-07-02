from django.urls import path, re_path

from . import views

app_name = 'books'

urlpatterns = [
    path('', views.book_list, name='books_list'),
    path('create/', views.book_create, name='book_create'),
    
]
