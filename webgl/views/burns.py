from django.shortcuts import render


def burns_chart(request):
    return render(request, 'webgl/burns.html')