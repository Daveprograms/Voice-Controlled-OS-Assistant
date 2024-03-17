
import datetime

import form
import pyttsx3
import os
import pygame
import speech_recognition as sr
from curl_cffi.requests import head
from gtts import gTTS
import pyautogui
import pywhatkit
from datetime import datetime
from scrapper.bot import click_on_chat_button, sendQuery, isBubbleLoaderVisible, retriveData
from gpt4 import GPT
from functions.emailsender import send_email
import time
from head.listen import take_command
from head.speak import speak



def sleep_music():
    pygame.mixer.init()
    pygame.mixer.music.load("relaxing-music-vol1-124477.mp3")
    pygame.mixer.music.play()
    time.sleep(5)

def wake_up_theme():
    pygame.mixer.init()
    pygame.mixer.music.load("legends-arise-185521.mp3")
    pygame.mixer.music.play()

    # Wait for 5 seconds
    pygame.time.delay(5000)

    # Fade out the music gradually over 2 seconds
    pygame.mixer.music.fadeout(2000)


def get_greeting():
    current_time = datetime.now()
    if current_time.hour < 12:
        return "Good morning"
    elif 12 <= current_time.hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"



def open_application(app_name):
    speak(f'Opening {app_name}')


    pygame.mixer.init()
    pygame.mixer.music.load("o-come-o-come-emmanuel-11563.mp3")
    pygame.mixer.music.play()

    pyautogui.press('super')
    pyautogui.typewrite(app_name)
    pyautogui.sleep(0.7)
    pyautogui.press('enter')

    pyautogui.sleep(5)


    pygame.mixer.music.stop()



def get_user_info():
    speak("Can you please provide your first name?")
    first_name = take_command()
    speak("Thank you. Can you now provide your last name?")
    last_name = take_command()
    speak("And finally, can you provide the name of your organization or Persons name")
    organization = take_command()
    return first_name, last_name, organization


def compose_email():
    speak("Please type the recipient's email address:")
    recipient = input("Recipient's email address: ")

    speak("What should be the subject of the email?")
    subject = take_command()

    speak("What should be the content? Just provide me some prompts.")
    email_prompt = take_command()

    first_name, last_name, organization = get_user_info()
    content = GPT(f'write a mail for {email_prompt} by {first_name} {last_name} from {organization}')

    return recipient, subject, content




def main():
    greeting = get_greeting()
    name = "David"
    message = f"{greeting} {name}, How can i help you today."
    print(message)
    speak(message)

    sleep_mode = False
    click_on_chat_button()


    while True:
        query = take_command()
        print('\n' + query)

        if 'open' in query:
            app_name = query.replace('open', '').strip()
            open_application(app_name)

        elif 'play' in query:
            song_name = query.replace('play', '').strip()
            speak(f'Sure David. Playing {song_name} on YouTube.')
            pywhatkit.playonyt(song_name)

        elif 'switch tab' in query:
            pyautogui.hotkey('ctrl', 'tab')

        elif 'change application' in query:
            pyautogui.hotkey('alt', 'tab')
        elif 'show all running apps' in query:
            pyautogui.hotkey('win', 'tab')

        elif 'close tab' in query:
            pyautogui.hotkey('ctrl', 'w')

        elif 'close' in query:
            pyautogui.hotkey('alt', 'f4')
            speak('Done Master David')

        elif 'time' in query:
            current_time = datetime.now().strftime('%I:%M %p')
            speak('The current time is ' + current_time)

        elif 'sleep' in query:
            speak("Ok, Master, I am going to sleep. You can wake me up anytime by saying 'Wake up'.")
            sleep_music()
            sleep_mode = True

        elif 'Write an email' in query or 'compose a mail' in query or 'send an email' in query or 'email' in query:
            recipient, subject, content = compose_email()

            speak('Email composed successfully. Ready to send. Do you want to proceed?')
            user_response = take_command()

            if 'yes' in user_response or 'send' in user_response or 'proceed' in user_response:
                try:
                    send_email(recipient, subject, content)
                    speak(f'Done Sir. Email sent successfully to {recipient}')
                except Exception as e:
                    print(e)
                    speak(f'Sorry, there was an error sending the email. Please try again.')
            else:
                speak('Email not sent. If you want to compose a new email, just let me know.')


        else:
            sendQuery(query)
            isBubbleLoaderVisible()
            response = retriveData()
            speak(response)

        while sleep_mode:
            query = take_command().lower()
            print(query)
            if 'wake up' in query:
                wake_up_theme()
                speak('I am awake. How can I help you, Master David?')
                sleep_mode = False



if __name__ == "__main__":
    main()
