from app.models import Contacts
def run(data):
    contact_data=data.get('contact_data')
    contact_data=Contacts(**contact_data)
    first_name=contact_data.first_name
    last_name=contact_data.last_name
    email=contact_data.email
    mobile_number=contact_data.mobile_number
    description=contact_data.description
    save=Contacts(first_name=first_name, last_name=last_name,email=email,
                  mobile_number=mobile_number,description=description)
    save.save()
