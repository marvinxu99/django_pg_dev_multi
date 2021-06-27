from django.urls import include, path, re_path

from . import views

app_name = 'kbase'
urlpatterns = [

    path('winn-jumps', views.winn_jumps, name='winn-jumps'),
    path('winn-aboutus', views.winn_aboutus, name='winn-aboutus'),

]
