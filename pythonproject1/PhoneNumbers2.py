import phonenumbers
number="+254723456789"
from phonenumbers import geocoder
#from testproject import number

#############PHONE COMPANY####################

from phonenumbers import carrier
service_number=phonenumbers.parse(number,'RO')
print(carrier.name_for_number(service_number,"eng"))

#############COUNTRY OF ORIGIN####################
phones=phonenumbers.parse(number ,"CH")
print(geocoder.description_for_number(phones,"eng"))