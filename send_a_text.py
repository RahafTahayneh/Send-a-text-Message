from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC7487ce336f75cda613abe3f2bbb081cf"
# Your Auth Token from twilio.com/console
auth_token  = "8f90985dd0a92c85c9fe508ccaa86acf"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+970595840503", 
    from_="+14253995455",
    body="Hello from Python!")

print(message.sid)
