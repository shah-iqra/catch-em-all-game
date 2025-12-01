from django.shortcuts import render

def home(request):
    # আগে home.html → এখন index.html
    return render(request, "game/index.html")  

def game(request):
    # আগে index.html → এখন game.html
    return render(request, "game/game.html")   # game page
