from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.contrib.auth.models import User
from app.models import Merchants
def run(data):
	user_data=data.get('merchant_data')
	user_data=User(**user_data)

	merchant_data=data.get('merchant_profile_data')
	merchant_data=Merchants(**merchant_data)

	mobile_number=merchant_data.mobile_number
	email=user_data.email
	first_name=user_data.first_name
	last_name=user_data.last_name
	send_to_saiba(email,first_name,last_name,mobile_number)


def send_to_saiba(email,first_name,last_name,mobile_number):
	subject="New Merchant Registration"
	subject, from_email, to = subject,email, settings.EMAIL_RECIPENT
	text_content = 'A new merchant {0} {1} using mobile number {2} has register as a merchant'.format(first_name, last_name, mobile_number)
	html_content = "<p>A new merchant {0} {1} using mobile number {2} has register as a merchant</p>".format(first_name, last_name, mobile_number)
	msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
	msg.attach_alternative(html_content, "text/html")
	msg.send()





def send_to_merchant(email):
	pass

