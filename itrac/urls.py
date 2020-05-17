from django.urls import path
from .views import get_issues, issue_detail, create_issue, \
    edit_issue, create_or_edit_comment, search, get_issue_type_json, \
    get_status_json, get_bug_upvotes_json, get_feature_upvotes_json, report, \
    upvote, my_issues, my_notifications, create_or_edit_reply, save_issue, \
    saved_issues, delete_saved_issue, do_search, do_search_my

app_name = 'itrac'

urlpatterns = [
    path('my_issues/', my_issues, name='my_issues'),
    path('saved_issues/', saved_issues, name='saved_issues'),
    path('notifications/', my_notifications, name='my_notifications'),
    path('', get_issues, name='get_issues'),
    path('<int:pk>/', issue_detail, name='issue_detail'),
    path('new/', create_issue, name='new_issue'),
    path('<int:pk>/edit/', edit_issue, name='edit_issue'),
    path('<int:issue_pk>/new/', create_or_edit_comment, name='new_comment'),
    path('<int:issue_pk>/<int:pk>/edit/', create_or_edit_comment, name='edit_comment'),
    path('<int:issue_pk>/<int:comment_pk>/new/', create_or_edit_reply, name='new_reply'),
    path('<int:issue_pk>/<int:comment_pk>/<int:pk>/edit/', create_or_edit_reply, name='edit_reply'),
    path('search/', search, name='search'),
    path('do_search/', do_search, name='do_search'),
    path('do_search_my/', do_search_my, name='do_search_my'),
    path('report/get_issue_type_json/', get_issue_type_json, name='get_issue_type_json'),
    path('report/get_status_json/', get_status_json, name='get_status_json'),
    path('report/get_bug_upvotes_json/', get_bug_upvotes_json, name='get_bug_upvotes_json'),
    path('report/get_feature_upvotes_json/', get_feature_upvotes_json, name='get_feature_upvotes_json'),
    path('report/', report, name='report'),
    path('<int:pk>/upvote/', upvote, name='upvote'),
    path('<int:pk>/save_issue/', save_issue, name='save_issue'),
    path('<int:pk>/delete_saved_issue/', delete_saved_issue, name='delete_saved_issue'),
]