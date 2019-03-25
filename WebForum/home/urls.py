from django.urls import path
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
#from home.views



urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home')
]
