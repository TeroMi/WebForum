from django.shortcuts import render

# Create your views here.
def allThreads(request):
    return render(request, "AllThreads.html")
