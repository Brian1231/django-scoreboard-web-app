#Scoreboard
from django.shortcuts import render
from . import scoreboard_logic

from scoreboard.forms import PlayerForm, PasswordForm, FilterForm
from scoreboard.models import Player, Match
from django.views.generic import ListView, DetailView, TemplateView
from itertools import chain
from django.db.models import Q

def index(request):
	return render(request, 'scoreboard/home.html')
	
	
def scoreboard(request):
	return render(request, 'scoreboard/scoreboard.html', {'data':scoreboard_logic.content})

#Home Page	
class HomeView(TemplateView):

	template_name="scoreboard/home.html"
	
	def get(self, request):
		form = PasswordForm()
		return render(request, self.template_name, {'form':form})
		
	def post(self, request):
		#form = PasswordForm(request.POST)
		form = PlayerForm()
		#return render(request, "scoreboard/scoreboard.html", {'form':form, 'object_list':Player.objects.all().order_by("-points")})
		return render('/scoreboard', self.template_name, {'form':form})
		
#View to render scoreboard page
class ScoreboardView(TemplateView):
	template_name="scoreboard/scoreboard.html"
	
	queryset=Player.objects.all().order_by("points")
	
	def get(self, request):
		form = PlayerForm()
		return render(request, self.template_name, {'form':form, 'object_list':Player.objects.all().order_by("-rating")})
		
	#If POST received from League
	def post(self, request):
		form = PlayerForm(request.POST)
		if form.is_valid():
			player1 = form.cleaned_data['player1']
			player2 = form.cleaned_data['player2']
			score1 = form.cleaned_data['score1']
			score2 = form.cleaned_data['score2']
			password = form.cleaned_data['password']
			
			if player1 != player2 and player1 != '' and player2 != '' and password == '':
				scoreboard_logic.process_data(player1, player2, score1, score2)
		
		##DELETE ME
		#matches=Match.objects.all()
		#for match in matches:
		#	scoreboard_logic.process_data(match.p1, match.p2, match.s1, match.s2)
		
		#Player.objects.filter(name='Brian').update(rating = 1000,played = 0,points = 0,won = 0,lost = 0,gfor = 0,gagainst = 0,gdiff = 0)
		#Player.objects.filter(name='Dean').update(rating = 1000,played = 0,points = 0,won = 0,lost = 0,gfor = 0,gagainst = 0,gdiff = 0)
		#Player.objects.filter(name='Dara').update(rating = 1000,played = 0,points = 0,won = 0,lost = 0,gfor = 0,gagainst = 0,gdiff = 0)
		#Player.objects.filter(name='Paul').update(rating = 1000,played = 0,points = 0,won = 0,lost = 0,gfor = 0,gagainst = 0,gdiff = 0)
		#Player.objects.filter(name='Blaine').update(rating = 1000,played = 0,points = 0,won = 0,lost = 0,gfor = 0,gagainst = 0,gdiff = 0)
		#Player.objects.filter(name='Conor').update(rating = 1000,played = 0,points = 0,won = 0,lost = 0,gfor = 0,gagainst = 0,gdiff = 0)
		##DELETE ME
		
		
		form = PlayerForm()
		args = {'form':form, 'object_list':Player.objects.all().order_by("-rating")}
		return render(request, self.template_name, args)
	
#View to render scoreboard page
class MatchesView(TemplateView):
	template_name="scoreboard/matches.html"
	
	matches=Match.objects.all()
	
	def get(self, request):
		form = FilterForm()
		return render(request, self.template_name, {'object_list':list(reversed(Match.objects.all())), 'form':form})
		
	def post(self, request):
		form = FilterForm(request.POST)
		args = {}
		if form.is_valid():
			player1 = form.cleaned_data['player1']
			player2 = form.cleaned_data['player2']
			print(player1)
			if player1 != player2 or (player1 == '' and player2 == ''):
			#filter(Q(income__gte=5000) | Q(income__isnull=True))
				if player1 == '' and player2 == '':
					args = {'form':form, 'object_list':list(reversed(Match.objects.all()))}
				elif player1 == '':
					args = {'form':form, 'object_list':list(reversed(Match.objects.filter(Q(p2=player2) | Q(p1=player2))))}
				elif player2 == '':
					args = {'form':form, 'object_list':list(reversed(Match.objects.filter(Q(p2=player1) | Q(p1=player1))))}
				else:
					args = {'form':form, 'object_list':list(reversed(Match.objects.filter(Q(p1=player1, p2=player2) | Q(p1=player2, p2=player1))))}
			else:
				form = FilterForm()
				args = {'form':form, 'object_list':list(reversed(Match.objects.all()))}
		else:
			args = {'form':form, 'object_list':list(reversed(Match.objects.all()))}
		
		return render(request, self.template_name, args)
		
	
		