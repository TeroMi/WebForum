from django.urls import path
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.allThreads, name='allThreads'),
    path('create', views.createThread, name='createThread')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
