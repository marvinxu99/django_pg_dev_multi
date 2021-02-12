from django.urls import path

from . import views


app_name = 'webgl'
urlpatterns = [

    path('texture/', views.texture, name='texture'),
    path('triangle-colour/', views.triangle_colour, name='triangle-colour'),
    path('animation/', views.animation, name='animation'),
    path('burns-chart/', views.burns_chart, name='burns-chart'),

]
