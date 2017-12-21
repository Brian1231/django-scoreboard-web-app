#Scoreboard
from django import forms
from scoreboard.models import Player

class PlayerForm(forms.Form):
	SCORE_CHOICES = (('0', '0'),('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),('7', '7'),('8', '8'),('9', '9'))
	
	iquery = Player.objects.values_list('name', flat=True).distinct()
	iquery_choices = [('', 'Choose a name')] + [(name, name) for name in iquery]
	#player1 = forms.ModelChoiceField(queryset=Player.objects.all().values_list('name', flat=True))
	player1 = forms.ChoiceField(choices=iquery_choices, required=False, widget=forms.Select())
	player2 = forms.ChoiceField(choices=iquery_choices, required=False, widget=forms.Select())
	score1 = forms.ChoiceField(widget=forms.Select, choices=SCORE_CHOICES)
	score2 = forms.ChoiceField(widget=forms.Select, choices=SCORE_CHOICES)
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"Password",'type':"password", 'class':"form-control"}))
	
	
class PasswordForm(forms.Form):
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"Password(Disabled)",'type':"password", 'class':"form-control",'readonly':"True"}))
	
	
class FilterForm(forms.Form):
	
	iquery = Player.objects.values_list('name', flat=True).distinct()
	iquery_choices = [('', 'Any')] + [(name, name) for name in iquery]
	player1 = forms.ChoiceField(choices=iquery_choices, required=False, widget=forms.Select())
	player2 = forms.ChoiceField(choices=iquery_choices, required=False, widget=forms.Select())

		
		