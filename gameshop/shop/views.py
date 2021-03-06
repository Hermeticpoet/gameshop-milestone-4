from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Game


# Home route function
def index(request):
    if request.method == "GET":
        return HttpResponse("Hello World")


# Games Function calls all games & then accesses the first one
def get_games(request):
    if request.method == 'GET':
        game = Game.objects.all()[0]
        return HttpResponse(str(game.title) + " $" + str(game.price))


# This test function uses the path that calls the 'shop' subfolder to get relevant files
# I have used it multiple times by changing the path to test all my new templates
def get_html(request):
    games = ["Pacman", "GTA", "Hitman"]
    if request.method == 'GET':
        return render(request, 'shop/login.html', {"games": games})
