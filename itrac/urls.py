from django.urls import path
from . import views 

app_name = 'itrac'

urlpatterns = [
    path('', views.issues_assigned_to_me, name='issues_assigned_to_me'),
    path('my_issues/', views.issues_reported_by_me, name='issues_reported_by_me'),
    path('my_issues2/', views.issues_reported_by_me2, name='issues_reported_by_me2'),
    path('saved_issues/', views.saved_issues, name='saved_issues'),
    path('notifications/', views.my_notifications, name='my_notifications'),
    path('issue/<int:pk>/', views.issue_detail, name='issue_detail'),
    path('issue/<int:pk>/partial', views.issue_detail_partial, name='issue_detail_partial'),
    path('issue/new/', views.create_issue, name='new_issue'),
    path('issue/<int:pk>/edit/', views.edit_issue, name='edit_issue'),
    path('issue/<int:pk>/change_status/', views.issue_change_status, name='change_status'),
    path('comment/<int:issue_pk>/new/', views.create_comment, name='new_comment'),
    path('comment/<int:issue_pk>/<int:pk>/edit/', views.edit_comment, name='edit_comment'),
    path('comment/<int:issue_pk>/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
    path('reply/<int:issue_pk>/<int:comment_pk>/new/', views.create_or_edit_reply, name='new_reply'),
    path('reply/<int:issue_pk>/<int:comment_pk>/<int:pk>/edit/', views.create_or_edit_reply, name='edit_reply'),
    path('issue/tag/', views.issues_with_tag, name='issues_with_tag'),
    
    path('search/', views.search, name='search'),
    path('do_search/', views.do_search, name='do_search'),
    path('do_search_my/', views.do_search_my, name='do_search_my'),
    
    path('report/get_issue_type_json/', views.get_issue_type_json, name='get_issue_type_json'),
    path('report/get_status_json/', views.get_status_json, name='get_status_json'),
    path('report/get_bug_upvotes_json/', views.get_bug_upvotes_json, name='get_bug_upvotes_json'),
    path('report/get_feature_upvotes_json/', views.get_feature_upvotes_json, name='get_feature_upvotes_json'),
    path('report/', views.report, name='report'),

    path('issue/<int:pk>/upvote/', views.upvote, name='upvote'),
    path('issue/<int:pk>/save_issue/', views.save_issue, name='save_issue'),
    path('issue/<int:pk>/delete_saved_issue/', views.delete_saved_issue, name='delete_saved_issue'),
]