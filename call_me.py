from twilio.rest import Client
from credentials import *

client = Client(account_sid, auth_token)

call = client.calls.create(
    to=phone_num,
    from_=my_phone,
    url='http://demo.twillio.com/docs/voice.xml'
)

print(call.account_sid)
