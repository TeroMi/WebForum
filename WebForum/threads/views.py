from django.shortcuts import render
from bs4 import BeautifulSoup
from .models import Category, Thread, Content
from threads.forms import ThreadForm
from datetime import datetime
from django.utils import timezone
# Create your views here.
def allThreads(request):
    #catt = Category.objects.createCategory("Motorsport")
    #cat = Category.create("Gaming")
    threads = Thread.objects.all()
    Testi = "<<<div>div>a onmouseover='alert(1)' onclick='alert(1)'><h1<<div><div></div>HAH HOH HEH</h1></a>"
    asd="<div onmouseover='alert(1)'>asd</script>"
    while Testi != BeautifulSoup(Testi, features="lxml").get_text():
        print(Testi)
        Testi = BeautifulSoup(Testi, features="lxml").get_text()

    return render(request, "AllThreads.html", {'categories':Category.objects.all(), 'testi':asd, 'threads':threads})

def createThread(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST, request.FILES)
        if form.is_valid():
            createDate = timezone.now
            author = request.user
            title = request.POST['title']
            header = request.POST['header']
            text = request.POST['text']
            image = request.FILES['image']
            category = Category.objects.get(Name="Sports")
            content = Content.createContent(header, text, "", image, "")
            thread = Thread.createThread(author, title, content, category)
            print(content.Header)
            print(thread.Title)

    else:
        form = ThreadForm()
    return render(request, "CreateThread.html", {'form':form})
