from django.shortcuts import render

def home(request):
    return render(request, "game/home.html")

def index(request):
    return render(request, "game/index.html")   # game page
