from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from bs4 import BeautifulSoup
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from .models import Category, Thread, Content, Comment
from .forms import ThreadForm
from django.shortcuts import redirect
from collections import defaultdict
from datetime import datetime
from django.utils import timezone
from django.conf import settings
# Create your views here.


def allThreads(request):
    threads = Thread.objects.all()
    categories = Category.objects.all()
    threadsByCategory = defaultdict(list)

    for category in categories:
        if threads:
            for thread in threads:
                if category.Name == thread.Category.Name:
                    threadsByCategory[category.Name].append(thread)
                else:
                    print(category.Name)
                    threadsByCategory[category.Name] = []

    print(threadsByCategory)
    return render(request, "AllThreads.html", {'categories': Category.objects.all(),
                                               'threads': threads, 'threadsByCategory': threadsByCategory.items()})

@login_required
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
    comments = Comment.objects.filter(Thread__id=threadId)
    return render(request, "Thread.html", {'categories': Category.objects.all(), 'thread': current_thread, 'comments': set(comments) })


@login_required
def upvoteThread(request, threadId):
    thr = Thread.objects.get(id=threadId)
    loggedUser = request.user

    if thr.UpVoters.filter(id=loggedUser.id):
        thr.Upvotes -= 1
        thr.UpVoters.remove(loggedUser)
        thr.save()
    elif thr.DownVoters.filter(id=loggedUser.id):
        thr.Downvotes -= 1
        thr.DownVoters.remove(loggedUser)
        thr.Upvotes += 1
        thr.UpVoters.add(loggedUser)
        thr.save()
    else:
        thr.Upvotes += 1
        thr.UpVoters.add(loggedUser)
        thr.save()
    return redirect('/threads/{}'.format(threadId))

@login_required
def downvoteThread(request, threadId):
    thr = Thread.objects.get(id=threadId)
    loggedUser = request.user

    if thr.DownVoters.filter(id=loggedUser.id):
        thr.Downvotes -= 1
        thr.DownVoters.remove(loggedUser)
        thr.save()
    elif thr.UpVoters.filter(id=loggedUser.id):
        thr.Upvotes -= 1
        thr.UpVoters.remove(loggedUser)
        thr.Downvotes += 1
        thr.DownVoters.add(loggedUser)
        thr.save()
    else:
        thr.Downvotes += 1
        thr.DownVoters.add(loggedUser)
        thr.save()
    return redirect('/threads/{}'.format(threadId))


def categoryThreads(request, categoryName):
    current_category = Category.objects.get(Name=categoryName.capitalize())
    category_threads = Thread.objects.filter(Category=current_category)
    return render(request, 'CategoryThreads.html', {'categories': Category.objects.all(), 'threads': category_threads, 'category': current_category.Name})

def comment(request):
    commentText = request.POST["comment"]
    while commentText != BeautifulSoup(commentText, features="lxml").get_text():
        commentText = BeautifulSoup(commentText, features="lxml").get_text()
    url = request.POST["url"]
    thread = Thread.objects.get(id=request.POST["id"])
    comment = Comment.createComment(request.user, commentText, thread)
    return redirect(url)