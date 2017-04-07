from django.test import TestCase

# Create your tests here.
import requests
def _test_(xml,url):
    url=url+xml
    headers={'content-type': 'text/xml; charset=utf-8'}
    r=requests.get(url, headers=headers)
    print url
if __name__=="__main__":
    from datetime import datetime
    import pytz
    reference = '{:%y%m%d%H%M%S}'.format(datetime.now())
    date = '{:%Y-%m-%d %H:%M:%S %z}'.format(datetime.utcnow().replace(tzinfo=pytz.utc))
    url="""http://196.201.214.53:5660/?VENDOR=D-C101&REQTYPE=EXRCTRFREQ&DATA"""
    xml="""<?xml version="1.0" encoding="UTF-8"?><ns0:COMMAND xmlns:ns0="http://safaricom.co.ke/Pinless/keyaccounts/"><ns0:TYPE>EXRCTRFREQ</ns0:TYPE><ns0:DATE>{0}</ns0:DATE><ns0:EXTNWCODE>SA</ns0:EXTNWCODE><ns0:MSISDN>700945099</ns0:MSISDN><ns0:PIN>9048</ns0:PIN><ns0:LOGINID>D-C101</ns0:LOGINID><ns0:PASSWORD>QGw6FyfM</ns0:PASSWORD><ns0:EXTCODE>D-C101</ns0:EXTCODE><ns0:EXTREFNUM>{1}</ns0:EXTREFNUM><ns0:MSISDN2>721799582</ns0:MSISDN2><ns0:AMOUNT>1000</ns0:AMOUNT><ns0:LANGUAGE1> </ns0:LANGUAGE1><ns0:LANGUAGE2></ns0:LANGUAGE2><ns0:SELECTOR></ns0:SELECTOR></ns0:COMMAND>""".format(date,reference).format(date,reference)
    _test_(xml,url)
    