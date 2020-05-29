from django.shortcuts import render

def i_robot(request):
    return render(request, 'utils/i_robot.html')