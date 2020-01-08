from django.shortcuts import render
from django.http import HttpResponse


# Home route function
def index(request):
    if request.method == "GET":
        return HttpResponse("Hello World")


# Games Function calls all games & then accesses the first one
def get_games(request):
    if request.method == 'GET':
        game = Game.objects.all()[0]
        return HttpResponse(str(game.title) + " $" + str(game.price))


