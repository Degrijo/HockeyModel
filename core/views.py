from django.shortcuts import render
from django.urls import reverse_lazy

from random import choice

from core.models import Main, Creator, Player

main = Main()
creator = Creator()
current_player = Player('Yarik', 'Yatsenko', 0, str(1.0))


def start_view(request):
    global creator, main
    main.main(creator)
    context = {'title': 'start', 'header': 'Start'}
    return render(request, 'core/start_page.html', context=context)


def trainer_view(request):
    context = {'title': 'trainer', 'header': 'Trainer', 'scope': '0 : 0', 'time': '13:37', }
    return render(request, 'core/trainer_page.html', context=context)


def goalkeeper_view(request):
    context = {'title': 'goalkeeper', 'header': 'Goalkeeper', 'scope': '0 : 0', 'time': '13:37'}
    return render(request, 'core/goalkeeper_page.html', context=context)


def field_player_view(request):
    global current_player, creator
    current_player = choice(creator.team1.composition)
    context = {'title': 'field player', 'header': 'Field Player', 'scope': f'{creator.game.goals1} : {creator.game.goals2}', 'time': '13:37'}
    return render(request, 'core/field_player_page.html', context=context)
