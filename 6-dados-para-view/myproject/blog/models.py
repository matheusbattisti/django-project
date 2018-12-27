from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

	POST_STATUS = (
		('active', 'Ativo'),
		('draft', 'Rascunho')
	)
	title = models.CharField(max_length=200)
	body = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)
	status = models.CharField(max_length=15, choices=POST_STATUS)

	def __str__(self):
	    return self.title