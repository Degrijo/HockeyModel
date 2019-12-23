from django.urls import path

from core.views import start_view, trainer_view, goalkeeper_view, field_player_view


urlpatterns = [
    path(r'start/', start_view, name='start'),
    path(r'trainer/', trainer_view, name='trainer'),
    path(r'goalkeeper/', goalkeeper_view, name='goalkeeper'),
    path(r'field_player/', field_player_view, name='field_player'),
]
