from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)


#dil

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	author = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.title


#dil
#
class BlogComments(models.Model):
    firstname= models.CharField(max_length=100)
    lastname= models.CharField(max_length=100)
    email= models.EmailField()
    comment= models.TextField(max_length=10000)

    def __str__(self):
    	return self.firstname
