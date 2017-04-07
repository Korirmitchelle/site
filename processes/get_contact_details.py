def run(request, data):
    data['contact_data']=get_contact_data(request)

def get_contact_data(request):
    contact_data={}
    contact_data['first_name']=request.get("first_name")
    contact_data['last_name']=request.get('last_name')
    contact_data['email']=request.get('email')
    contact_data['mobile_number']=request.get('mobile_number')
    contact_data['description']=request.get('description')
    return  contact_data
