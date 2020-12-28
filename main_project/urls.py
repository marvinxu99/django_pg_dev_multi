"""main_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

from core import views as core_views
# import notifications.urls

urlpatterns = [
    path('', core_views.index, name='home'),
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('boards/', include('boards.urls')),
    path('accounts/', include('accounts.urls')),
    
    path('catalog/', include('catalog.urls')),
    #path('', RedirectView.as_view(url='catalog/', permanent=True)),

    path('core/', include('core.urls')),
    path('kbase/', include('kbase.urls')),
    path('posts/', include('posts.urls')),
    
    path('winter_winnpy/', core_views.winter_winnpy, name='winter_winnpy'),
    path('winter_univer/', core_views.winter_univer, name='winter_univer'),
    path('face_recognition/', core_views.face_recognition, name='face_recognition'),

    path('utils/', include('utils.urls')),
    path('itrac/', include('itrac.urls')),
    path('webgl/', include('webgl.urls')),
    
    path('payments/', include('payments.urls')),
    path('budget/', include('budget.urls')),
    path('scan_n_pay/', include('scan_n_pay.urls')),
    path('books/', include('books.urls')),

    path('shop/', include('shop.urls')),

    path('i18n/', include('django.conf.urls.i18n')),

]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)