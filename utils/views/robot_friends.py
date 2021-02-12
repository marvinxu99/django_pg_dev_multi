from django.shortcuts import render

def robot_friends(request):
    return render(request, 'utils/robot_friends.html')
