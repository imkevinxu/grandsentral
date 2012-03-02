from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.core.context_processors import csrf
from django.template import RequestContext
from django.core.mail import send_mail, send_mass_mail
from datetime import datetime
from binascii import hexlify
import os

from emails.models import Email, Confirm

def _createId():
    return hexlify(os.urandom(16))

def home(request):
	return render_to_response('index.html', context_instance=RequestContext(request))

def hold(request):
	if request.method == "POST":
		subject = request.POST["email_subject"]
		unformatted_body = request.POST["email_body"]

		from_name = request.POST["email_from_name"]
		from_email = request.POST["email_from_email"]

		to_name_list = request.POST.getlist("email_recipients_name")
		to_email_list = request.POST.getlist("email_recipients_email")
		
		formatted_to_email_list = []
		holding_email_list = []
		for i in range(len(to_name_list)):
			if to_name_list[i] == "" or to_email_list[i] == "": break
			body = unformatted_body.replace("[First]", getFirstName(to_name_list[i]))
			formatted_to_email_list.append(formatEmail(to_name_list[i], to_email_list[i]));

			email = Email(from_name = from_name,
						  from_email = from_email,
						  to_name = to_name_list[i],
						  to_email = to_email_list[i],
						  subject = subject,
						  body = body,
						  uid = _createId(),
						  sent = False)
			email.save()
			holding_email_list.append(email);

		# Creating the confirmation email
		confirm_email = Confirm(uid = _createId())
		confirm_email.save()
		confirm_email.email_ids = holding_email_list
		confirm_email.save()

		return render_to_response('holding.html',
			{"count" : len(formatted_to_email_list),
			"to_emails" : formatted_to_email_list,
			"from" : getFirstName(from_name),
			"subject" : subject,
			"body" : unformatted_body},
			context_instance=RequestContext(request))

	return HttpResponseRedirect('/')

#def sendEmail():

#		from_email = formatEmail(from_array[0], from_array[1])
#		formatted_to_email_list = []
#		message_list = []
#			formatted_to_email_list.append(formatEmail(to_name_list[i], to_email_list[i]));
#			message_list.append((subject, body, from_email, [formatted_to_email_list[i]]))


		#if len(message_list) > 0:
			#send_mass_mail(message_list, fail_silently=False)


# Fancier functions

def formatEmail(name, email):
	return name+" <"+email+">"

def getFirstName(name):
	return name.split(' ')[0]