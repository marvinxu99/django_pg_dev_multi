from django.urls import path

from . import views


app_name = 'posts'
urlpatterns = [
    path('', views.AllPostsListView.as_view(), name='all_posts'),
    path('create/', views.create_post, name='create_post'),
    path('cards/', views.responsive_cards, name='responsive_cards'),
    path('carousel/', views.AllPostsCarouselView.as_view(), name='all_posts_carousel'),
    path('carousel_demo/', views.carousel_demo, name='carousel_demo'),
    path('<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('by-user', views.AllPostsByUserListView.as_view(), name='all_posts_user'),
]
