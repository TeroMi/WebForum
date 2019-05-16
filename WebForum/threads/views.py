from django.shortcuts import render
from bs4 import BeautifulSoup
from .models import Category, Thread, Content
from .forms import ThreadForm
from django.shortcuts import redirect
from collections import defaultdict
from datetime import datetime
from django.utils import timezone
from django.conf import settings
# Create your views here.


def allThreads(request):
    threads = Thread.objects.all()

    threadsByCategory = defaultdict(list)
    for thread in threads:
        category = thread.Category.Name
        threadsByCategory[category].append(thread)
    return render(request, "AllThreads.html", {'categories': Category.objects.all(),
                                               'threads': threads, 'threadsByCategory': threadsByCategory.items()})


def createThread(request, categoryName):
    category = categoryName
    print(category)
    if request.method == 'POST':
        form = ThreadForm(request.POST, request.FILES)
        if form.is_valid():
            author = request.user
            title = form.cleaned_data['title']
            while title != BeautifulSoup(title, features="lxml").get_text():
                title = BeautifulSoup(title, features="lxml").get_text()
            header = form.cleaned_data['header']
            while header != BeautifulSoup(header, features="lxml").get_text():
                header = BeautifulSoup(header, features="lxml").get_text()
            text = form.cleaned_data['text']
            while text != BeautifulSoup(text, features="lxml").get_text():
                text = BeautifulSoup(text, features="lxml").get_text()
            image = form.cleaned_data['image']
            category = Category.objects.get(Name=category)
            content = Content.createContent(header, text, "", image, "")
            created_thread = Thread.createThread(author, title, content, category)
            return redirect("Thread", threadId=created_thread.id)
    else:
        form = ThreadForm()

    return render(request, "CreateThread.html", {'categories': Category.objects.all(), 'form':form, 'category':category})


def thread(request, threadId):
    current_thread = Thread.objects.get(id=threadId)

    return render(request, "Thread.html", {'categories': Category.objects.all(), 'thread': current_thread})


def categoryThreads(request, categoryName):
    current_category = Category.objects.get(Name=categoryName.capitalize())
    print(current_category)
    category_threads = Thread.objects.filter(Category=current_category)
    return render(request, 'CategoryThreads.html', {'categories': Category.objects.all(), 'threads': category_threads, 'category': current_category.Name})