from django.shortcuts import render, redirect


def index(request):
    return render(request, 'core/index.html')

def winter_winnpy(request):
    return redirect('http://winterai.herokuapp.com')

def winter_univer(request):
    return redirect('http://winnpy.pythonanywhere.com')

def face_recognition(request):
    return redirect('http://winter-x-face.herokuapp.com')
