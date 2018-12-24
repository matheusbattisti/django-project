from django.db import models

class Post(models.Model):

	POST_STATUS = (
		('Ativo', 'active'),
		('Rascunho', 'draft')
	)
	title = models.CharField(max_length=200)
	body = models.TextField()
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)
	status = models.CharField(max_length=1, choices=POST_STATUS)


