from twilio.rest import TwilioRestClient

# put your own credentials here
ACCOUNT_SID = "AC29057cf0369870f6223bc6c566dd79d3"
AUTH_TOKEN = "bb7b9351a2bdd8e83b2844c4dddde73e"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(
	to="+919886689752",
	from_="+14848702183",
	body="Hello Sammme here came from atom",
)
