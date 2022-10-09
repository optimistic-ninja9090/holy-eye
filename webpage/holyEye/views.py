from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "main/home.html")

def about(request):
    return render(request, "main/about.html")

def page1(request):
    return render(request, "main/page1.html")

def page2(request):
    return render(request, "main/page2.html")

def page3(request):
    return render(request, "main/page3.html")