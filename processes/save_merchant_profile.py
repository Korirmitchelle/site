from app.models import Merchants
from django.contrib.auth.models import User

def run(data):
	merchant_data=data.get('merchant_profile_data')
	merchant_data=Merchants(**merchant_data)
	user_data=data.get('merchant_data')
	user_data=User(**user_data)
	business_name=merchant_data.business_name
	mobile_number=merchant_data.mobile_number
	address=merchant_data.address
	email=user_data.email
	user=User.objects.get(email=email)
	save=Merchants(user=user,business_name=business_name,mobile_number=mobile_number,address=address)
	save.save()



