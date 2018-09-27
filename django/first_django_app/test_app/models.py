from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=200)
	pages = models.IntegerField()
	author = models.CharField(max_length=100)
	award_winning = models.BooleanField(default=False)

	def __str__(self):
		return 'Bob\'s book: ' + self.title + ' has ' + str(self.pages) + ' pages' 
