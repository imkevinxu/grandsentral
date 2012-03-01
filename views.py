from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.core.context_processors import csrf
from django.template import RequestContext
from django.core.mail import send_mail, send_mass_mail

def home(request):
	return render_to_response('index.html', context_instance=RequestContext(request))

def send(request):
	if request.method == "POST":
		from_email = formatEmail(request.POST["email_from_name"], request.POST["email_from_email"])
		subject = request.POST["email_subject"]
		unformatted_body = request.POST["email_body"]

		to_name_list = request.POST.getlist("email_recipients_name")
		to_email_list = request.POST.getlist("email_recipients_email")
		formatted_to_email_list = []
		for i in range(len(to_name_list)):
			if to_name_list[i] == "" or to_email_list[i] == "": break
			formatted_to_email_list.append(formatEmail(to_name_list[i], to_email_list[i]));

		message_list = []
		for formatted_email in formatted_to_email_list:
			body = unformatted_body.replace("[First]", grabFirstName(formatted_email))
			message_list.append((subject, body, from_email, [formatted_email]))

		if len(message_list) > 0:
			#send_mass_mail(message_list, fail_silently=False)

		return render_to_response('success.html',
			{"count" : len(formatted_to_email_list),
			"to_emails" : formatted_to_email_list,
			"from" : grabFirstName(from_email),
			"subject" : subject,
			"body" : unformatted_body},
			context_instance=RequestContext(request))
	return HttpResponseRedirect('/')


# Fancier functions

def formatEmail(name, email):
	return name+" <"+email+">"

def grabFirstName(name):
	return name.split(' ')[0]