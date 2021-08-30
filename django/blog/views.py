from django.shortcuts import render, get_object_or_404

def home(req):
    return render(req, "home.html")