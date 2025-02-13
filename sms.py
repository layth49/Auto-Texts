import os 
import subprocess
import pyautogui
import time
import azure.cognitiveservices.speech as speechsdk

# Define your contacts here
contacts = {


}


speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
speech_config.speech_recognition_language="en-US"

audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

# Add phrases to the grammar to be recognized by the speech recognizer
phrase_list = speechsdk.PhraseListGrammar.from_recognizer(speech_recognizer)
phrases = list(contacts.keys())


for phrase in phrases:
    phrase_list.addPhrase(phrase)
    print(f"Added phrase: {phrase}")


print("Speak into your microphone.")
speech_recognition_result = speech_recognizer.recognize_once_async().get()



# This is wrong but I'll fix it later
if contacts in speech_recognition_result:
    
    print("Recognized: " + speech_recognition_result.text)

    recipient_number = contacts[speech_recognition_result]

    # Ask the user for the message (this will be replaced by speech recognition later)
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