from django.urls import path

from .views import CalendarView, event, robot_friends, github, oxford


app_name = 'utils'
urlpatterns = [
    
    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('event/new', event, name='event_new'),
    path('event/edit/<int:event_id>', event, name='event_edit'),
    path('robot/', robot_friends, name='robot_friends'),
    path('github/', github, name='github'),
    path('oxford/', oxford, name='oxford'),
]
