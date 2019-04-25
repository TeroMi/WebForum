from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from home.forms import SignUpForm

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})
