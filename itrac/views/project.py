from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

from ..models import Project
from ..forms import ProjectForm


DEFAULT_CURRENT_PROJECT = { 'project': 'WINN', 'id': 0 }

@login_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'itrac/project/project_list.html', { 'projects': projects })


@login_required
def project_create(request):
    data = dict()
    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.updated_by = request.user
            project.save()

            data['form_is_valid'] = True
            projects = Project.objects.all()
            data['html_project_list'] = render_to_string('itrac/project/partial_project_list.html', {
                'projects': projects,
                'user': request.user, 
            })
        else:
            data['form_is_valid'] = False
    else:
        form = ProjectForm()

    context = {'form': form}
    data['html_form'] = render_to_string('itrac/project/partial_project_create.html', context, request=request)

    return JsonResponse(data)


@login_required
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    data = dict()

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)

        if form.is_valid():
            project = form.save(commit=False)
            project.updated_by = request.user
            project.save()

            data['form_is_valid'] = True
            projects = Project.objects.all()
            data['html_project_list'] = render_to_string('itrac/project/partial_project_list.html', {
                'projects': projects,
                'user': request.user, 
            })
        else:
            data['form_is_valid'] = False
    else:
        form = ProjectForm(instance=project)

    context = {'form': form}
    data['html_form'] = render_to_string('itrac/project/partial_project_edit.html', context, request=request)

    return JsonResponse(data)


@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    data = dict()

    if request.method == 'POST':
        project.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        projects = Project.objects.all()
        data['html_project_list'] = render_to_string('itrac/project/partial_project_list.html', {
            'projects': projects,
            'user': request.user, 
        })
    else:
        context = {'project': project}
        data['html_form'] = render_to_string('itrac/project/partial_project_delete.html', context, request=request)

    return JsonResponse(data)


@login_required
def set_current_project(request, pk):
    project = get_object_or_404(Project, pk=pk)

    prev_current = request.session.get('current_projects', None)
    prev_recent = request.session.get('recent_projects', None)


    request.session['current_project'] = { 
        'title': project.title, 
        'id': project.id 
    } 

    return redirect('itrac:filtered_issues_open') 

