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


# This test function uses the path that calls the 'shop' subfolder to get index.html file
# I then altered this to point to the base.html file
def get_html(request):
    if request.method == 'GET':
        return render(request, 'shop/base.html')
