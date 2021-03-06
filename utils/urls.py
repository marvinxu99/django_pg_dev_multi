from django.urls import path

from . import views
from .views import (CalendarView, event, github, highcharts_clock, oxford,
                    robot_friends)

app_name = 'utils'
urlpatterns = [

    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('event/new', views.event, name='event_new'),
    path('event/edit/<int:event_id>', views.event, name='event_edit'),
    path('robot/', views.robot_friends, name='robot_friends'),
    path('github/', views.github, name='github'),
    path('oxford/', views.oxford, name='oxford'),
    path('solu-calc/', views.solution_calculator, name='solution_calculator'),
    path('highcharts_clock/', views.highcharts_clock, name='highcharts_clock'),
]
