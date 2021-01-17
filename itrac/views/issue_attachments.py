from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils import timezone
import json

from ..models import Issue, IssueAttachment
from ..forms import AttachmentAddForm


@login_required
def issue_attachment_add(request, pk):
    data = dict()

    current_project = request.session.get('current_project', { 'project': 'WINN', 'id': 0 })

    issue = get_object_or_404(Issue, pk=pk)
    
    if request.method == 'POST':
        form = AttachmentAddForm(request.POST, request.FILES)
        if form.is_valid():
            attachment = form.save(commit=False)
            attachment.issue = issue
            attachment.uploaded_at = timezone.now()
            attachment.uploaded_by = request.user
            attachment.description = attachment.attachment.name
            attachment.save()

            data['form_is_valid'] = True
            data['html_list'] = render_to_string(
                'includes/partial_issue_details_attachments/partial_issue_details_attachments_list.html', 
                { 
                    'issue': issue,
                    'user': request.user 
                }
            )
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
    else:
        form = AttachmentAddForm()
    
    context = { 
        'form': form,
        'issue': issue,
    }
    data['html_form'] = render_to_string(
        'includes/partial_issue_details_attachments/partial_issue_details_attachment_add_form.html',
        context, 
        request=request
    )

    return JsonResponse(data)


@login_required
def issue_attachment_delete(request, pk, att_pk):
    '''Delete an attachment
    '''
    data = dict()

    issue = get_object_or_404(Issue, pk=pk)

    try:
        attachment = IssueAttachment.objects.filter(issue=issue, pk=att_pk)
        attachment[0].delete()
        
    except:
        pass
    
    data['status'] = 'S'
    data['html_list'] = render_to_string(
        'includes/partial_issue_details_attachments/partial_issue_details_attachments_list.html',
        { 
            'issue': issue,
            'user': request.user 
        },
        
    )
    return JsonResponse(data)