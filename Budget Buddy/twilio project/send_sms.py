from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio

client = Client(account_sid, auth_token)

my_msg = "\n\nHello this is Budget Buddy!\n\nWe are sending this message to inform you that a $100 has been spent on the following card on Fornite.\n\nCard Holder: Oscar San\n\nCredit Card Number: 4983076716444511\n\nReply Yes if you would like this transaction to go through\n\nReply No if you would like to decline this transaction\n\nThank you."

message = client.messages.create(to=my_cell, from_=my_twilio, body=my_msg)

