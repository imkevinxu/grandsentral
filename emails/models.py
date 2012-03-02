from django.db import models
from django.contrib import admin

class Email(models.Model):
	from_name 		= models.CharField(max_length=50)
	from_email		= models.CharField(max_length=50)
	to_name   		= models.CharField(max_length=50)
	to_email  		= models.CharField(max_length=50)
	subject   		= models.CharField(max_length=100)
	body      		= models.TextField()

	date			= models.DateTimeField(auto_now_add=True)
	uid 			= models.CharField(max_length=16, primary_key=True, unique=True)
	sent 			= models.BooleanField()

	def __unicode__(self):
		return u'%s -> %s [%s]' % (self.from_name, self.to_name, self.subject)

class Confirm(models.Model):
	uid				= models.CharField(max_length=16, primary_key=True, unique=True)
	date			= models.DateTimeField(auto_now_add=True)
	emails			= models.ManyToManyField("Email")

	def __unicode__(self):
		return u'Hash: %s' % (self.uid)