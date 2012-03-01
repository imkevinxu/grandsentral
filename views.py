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
		subject = request.POST["email_subject"]

		to_name_list = request.POST.getlist("email_recipients_name")
		to_email_list = request.POST.getlist("email_recipients_email")
		formatted_to_email_list = []
		for i in range(len(to_name_list)):
			if to_name_list[i] == "" or to_email_list[i] == "": break
			formatted_to_email_list.append(formatEmail(to_name_list[i], to_email_list[i]));

		for formatted_email in formatted_to_email_list:
			body = request.POST["email_body"].replace("[First]", grabFirstName(formatted_email))
			print body
			#send_mail(subject, body, from_email, [to_email], fail_silently=False)
		return render_to_response('index.html', context_instance=RequestContext(request))
	return HttpResponseRedirect('/')


# Fancier functions

def formatEmail(name, email):
	return name+" <"+email+">"

def grabFirstName(name):
	return name.split(' ')[0]