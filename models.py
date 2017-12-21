from django.db import models

#Table
class Player(models.Model):
	#Columns
	name = models.CharField(default= 'No Name', max_length=30)
	rating = models.IntegerField(default=1000)
	played = models.IntegerField(default=0)
	points = models.IntegerField(default=0)
	won = models.IntegerField(default=0)
	lost = models.IntegerField(default=0)
	drawn = models.IntegerField(default=0)
	gfor = models.IntegerField(default=0)
	gagainst = models.IntegerField(default=0)
	gdiff = models.IntegerField(default=0)

	def __str__(self):
		return self.name
		
class Match(models.Model):
	#Columns
	p1 = models.CharField(default= 'No Name', max_length=30)
	p2 = models.CharField(default= 'No Name', max_length=30)
	s1 = models.IntegerField(default=0)
	s2 = models.IntegerField(default=0)


