from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from threads.models import Category
import requests

def index(request):
    URL = "http://api.publictransport.tampere.fi/prod"
    PARAMS = {'request': 'stop', 'user': 'teromi', 'pass': 'ta1k4Raspi!', 'code': '3527', 'format': 'jsonp'}
    print(URL)
    print(PARAMS)
    r = requests.get(url=URL, params=PARAMS)
    print(r)
    print(r.json())
    all_categories = Category.objects.all()
    return render(request, 'home.html', {'categories': all_categories})

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})
