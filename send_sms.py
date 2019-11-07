from twilio.rest import TwilioRestClient, Client
from credentials import *
from twilio.twiml.messaging_response import MessagingResponse

client = Client(account_sid, auth_token)

message = "ЯШКИНО"

message = client.messages.create(
    to=phone_num,
    from_=my_phone,
    body=message
)
