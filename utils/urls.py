from django.urls import path

from .views import CalendarView, event_calendar


app_name = 'utils'
urlpatterns = [
    
    path('event-calendar/', CalendarView.as_view(), name='event-calendar'),

]
