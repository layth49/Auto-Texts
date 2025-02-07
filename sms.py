import os 
import subprocess
import pyautogui
import time

# Define your contacts here
contacts = {
}


# Collect input for recipient
recipient_name = input("Who would you like to message? ")

# Check if the recipient is in your contact list
if recipient_name not in contacts:
    print(f"Error: {recipient_name} is not in your contact list.")
    exit()

recipient_number = contacts[recipient_name]

# Ask the user for the message
message_body = input("What would you like to say? ")


# Open the Phone Link app
os.system("start explorer shell:appsfolder\\Microsoft.YourPhone_8wekyb3d8bbwe!App")

# Press the compose button
while True:
    try:
        button = pyautogui.locateOnScreen("assets/compose.png", grayscale= True, confidence= 0.9)
        pyautogui.click(button)

        print("Compose button found")
        time.sleep(1)
        break
    except:
        time.sleep(1)
        print("Waiting for the compose button to appear")

# Type the recipient's number
pyautogui.write(recipient_number)
time.sleep(0.1)
pyautogui.press("enter")

time.sleep(1)

# Type the message
pyautogui.write(message_body)
time.sleep(0.1)
pyautogui.press("enter")