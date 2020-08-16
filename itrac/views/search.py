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


from ..models import Issue, Comment, SavedIssue, Tag, ISSUE_STATUS
from ..filters import IssueFilter


def do_search_my(request):
    """
    Create a view for searching my issues by keyword search on Issue.Title to return a list
    of matching Issues and render them to the 'myissues.html' template
    """
    user = request.user
    issues = Issue.objects.filter(author=user).filter(title__icontains=request.GET['q'])
    return render(request, "itrac/myissues.html", {"issues": issues})


def do_search(request):
    """
    Create a view for searching all issues by keyword search on Issue.Title to return a list
    of matching Issues and render them to the 'issues.html' template
    """
    issues = Issue.objects.filter(title__icontains=request.GET['q'])

    issue_count_total = Issue.objects.count()
    issue_count_filter = issues.count()

    filter_name = f'''Issue title contains "{ request.GET['q']}" '''

    context = {
            'issue_count_total': issue_count_total,
            'issue_count_filter': issue_count_filter,
            'issues': issues,
            'filter_name': filter_name,
        }

    return render(request, "itrac/issues.html", context)

@login_required()
def search(request):
    issue_list = Issue.objects.all()
    issue_filter = IssueFilter(request.GET, queryset=issue_list)
    issue_count = issue_filter.qs.count()
    context = {
        'filter': issue_filter,
        'issue_count': issue_count,
    }
    return render(request, 'itrac/search_issues.html', context)
