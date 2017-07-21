from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Wine(models.Model):
	name = models.CharField(max_length=200)
	
	def _unicode_(self):
		return self.name

class Review(models.Model): 
	
	Ratings_Reviews = (
			  (1,'1'),
			  (2,'2'),
			  (3,'3'),
			  (4,'4'),
			  (5,'5'),
	)

# Defining the elements
	wine = models.ForeignKey(Wine)
	pub_date = models.DateTimeField('date_published')
	user_name = models.CharField(max_length=100)
	comment = models.CharField(max_length=200)
	rating = models.IntegerField(choices=Ratings_Reviews)
