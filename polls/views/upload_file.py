import os

from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from polls.forms import UploadFileForm


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file_name'])
            print('file uploaded')
            return HttpResponseRedirect(reverse('polls:upload_success'))
    else:
        form = UploadFileForm()

    context = {
            'domain': settings.DOMAIN,
            'form': form,
        }
    return render(request, 'polls/upload_file.html', context)


def handle_uploaded_file(f):
    # f_name = 'uploaded_file' + datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + '.txt'
    # f_name = 'uploaded_file.txt'
    f_name = f.name
    uploaded_file = os.path.join(settings.FILE_UPLOAD_DIR, f_name)

    with open(uploaded_file, 'wb+') as f_uploaded:
        for chunk in f.chunks():
            f_uploaded.write(chunk)


def upload_success(request):
    context = {
            'domain': settings.DOMAIN,
            'msg_text': "The file was uploaded successfully!",
        }
    return render(request, 'polls/successful.html', context)
