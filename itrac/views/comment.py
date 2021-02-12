import os
import requests
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
from django.http.response import JsonResponse
from django.template.loader import render_to_string
import json

from itrac.models import Issue, Comment
from itrac.forms import CommentForm
from core.constants import ACTIVE_STATUS


# @login_required()
# def create_comment(request, issue_pk):
#     """
#     Create a view that allows us to create
#     or edit a comment depending if the Comment ID
#     is null or not
#     """
#     issue = get_object_or_404(Issue, pk=issue_pk)

#     if request.method == "POST":
#         form = CommentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.instance.author = request.user
#             form.instance.issue = issue
#             form.save()
#             # notify.send(request.user, recipient=issue.author, verb="added a comment to your Issue: " + issue.title)
#             # messages.success(request, 'Comment Saved!')
#             return redirect('itrac:issue_detail', issue_pk)
#     else:
#         form = CommentForm()

#     return render(request, 'itrac/comment_create.html', {'form': form})


@login_required()
@require_POST
def save_new_comment(request, issue_pk):
    """
    Save a comment created using an ajax POST call
    """
    issue = get_object_or_404(Issue, pk=issue_pk)

    form = CommentForm(request.POST, request.FILES)
    if form.is_valid():
        form.instance.author = request.user
        form.instance.issue = issue
        form.save()

        resp = {
            'status': 'S',         # 'S': successful, 'F': Failed
        }
    else:
        resp = {
            'status': 'F',         # 'S': successful, 'F': Failed
            'error': "error",
        }

    return JsonResponse(resp)


@login_required
@require_POST
def edit_comment(request, issue_pk, pk):
    """
    Create a view that allows us to create
    or edit a comment depending if the Comment ID
    is null or not
    """
    issue = get_object_or_404(Issue, pk=issue_pk)
    comment = get_object_or_404(Comment, pk=pk)

    form = CommentForm(request.POST, request.FILES, instance=comment)
    if form.is_valid():
        form.instance.author = request.user
        form.instance.issue = issue
        form.save()

        resp = {
            'status': 'S',         # 'S': successful, 'F': Failed
        }
    else:
        resp = {
            'status': 'F',         # 'S': successful, 'F': Failed
            'error': "error",
        }

    return JsonResponse(resp)


@login_required
@require_GET
def comment_markdown(request, issue_pk, pk):
    """
     return the raw markdown of the comment field
    """
    comment = get_object_or_404(Comment, pk=pk)
    data = {
        'comment': comment.comment,
    }

    return JsonResponse(data)


@login_required()
def delete_comment(request, issue_pk, pk):
    '''
    Mark the comment as "deleted"
    '''
    comment = get_object_or_404(Comment, pk=pk)
    comment.active_ind = False
    comment.active_status_cd = ACTIVE_STATUS.DELETED
    comment.save()
    return redirect('itrac:issue_detail', issue_pk)
