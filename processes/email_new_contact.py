from app.models import Contacts
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
def run(data):
    contact_data=data.get('contact_data')
    contact_data=Contacts(**contact_data)
    email=contact_data.email
    first_name = contact_data.first_name
    last_name = contact_data.last_name
    email = contact_data.email
    mobile_number = contact_data.mobile_number
    description = contact_data.description
    send_to_saiba(email,first_name, last_name,mobile_number, description)

def send_to_saiba(email,first_name,last_name,mobile_number,description):
	subject="New Contact"
	subject, from_email, to = subject,email, settings.EMAIL_RECIPENT
	text_content = 'An enquiry was sent by {0} {1} saying {2} you can get back  using mobile number {3} or {4}'.format(first_name, last_name,description, mobile_number,email)
	html_content = "<p>An enquiry was sent by {0} {1} saying {2} you can get back  using mobile number {3} or {4}</p>".format(first_name, last_name,description, mobile_number,email)
	msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
	msg.attach_alternative(html_content, "text/html")
	msg.send()
