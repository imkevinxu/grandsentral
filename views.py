from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.core.context_processors import csrf
from django.template import RequestContext
from django.template.loader import render_to_string
from django.core.mail import send_mail, send_mass_mail, EmailMultiAlternatives
from datetime import datetime
from binascii import hexlify
import os
from emails.models import Email, Confirm

def home(request):
	return render_to_response('index.html', context_instance=RequestContext(request))

def hold(request):
	if request.method == "POST":

		# Grab all the data from POST requests
		subject = request.POST["email_subject"]
		unformatted_body = request.POST["email_body"]

		from_name = request.POST["email_from_name"]
		from_email = request.POST["email_from_email"]

		to_name_list = request.POST.getlist("email_recipients_name")
		to_email_list = request.POST.getlist("email_recipients_email")

		#TODO: QUICK HACKY FORM VALIDATION
		if subject == "" or unformatted_body == "" or from_name == "" or to_name_list[0] == "" or to_email_list[0] == "":
			return HttpResponseRedirect('/')
		
		# Format all the data and store into lists of correct emails
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

		#TODO: STOP Confirmation from happening if emails blank
		createConfirmationEmail(holding_email_list, from_name, from_email,
								formatted_to_email_list)

		return render_to_response('holding.html',
			{"count" : len(formatted_to_email_list),
			"to_emails" : formatted_to_email_list,
			"from" : getFirstName(from_name),
			"subject" : subject,
			"body" : unformatted_body},
			context_instance=RequestContext(request))

	return HttpResponseRedirect('/')

# Creating the confirmation email
def createConfirmationEmail(holding_email_list, from_name, from_email,
							formatted_to_email_list):
	confirm_email = Confirm(uid = _createId(), confirmed = False)
	confirm_email.save()
	confirm_email.emails = holding_email_list
	confirm_email.save()

	recipient = formatEmail(from_name, from_email)
	subject = 'GrandSentral Mailing Confirmation for ' + getFirstName(from_name)
	text_content = "Click here to send your mail merged emails http://grandsentral.com/confirm/" + confirm_email.uid
	html_content = render_to_string('email/confirmation.html',
					{'uid' : confirm_email.uid,
					'from' : getFirstName(from_name),
					'emails' : formatted_to_email_list})
	email = EmailMultiAlternatives(subject, text_content, 'Kevin Xu <admin@grandsentral.com>', [recipient])
	email.attach_alternative(html_content, "text/html")
	email.send()

def confirm(request, hash):
	confirm = Confirm.objects.get(uid=hash)
	if confirm.confirmed:
		return HttpResponseRedirect('/')
	else:
		sendEmail(confirm.emails.all())
		confirm.confirmed = True
		confirm.save()
	return HttpResponseRedirect('/success')

def success(request):
	return render_to_response('success.html', context_instance=RequestContext(request))

# Send email based on email list
def sendEmail(emails_to_send):
	message_list = []
	for email in emails_to_send:
		if email.sent == False:
			from_email = formatEmail(email.from_name, email.from_email)
			to_email = formatEmail(email.to_name, email.to_email)
			subject = email.subject
			body = email.body
			message_list.append((subject, body, from_email, [to_email]))
			email.sent = True
			email.save()

	if len(message_list) > 0:
		send_mass_mail(message_list, fail_silently=False)


# Fancier functions
def formatEmail(name, email):
	return name+" <"+email+">"

def getFirstName(name):
	return name.split(' ')[0]

def _createId():
    return hexlify(os.urandom(16))

