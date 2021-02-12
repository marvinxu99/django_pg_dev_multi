from django.urls import path, re_path

from . import views

app_name = 'boards'

urlpatterns = [
    path('', views.BoardListView.as_view(), name='boards_home'),

    path('<int:board_pk>/new/', views.new_topic, name='new_topic'),

    # path('<int:board_pk>/', views.board_topics, name='board_topics'),
    path('<int:board_pk>/', views.TopicListView.as_view(), name='board_topics'),

    #path('<int:board_pk>/topics/<int:topic_pk>/', views.topic_posts, name='topic_posts'),
    path('<int:board_pk>/topics/<int:topic_pk>/', views.PostListView.as_view(), name='topic_posts'),

    path('<int:board_pk>/topics/<int:topic_pk>/reply/', views.reply_topic, name='reply_topic'),
    path('<int:board_pk>/topics/<int:topic_pk>/delete/', views.delete_topic, name='delete_topic'),

    path('<int:board_pk>/topics/<int:topic_pk>/posts/<int:post_pk>/edit/',
        views.PostUpdateView.as_view(), name='edit_post'),

    path('<int:board_pk>/topics/<int:topic_pk>/posts/<int:post_pk>/delete/',
        views.delete_post, name='delete_post'),
]
