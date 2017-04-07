def run(request, data):
	data['merchant_data']=get_merchant_data(request)
	data['merchant_profile_data']=get_merchant_profile_data(request)
	print data

def get_merchant_data(request):
	merchant_data={}
	merchant_data['first_name']=request.get('first_name')
	merchant_data['last_name']=request.get('last_name')
	merchant_data['password']=request.get('password')
	merchant_data['email']=request.get('email')
	return merchant_data

def get_merchant_profile_data(request):
	merchant_profile_data={}
	merchant_profile_data['address']=request.get('address')
	merchant_profile_data['business_name']=request.get('business_name')
	merchant_profile_data['mobile_number']=request.get('mobile_number')
	return merchant_profile_data

