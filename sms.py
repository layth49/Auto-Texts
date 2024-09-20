import os
import requests
import logging
import smtplib
import numlookupapi

# Get ready for some ugly code


API_KEY_1 = os.environ['API_KEY_1']
API_KEY_2 = os.environ['API_KEY_2']
API_KEY_3 = os.environ['API_KEY_3']

def make_api_call(url, headers=None):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        return response.json()
    except requests.RequestException as e:
        logging.error(f"API call failed: {e}")
        return None

def get_carrier1(phone_number):
    url = f"http://apilayer.net/api/validate?access_key={API_KEY_1}&number=+1{phone_number}"
    data = make_api_call(url)
    if data and data["valid"]:
        return data["carrier"]
    return "Invalid phone number"

def get_carrier2(phone_number):
    url = f"https://api.apilayer.com/number_verification/validate?number=+1{phone_number}"
    headers = {"apikey": API_KEY_2}
    data = make_api_call(url, headers)
    if data:
        return data.get("carrier")
    return None

def get_carrier3(phone_number):
    client = numlookupapi.Client(API_KEY_3)
    result = client.validate(phone_number, country_code='US')
    if result and result["valid"]:
        return result["carrier"]
    return None

def get_carrier(phone_number):
    try:
        return get_carrier1(phone_number)
    except Exception:
        logging.error("Failed to get carrier from API 1")
        try:
            return get_carrier2(phone_number)
        except Exception:
            logging.error("Failed to get carrier from API 2")
            try:
                return get_carrier3(phone_number)
            except Exception:
                logging.error("Failed to get carrier from API 3")
                return "All API's are fully used"

# Example usage
phone_number = "+1234567890"
carrier = get_carrier(phone_number)
print(carrier)









# Storing this down here


"""
FROM_EMAIL = "#####@gmail.com"
PASSWORD = "#########"

number = input("Who would you like to message? ")

message = input("What would you like to say? ")


# Create the SMTP session
server = smtplib.SMTP('smtp.gmail.com', 587)  # Use Gmail's SMTP server with port 587
server.starttls()  

try:
    # Login to the email account
    server.login(FROM_EMAIL, PASSWORD)
    print("Login successful")


    server.sendmail(FROM_EMAIL, TO_EMAIL, message)
    print(f"Email sent successfully")

except Exception as e:
    print(f"Failed to send email: {e}")
finally:
    # Terminate the SMTP session
    server.quit()
    
"""