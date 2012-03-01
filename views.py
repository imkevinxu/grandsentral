from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.core.context_processors import csrf
from django.template import RequestContext
from django.core.mail import send_mail

def home(request):
	return render_to_response('index.html', context_instance=RequestContext(request))

def send(request):
	if request.method == "POST":
		from_email = formatEmail(request.POST["email_from_name"], request.POST["email_from_email"])

		to_name = request.POST["email_recipients_name"]
		to_email = formatEmail(request.POST["email_recipients_name"], request.POST["email_recipients_email"])
		subject = request.POST["email_subject"]
		body = request.POST["email_body"].replace("@@First", grabFirstName(to_name))
		#send_mail(subject, body, from_email, [to_email], fail_silently=False)
		return render_to_response('index.html', context_instance=RequestContext(request))
	return HttpResponseRedirect('/')


# Fancier functions

def formatEmail(name, email):
	return name+" <"+email+">"

def grabFirstName(name):
	return name.split(' ')[0]