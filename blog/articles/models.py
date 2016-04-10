from django.db import models
from django.core.urlresolvers import reverse


# Create your models here. 

class CategoryName(models.Model):
	title = models.CharField(max_length = 200)

	def __unicode__(self):
	    return(self.title)

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	category = models.ForeignKey('CategoryName')
	title = models.CharField( max_length = 200)
	text = models.TextField()
	created_date = models.DateTimeField(auto_now_add = True)


	def __unicode__(self):
		return(self.title)

	def get_absolute_url(self):
		return reverse ("post_read", kwargs = {'id': self.id})

	class Meta:
		ordering = ['-created_date']
			

class Comment(models.Model):
	name = models.CharField(max_length = 50)
	email = models.EmailField (max_length = 75)
	text = models.TextField()
	post = models.ForeignKey ('Post')
	created = models.DateTimeField (auto_now_add = True)

	def __unicode__():
	 	return self.text
