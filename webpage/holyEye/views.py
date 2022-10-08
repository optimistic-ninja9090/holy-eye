from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'holyEye/home.html')

def about(request):
    return render(request, 'holyEye/about.html')

def page1(request):
    return render(request, 'holyEye/page1.html')

def page2(request):
    return render(request, 'holyEye/page2.html')

def page3(request):
    return render(request, 'holyEye/page3.html')