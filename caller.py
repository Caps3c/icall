# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

print ("Please input the number you want to call")
victim = input()

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC505b8be8cceaf8a79a9cd5e937e2be14'
auth_token = '95aad1c2e446178f1e9554c51e5fae76'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to=victim,
                        from_='+12533001114'
                    )

print(call.sid)
