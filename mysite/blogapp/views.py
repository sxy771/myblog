from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')

def blogMain(request):
    return render(request, 'blog/blogMain.html')