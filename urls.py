##Scoreboard
from django.urls import path
from . import views
from django.views.generic import ListView, DetailView
from scoreboard.models import Player
from scoreboard.views import ScoreboardView, HomeView, MatchesView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
	path('matches/', MatchesView.as_view(), name='matches'),
	#path('scoreboard/', views.scoreboard, name='scoreboard')
	path('scoreboard/', ScoreboardView.as_view(), name='scoreboard')
	]