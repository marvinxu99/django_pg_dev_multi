import os
import requests
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone


from ..models import Issue, Comment
from ..forms import CommentForm


@login_required()
def create_comment(request, issue_pk):
    """
    Create a view that allows us to create
    or edit a comment depending if the Comment ID
    is null or not
    """
    issue = get_object_or_404(Issue, pk=issue_pk)
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.instance.issue = issue
            form.save()
            # notify.send(request.user, recipient=issue.author, verb="added a comment to your Issue: " + issue.title)
            # messages.success(request, 'Comment Saved!')
            return redirect('itrac:issue_detail', issue_pk)
    else:
        form = CommentForm()
        
    return render(request, 'itrac/comment_create.html', {'form': form})

@login_required()
def edit_comment(request, issue_pk, pk):
    """
    Create a view that allows us to create
    or edit a comment depending if the Comment ID
    is null or not
    """
    issue = get_object_or_404(Issue, pk=issue_pk)
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            form.instance.author = request.user
            form.instance.issue = issue
            form.save()
            # notify.send(request.user, recipient=issue.author, verb="added a comment to your Issue: " + issue.title)
            # messages.success(request, 'Comment Saved!')
            return redirect('itrac:issue_detail', issue_pk)
    else:
        form = CommentForm(instance=comment)
        
    return render(request, 'itrac/comment_edit.html', {'form': form})

@login_required()
def delete_comment(request, issue_pk, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('itrac:issue_detail', issue_pk)
