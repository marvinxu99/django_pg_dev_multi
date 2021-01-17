from django.urls import path
from . import views 

app_name = 'itrac'

urlpatterns = [
    path('', views.my_in_progress_issues, name='my_in_progress_issues'),
    path('my_issues/', views.issues_reported_by_me, name='issues_reported_by_me'),
    path('my_issues2/', views.issues_reported_by_me2, name='issues_reported_by_me2'),
    path('saved_issues/', views.my_saved_issues, name='my_saved_issues'),

    path('issues/all/', views.filtered_issues, {'filter': 'all'}, name='filtered_issues_all'),
    path('issues/open/', views.filtered_issues, {'filter': 'open'}, name='filtered_issues_open'),

    path('notifications/', views.my_notifications, name='my_notifications'),
    path('issue/<int:pk>/', views.issue_detail, name='issue_detail'),
    path('issue/<int:pk>/partial', views.issue_detail_partial, name='issue_detail_partial'),
    path('issue/new/', views.create_issue, name='new_issue'),
    path('issue/<int:pk>/clone/', views.clone_issue, name='clone_issue'),
    path('issue/<int:pk>/edit/', views.edit_issue, name='edit_issue'),
    path('issue/<int:pk>/desc_markdown/', views.description_raw_markdown, name='description_raw_markdown'),
    path('issue/<int:pk>/desc_html/', views.description_as_html, name='description_as_html'),
    path('issue/<int:pk>/desc_edit/', views.edit_description, name='edit_description'),
    path('issue/<int:pk>/change_status/', views.issue_change_status, name='change_status'),
    path('issue/<int:pk>/assingee/users', views.change_assignee_users, name='change_assignee_users'), 
    path('issue/<int:pk>/assingee/change/<int:user_pk>', views.change_assignee_change, name='change_assignee_change'),

    path('issue/<int:pk>/save_issue/', views.save_issue_favourite, name='save_issue_favourite'),

    path('issue/<int:pk>/upvote/', views.upvote, name='upvote'),
    path('issue/<int:pk>/purchasevote/', views.purchase_vote, name='purchase_vote'),

    # example url: /itrac/issue/tag/?tag=test%20test
    path('issue/tag/', views.issues_with_tag, name='issues_with_tag'),

    path('issue/<int:pk>/tags/edit', views.edit_issue_tags, name='edit_issue_tags'),
    path('issue/<int:pk>/tags/list', views.partial_issue_tags_list, name='partial_issue_tags_list'),
    path('issue/<int:pk>/tag/<int:tag_pk>/delete', views.issue_delete_tag, name='issue_delete_tag'),
    path('issue/<int:pk>/tag/<int:tag_pk>/add', views.issue_add_tag, name='issue_add_tag'),
    path('issue/<int:pk>/tag/add_new', views.issue_add_net_new_tag, name='issue_add_net_new_tag'),

    path('issue/<int:pk>/attachment/add', views.issue_attachment_add, name='issue_attachment_add'),
    path('issue/<int:pk>/attchment/<int:att_pk>/delete', views.issue_attachment_delete, name='issue_attachment_delete'),

    path('issue/<int:pk>/link/add', views.issue_links_add_issue, name='issue_links_add_issue'),
    path('issue/<int:pk>/link/<int:linked_pk>/delete', views.issue_links_delete_issue, name='issue_links_delete_issue'),

    path('comment/<int:issue_pk>/save_new/', views.save_new_comment, name='save_new_comment'),
    path('comment/<int:issue_pk>/<int:pk>/edit/', views.edit_comment, name='edit_comment'),
    path('comment/<int:issue_pk>/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
    path('comment/<int:issue_pk>/<int:pk>/markdown/', views.comment_markdown, name='comment_markdown'),

    path('project/', views.project_list, name='project_list'),
    path('project/create/', views.project_create, name='project_create'),
    path('project/edit/<int:pk>', views.project_edit, name='project_edit'),
    path('project/delete/<int:pk>', views.project_delete, name='project_delete'),
    path('project/set_current/<int:pk>', views.set_current_project, name='set_current_project'),

    path('tag/', views.tag_list, name='tag_list'),
    path('tag/create/', views.tag_create, name='tag_create'),
    path('tag/edit/<int:pk>', views.tag_edit, name='tag_edit'),
    path('tag/delete/<int:pk>', views.tag_delete, name='tag_delete'),

    path('search/', views.search_issues, name='search'),
    path('do_search/', views.do_search, name='do_search'),
    path('do_search_my/', views.do_search_my, name='do_search_my'),
    
    path('report/get_issue_type_json/', views.get_issue_type_json, name='get_issue_type_json'),
    path('report/get_status_json/', views.get_status_json, name='get_status_json'),
    path('report/get_bug_upvotes_json/', views.get_bug_upvotes_json, name='get_bug_upvotes_json'),
    path('report/get_feature_upvotes_json/', views.get_feature_upvotes_json, name='get_feature_upvotes_json'),
    path('report/', views.report, name='report'),

    path('report/resolved_by_days', views.rpt_resolved_by_days, name='rpt_resolved_by_days'),
    path('report/issues_by_type', views.rpt_issues_by_type, name='rpt_issues_by_type'),
    path('report/issues_by_status', views.rpt_issues_by_status, name='rpt_issues_by_status'),

]