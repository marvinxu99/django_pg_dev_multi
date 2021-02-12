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
from ..filters import IssueFilter, IssueFilter_superuser
from .project import DEFAULT_CURRENT_PROJECT


def do_search(request):
    """
    search issues by keyword search on Issue_coded_id first, then Issue.Title to return a list
    of matching Issues and render them to the 'issues.html' template
    """
    # Search Issue.coded_id first. If no hit, then searc issue title
    current_project = request.session.get('current_project', DEFAULT_CURRENT_PROJECT)
    issues = Issue.objects.filter(
            coded_id__iexact=request.GET['q'],
            project__pk = current_project['id'],
        ).order_by('-created_date')
    if(not issues):
        issues = Issue.objects.filter(title__icontains=request.GET['q'],
                project__pk = current_project['id'],
            ).order_by('-created_date')
        filter_name = f'''Issue title contains "{ request.GET['q']}" '''
    else:
        filter_name = f'''Issue contains "{ request.GET['q']}" '''

    issue_count_total = Issue.objects.count()
    issue_count_filter = issues.count()

    context = {
            'issue_count_total': issue_count_total,
            'issue_count_filter': issue_count_filter,
            'issues': issues,
            'filter_name': filter_name,
        }

    return render(request, "itrac/issues.html", context)


@login_required()
def search_issues(request):
    ''' Super users can see all projects while ordinary users can only view current select project.
    '''
    user = request.user
    if user.is_superuser:
        issue_list = Issue.objects.all().order_by('-created_date')
        issue_filter = IssueFilter_superuser(request.GET, queryset=issue_list)
    else:
        current_project = request.session.get('current_project', DEFAULT_CURRENT_PROJECT)
        issue_list = Issue.objects.filter(project__pk = current_project['id']).order_by('-created_date')
        issue_filter = IssueFilter(request.GET, queryset=issue_list)

    context = {
        'filter': issue_filter,
    }

    return render(request, 'itrac/search_issues.html', context)


def do_search_my(request):
    """
    Create a view for searching my issues by keyword search on Issue.Title to return a list
    of matching Issues and render them to the 'myissues.html' template
    """
    user = request.user
    issues = Issue.objects.filter(author=user).filter(title__icontains=request.GET['q'])
    return render(request, "itrac/myissues.html", {"issues": issues})


def generic_search(request):
    keywords=''

    if request.method=='POST': # form was submitted

        keywords = request.POST.get("keywords", "") # <input type="text" name="keywords">
        all_queries = None
        search_fields = ('title','description','coded_id') # change accordingly
        for keyword in keywords.split(' '): # keywords are splitted into words (eg: john science library)
            keyword_query = None
            for field in search_fields:
                each_query = Q(**{field + '__icontains': keyword})
                if not keyword_query:
                    keyword_query = each_query
                else:
                    keyword_query = keyword_query | each_query
                    if not all_queries:
                        all_queries = keyword_query
                    else:
                        all_queries = all_queries & keyword_query

        issues = Issue.objects.filter(all_queries).distinct()
        context = {'issues':issues}
        return render(request, 'search.html', context)

    else: # no data submitted

        context = {}
        return render(request, 'index.html', context)
