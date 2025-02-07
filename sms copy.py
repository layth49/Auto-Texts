import smtplib
from email.mime.text import MIMEText
import vonage

# Define your contacts here
contacts = {
    
}
'''
# Collect input for recipient and message
recipient_name = input("Who would you like to message? ")

# Check if the recipient is in your contact list
if recipient_name not in contacts:
    print(f"Error: {recipient_name} is not in your contact list.")
    exit()

recipient_email = contacts[recipient_name]
'''
client = vonage.Client(key="", secret="")

print(f"Account balance is: {client.account.get_balance()}")

# Ask the user for the message
message_body = input("What would you like to say? ")


try:
    print("Sending an SMS")
    client.sms.send_message({
        "from": "Vonage",
        "to": "1234567890",
        "text": message_body
    })
except:
    print("Failed to send SMS")