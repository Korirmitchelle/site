from django.contrib.auth.models import User
from app.models import Merchants


def run(data):
	global email
	merchant_data=data.get('merchant_data')
	merchant_data=User(**merchant_data)

	user_data=data.get('merchant_profile_data')
	user_data=Merchants(**user_data)

	first_name=merchant_data.first_name
	last_name=merchant_data.last_name
	password=merchant_data.password
	email=merchant_data.email
	mobile_number=user_data.mobile_number
	save=User(first_name=first_name, username=mobile_number, last_name=last_name,password=password, email=email)
	save.save()

