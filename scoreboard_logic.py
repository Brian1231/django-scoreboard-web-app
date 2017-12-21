#Scoreboard
import random
from scoreboard.models import Player, Match
from django.db.models import F
 

def process_data(player1,player2,score1,score2):
	#Create Match
	match = Match(p1=player1, p2=player2, s1=score1, s2=score2)
	match.save()
	
	Player.objects.filter(name=player1).update(played=F("played") + 1)
	Player.objects.filter(name=player2).update(played=F("played") + 1)
		
	Player.objects.filter(name=player1).update(gfor=F("gfor") + score1)
	Player.objects.filter(name=player2).update(gfor=F("gfor") + score2)
		
	Player.objects.filter(name=player1).update(gagainst=F("gagainst") + score2)
	Player.objects.filter(name=player2).update(gagainst=F("gagainst") + score1)
		
	Player.objects.filter(name=player1).update(gdiff=F("gdiff") + score1-score2)
	Player.objects.filter(name=player2).update(gdiff=F("gdiff") + score2-score1)


	#UPDATE PLAYERS ELO RATING
	K_FACTOR = 100
	rating1 = float(Player.objects.filter(name=player1)[0].rating)
	rating2 = float(Player.objects.filter(name=player2)[0].rating)
	
	#value in range 0-1
	expected_score1 = 1/(1+10**((rating2-rating1)/400))
	expected_score2 = 1/(1+10**((rating1-rating2)/400))
	
	if (float(score1) == 0 and float(score2) == 0):
		sa1 = 0.5
		sa2 = 0.5
	else:
		sa1 = ((float(score1))/(float(score1)+ float(score2)))
		sa2 = ((float(score2))/(float(score1)+ float(score2)))
	
	
	new_rating1 = rating1 + K_FACTOR*(sa1 - expected_score1)
	new_rating2 = rating2 + K_FACTOR*(sa2 - expected_score2)

	Player.objects.filter(name=player1).update(rating=str(round(new_rating1)))
	Player.objects.filter(name=player2).update(rating=str(round(new_rating2)))
	
	if(score1>score2):
		Player.objects.filter(name=player1).update(points=F("points") + 3)
		Player.objects.filter(name=player1).update(won=F("won") + 1)
		Player.objects.filter(name=player2).update(lost=F("lost") + 1)
		
	elif(score1<score2):
		Player.objects.filter(name=player2).update(points=F("points") + 3)
		Player.objects.filter(name=player2).update(won=F("won") + 1)
		Player.objects.filter(name=player1).update(lost=F("lost") + 1)
	
	else:
		Player.objects.filter(name=player1).update(points=F("points") + 1)
		Player.objects.filter(name=player2).update(points=F("points") + 1)
		Player.objects.filter(name=player1).update(drawn=F("drawn") + 1)
		Player.objects.filter(name=player2).update(drawn=F("drawn") + 1)
	
	#Player db
#	name = models.CharField(default= 'No Name', max_length=30)
#	rating = models.IntegerField(default=1000)
#	played = models.IntegerField(default=0)
#	points = models.IntegerField(default=0)
#	won = models.IntegerField(default=0)
#	lost = models.IntegerField(default=0)
#	gfor = models.IntegerField(default=0)
#	gagainst = models.IntegerField(default=0)
#	gdiff = models.IntegerField(default=0)
	
	

