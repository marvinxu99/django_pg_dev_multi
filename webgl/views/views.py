from django.shortcuts import render

# Create your views here.
def texture(request):
    return render(request, 'webgl/texture.html')

def triangle_colour(request):
    return render(request, 'webgl/triangle_colour.html')

def animation(request):
    return render(request, 'webgl/webgl_animation.html')
