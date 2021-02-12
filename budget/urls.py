from django.urls import path, re_path

from . import views

app_name = 'budget'

urlpatterns = [
    path('', views.budget_home, name='budget_home'),

]
