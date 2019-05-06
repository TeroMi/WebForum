from django.urls import path
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('', views.allThreads, name='home')
]
