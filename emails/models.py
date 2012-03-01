from django.db import models
from django.contrib import admin
from binascii import hexlify

def _createId():
    return hexlify(os.urandom(16))

class Email(models.Model):
	from_name 		= models.CharField(max_length=50)
	from_email		= models.CharField(max_length=50)
	to_name   		= models.CharField(max_length=50)
	to_email  		= models.CharField(max_length=50)
	subject   		= models.CharField(max_length=100)
	body      		= models.TextField()

	#email_date		= models.DateTimeField(required=True)
	#unique_id		= models.CharField(max_length=16, primary_key=True, default=_createId)

	def __unicode__(self):
		return u'%s -> %s: %s' % (self.from_name, self.to_name, self.subject)