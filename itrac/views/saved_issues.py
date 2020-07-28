import os
import requests
from datetime import datetime, timedelta, time
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.conf import settings
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.db.models import Count, Q
from django.core import serializers
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
import json


from ..models import Issue, Comment, Reply, SavedIssue, Tag, ISSUE_STATUS
from ..filters import IssueFilter


@login_required()
def my_saved_issues(request):
    """
    Create a view that will return a list
    of current user's Saved Issues and render them to the 'issues.html' template
    """
    issue_count_total = Issue.objects.count()

    user = request.user
    saved_issues = SavedIssue.objects.filter(user=user).order_by('-created_date')
    issues = []
    for saved_issue in saved_issues:
        issues.append(saved_issue.issue)

    issue_count_filter = saved_issues.count()

    context = {
        'issue_count_total': issue_count_total,
        'issue_count_filter': issue_count_filter,
        'issues': issues,
        'filter_name': "My Favorite Issues"
    }

    return render(request, "itrac/issues.html", context)


@login_required()
def save_issue(request, pk):
    user = request.user
    issue = Issue.objects.get(pk=pk)
    try:
        savedissue = SavedIssue.objects.get(user=user, issue=issue)
    except SavedIssue.DoesNotExist:
        savedissue = None
    if savedissue is None:
        savedissue = SavedIssue(user=user, issue=issue)
        savedissue.save()
        messages.success(request, 'Issue added to your Saved Issues!')
    else:
        messages.error(request, 'Issue already added in your Saved Issues!')
    return redirect('itrac:issue_detail', pk)

@login_required()
def delete_saved_issue(request, pk):
    savedissue = SavedIssue.objects.get(pk=pk)
    savedissue.delete()
    messages.success(request, 'Saved Issue deleted!')
    return redirect('saved_issues')