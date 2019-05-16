from django.shortcuts import render
from WebForum.threads.models import Category
# Create your views here.

def index(request):
    all_categories = Category.objects.all()
    render(request, 'base.html', {'categories': all_categories})