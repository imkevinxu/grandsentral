from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.core.context_processors import csrf
from django.template import RequestContext
from django.core.mail import send_mail, send_mass_mail
from datetime import datetime
from binascii import hexlify
import os

from emails.models import Email

def _createId():
    return hexlify(os.urandom(16))

def home(request):
	return render_to_response('index.html', context_instance=RequestContext(request))

def send(request):
	if request.method == "POST":
		subject = request.POST["email_subject"]
		unformatted_body = request.POST["email_body"]

		from_array = [request.POST["email_from_name"], request.POST["email_from_email"]]
		from_email = formatEmail(from_array[0], from_array[1])

		to_name_list = request.POST.getlist("email_recipients_name")
		to_email_list = request.POST.getlist("email_recipients_email")
		to_array = [to_name_list, to_email_list]

		formatted_to_email_list = []
		message_list = []
		for i in range(len(to_name_list)):
			if to_name_list[i] == "" or to_email_list[i] == "": break
			formatted_to_email_list.append(formatEmail(to_name_list[i], to_email_list[i]));
			body = unformatted_body.replace("[First]", getFirstName(to_name_list[i]))
			message_list.append((subject, body, from_email, [formatted_to_email_list[i]]))

			email = Email(from_name = from_array[0],
						  from_email = from_array[1],
						  to_name = to_array[0][i],
						  to_email = to_array[1][i],
						  subject = subject,
						  body = body,
						  email_date = datetime.now(),
						  unique_id = _createId())
			email.save()

		#if len(message_list) > 0:
			#send_mass_mail(message_list, fail_silently=False)

		return render_to_response('success.html',
			{"count" : len(formatted_to_email_list),
			"to_emails" : formatted_to_email_list,
			"from" : getFirstName(from_email),
			"subject" : subject,
			"body" : unformatted_body},
			context_instance=RequestContext(request))
	return HttpResponseRedirect('/')


# Fancier functions

def formatEmail(name, email):
	return name+" <"+email+">"

def getFirstName(name):
	return name.split(' ')[0]