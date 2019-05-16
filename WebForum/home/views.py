from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from threads.models import Category

def index(request):
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
