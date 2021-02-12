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


from ..models import Issue, Comment, SavedIssue, Tag, ISSUE_STATUS, ISSUE_TYPE
from ..filters import IssueFilter


@login_required
def rpt_resolved_by_days(request):
    today = datetime.now().date()
    tomorrow = today + timedelta(1)
    today_start = datetime.combine(today, time())
    today_end = datetime.combine(tomorrow, time())
    completed_daily = Issue.objects.filter(resolved_date__gte=today_start).filter(resolved_date__lt=today_end).count()

    this_week_start = datetime.combine(today - timedelta(7), time())
    completed_weekly = Issue.objects.filter(resolved_date__gte=this_week_start).filter(resolved_date__lt=today_end).count()

    this_month_start = datetime.combine(today - timedelta(28), time())
    completed_monthly = Issue.objects.filter(resolved_date__gte=this_month_start).filter(resolved_date__lt=today_end).count()
    print(completed_daily)

    context = {
        'completed_daily': str(completed_daily),
        'completed_weekly': str(completed_weekly),
        'completed_monthly': str(completed_monthly)
    }
    return render(request, "itrac/rpt_resolved_by_days.html", context)


@login_required
def report(request):
    today = datetime.now().date()
    tomorrow = today + timedelta(1)
    today_start = datetime.combine(today, time())
    today_end = datetime.combine(tomorrow, time())
    completed_daily = Issue.objects.filter(resolved_date__gte=today_start).filter(resolved_date__lt=today_end).count()

    this_week_start = datetime.combine(today - timedelta(7), time())
    completed_weekly = Issue.objects.filter(resolved_date__gte=this_week_start).filter(resolved_date__lt=today_end).count()

    this_month_start = datetime.combine(today - timedelta(28), time())
    completed_monthly = Issue.objects.filter(resolved_date__gte=this_month_start).filter(resolved_date__lt=today_end).count()
    print(completed_daily)

    context = {
        'completed_daily': str(completed_daily),
        'completed_weekly': str(completed_weekly),
        'completed_monthly': str(completed_monthly)
    }

    return render(request, "itrac/report.html", context)



@login_required
def rpt_issues_by_type(request):
    return render(request, "itrac/rpt_issues_by_type.html")


@login_required
def rpt_issues_by_status(request):
    return render(request, "itrac/rpt_issues_by_status.html")


@login_required
def get_issue_type_json(request):
    dataset = Issue.objects \
        .values('issue_type') \
        .exclude(issue_type='') \
        .annotate(total=Count('issue_type')) \
        .order_by('issue_type')

    # get the issue type display
    # https://docs.djangoproject.com/en/3.0/ref/models/fields/
    for i in range(len(dataset)):
        dataset[i]['issue_type_display'] = ISSUE_TYPE(dataset[i]['issue_type']).label

    # Highchart.js configure
    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'Issue Type'},
        'xAxis': {'type': "category"},
        'series': [{
            'name': 'Issues',
            'data': list(map(lambda row: {'name': [row['issue_type_display']], 'y': row['total']}, dataset))
        }]
    }

    return JsonResponse(chart)


@login_required
def get_status_json(request):
    dataset = Issue.objects \
        .values('status') \
        .exclude(status='') \
        .annotate(total=Count('status')) \
        .order_by('status')

    # get the issue status display
    # https://docs.djangoproject.com/en/3.0/ref/models/fields/
    for i in range(len(dataset)):
        dataset[i]['status_display'] = ISSUE_STATUS(dataset[i]['status']).label

    chart = {
        'chart': {'type': 'pie'},
        'title': {'text': 'Issue Status'},
        'series': [{
            'name': 'Issues',
            'data': list(map(lambda row: {'name': [row['status_display']], 'y': row['total']}, dataset))
        }]
    }

    return JsonResponse(chart)

@login_required
def get_bug_upvotes_json(request):
    dataset = Issue.objects \
        .filter(issue_type='BUG') \
        .values('upvotes', 'title') \
        .exclude(upvotes=0) \
        .order_by('upvotes')

    chart = {
        'chart': {'type': 'pie'},
        'title': {'text': 'Top Bug Upvotes'},
        'series': [{
            'name': 'Issue Upvotes',
            'data': list(map(lambda row: {'name': [row['title']], 'y': row['upvotes']}, dataset))
        }]
    }

    return JsonResponse(chart)


@login_required
def get_feature_upvotes_json(request):
    dataset = Issue.objects \
    .filter(issue_type='FEATURE') \
    .values('upvotes', 'title') \
    .exclude(upvotes=0) \
    .order_by('upvotes')

    chart = {
        'chart': {'type': 'pie'},
        'title': {'text': 'Top Feature Upvotes'},
        'series': [{
            'name': 'Issue Upvotes',
            'data': list(map(lambda row: {'name': [row['title']], 'y': row['upvotes']}, dataset))
        }]
    }

    return JsonResponse(chart)
