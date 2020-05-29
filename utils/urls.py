from django.urls import path

from .views import CalendarView, event, i_robot


app_name = 'utils'
urlpatterns = [
    
    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('event/new', event, name='event_new'),
    path('event/edit/<int:event_id>', event, name='event_edit'),
    path('robot/', i_robot, name='i_robot'),
]
