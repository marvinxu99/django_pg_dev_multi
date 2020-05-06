from django.urls import path

from .views import CalendarView, event_calendar


app_name = 'utils'
urlpatterns = [
    
    path('calendar/', CalendarView.as_view(), name='calendar'),

]
