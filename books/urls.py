from django.urls import path, re_path

from . import views

app_name = 'books'

urlpatterns = [
    path('', views.book_list, name='books_list'),
    path('create/', views.book_create, name='book_create'),
    path('update/<int:pk>/', views.book_update, name='book_update'),
    path('delete/<int:pk>', views.book_delete, name='book_delete'),

]
