import phonenumbers
number = "+254732813746"
from phonenumbers import carrier
service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "eng"))
