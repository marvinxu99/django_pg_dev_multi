from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

from ..models import Project
from ..forms import ProjectForm


DEFAULT_CURRENT_PROJECT = { 'project': 'WINN', 'id': 0 }
MAX_RECENT_PROJECT_ITEMS = 4

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
    '''
    Current project
    Recent Projects
    '''
    project = get_object_or_404(Project, pk=pk)

    prev_current = {}
    if 'current_project' in request.session:
        prev_current = request.session.get('current_project')

    # Recents is a list of [recent1, recent2, recent3, recent4 ]
    recent_projects = []
    if 'recent_projects' in request.session:
        recent_projects = request.session.get('recent_projects')

    # Set up current project
    current_project = {
        'title': f'{project.title}({project.code})',
        'id': project.id
    }

    # Remove the current project from recent_projects if it was in them
    if len(recent_projects) > 0:
        try:
            index = recent_projects.index(current_project)
            recent_projects.pop(index)
        except ValueError:
            if len(recent_projects) >= MAX_RECENT_PROJECT_ITEMS:
                del recent_projects[-1]

    if prev_current:
        recent_projects.insert(0, prev_current)

    request.session['current_project'] = current_project
    request.session['recent_projects'] = recent_projects

    return redirect('itrac:filtered_issues_open')
