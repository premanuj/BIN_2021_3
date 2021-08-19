from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    return HttpResponse("Hello world")

def home(request):
    context = {'greet': "Welcome to my site"}
    return render(request, 'home.html', context)