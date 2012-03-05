from django.db import models
from django.contrib import admin

class Email(models.Model):
	from_name 		= models.CharField(max_length=50)
	from_email		= models.EmailField()
	to_name   		= models.CharField(max_length=50)
	to_email  		= models.EmailField()
	subject   		= models.CharField(max_length=100)
	body      		= models.TextField()

	date			= models.DateTimeField(auto_now_add=True)
	uid 			= models.CharField(max_length=32, primary_key=True)
	sent 			= models.BooleanField()

	def __unicode__(self):
		return u'%s -> %s [%s]' % (self.from_name, self.to_name, self.subject)

class Confirm(models.Model):
	uid				= models.CharField(max_length=32, primary_key=True)
	date			= models.DateTimeField(auto_now_add=True)
	emails			= models.ManyToManyField("Email")
	confirmed		= models.BooleanField()

	def __unicode__(self):
		return u'Hash: %s' % (self.uid)