"""Task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.db import router
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views 

router=DefaultRouter()
router.register('quizzapi',views.QuizzCRUD,basename='quizz')

from django.views.static import serve
from django.conf.urls import url
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin', admin.site.urls),
    path('crud',include(router.urls)),
    path('',views.well,name='welcome_note'),
    path('auth',include('rest_framework.urls',namespace='sessionauth')),
    path('start',views.all_questions,name='start'),
    path('sin_an',views.single_ans,name='sa'),
    path('mca',views.mcq_ans,name='mc'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]

urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)