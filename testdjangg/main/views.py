from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def demand(request):
    return render(request, 'main/page2.html')