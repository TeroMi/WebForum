from django.urls import path
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from . import views



urlpatterns = [
    path('', views.index, name='home'),
    path('login', auth_views.LoginView.as_view(
                        template_name='login.html'),
                    name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page ='home'), name='logout'),
    path('register', views.register, name='register')
]
