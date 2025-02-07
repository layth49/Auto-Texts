import smtplib
from email.mime.text import MIMEText

# Define your contacts here
contacts = {
    
}

# Collect input for recipient and message
recipient_name = input("Who would you like to message? ")

# Check if the recipient is in your contact list
if recipient_name not in contacts:
    print(f"Error: {recipient_name} is not in your contact list.")
    exit()

recipient_email = contacts[recipient_name]

FROM_EMAIL = ""
PASSWORD = ""

# Ask the user for the message
message_body = input("What would you like to say? ")

# Create the message as plain text
msg = MIMEText(message_body)
msg['From'] = FROM_EMAIL
msg['To'] = recipient_email
msg['Subject'] = ""  # Blank subject to avoid carrier-specific formatting

# Create the SMTP session
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

try:
    # Login to your email account
    server.login(FROM_EMAIL, PASSWORD)
    print("Login successful")

    # Send the email
    server.sendmail(FROM_EMAIL, recipient_email, msg.as_string())
    print(f"Message sent successfully to {recipient_name}")

except Exception as e:
    print(f"Failed to send message: {e}")

finally:
    # Close the SMTP session
    server.quit()