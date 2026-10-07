from django.db import models

class Task(models.Model):
	title = models.CharField(max_length=200)
	date = models.CharField(max_length=8)

	def __str__(self):
		return self.title