from django.shortcuts import render


def start_view(request):
    context = {'title': 'start', 'header': 'Start'}
    return render(request, 'core/start_page.html', context=context)


def trainer_view(request):
    context = {'title': 'trainer', 'header': 'Trainer', 'scope': '0 : 0', 'time': '13:37'}
    return render(request, 'core/trainer_page.html', context=context)


def goalkeeper_view(request):
    context = {'title': 'goalkeeper', 'header': 'Goalkeeper', 'scope': '0 : 0', 'time': '13:37'}
    return render(request, 'core/goalkeeper_page.html', context=context)


def field_player_view(request):
    context = {'title': 'field player', 'header': 'Field Player', 'scope': '0 : 0', 'time': '13:37'}
    return render(request, 'core/field_player_page.html', context=context)
