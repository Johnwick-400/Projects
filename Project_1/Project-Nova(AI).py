import datetime
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr
import webbrowser
import subprocess
import os
from time import sleep
import pyautogui as p
import pyjokes
import requests as r



engine = pyttsx3.init('sapi5')  # initialise pyttsx3
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0-2 range for different voices
voicespeed = 140  # setting speed
engine.setProperty('rate', voicespeed)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    """Listen for a command from the user and return it as text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...") 
        query = r.recognize_google(audio, language='en-us')
    except Exception as e:

        print()
        return "---"
    return query

def time():
    """Speak the current time."""
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(time)
    print(time)

def wishme():
    speak("welcome back sir")

    hour = datetime.datetime.now().hour
    if hour>=6 and hour<=11:
        speak('Good morning')
    elif hour>=11 and hour<=16:
        speak('Good afternoon')
    elif hour>=16 and hour<20:
        speak('Good evening')
    else:
        speak('good night') 
    speak('How can i help you today')
def bye():
    speak("Have a good day")
    exit()
def open_chrome():
    # url u want to open
    url = 'http://www.lendi.org/'

    # Windows
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    # replace chrome_path with the correct path for your platform.

    # MacOS
    # chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

    # Linux
    # chrome_path = '/usr/bin/google-chrome %s'
    webbrowser.get(chrome_path).open(url)
    # call the function
def search():
    speak("what should i search?")
    chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"  # location
    search = takeCommand().lower()
    webbrowser.get(chromepath).open_new_tab(search + ".com")
def vscode():
     speak("opening virtual studio code")
     vscode_path="C:/Program Files/VMware Workstation 17 Player.exe"
     vscode=subprocess.Popen(vscode_path)
def name():
    speak('Hello sir i am nova')
def music():
     url = 'https://open.spotify.com/'

     chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
     webbrowser.get(chrome_path).open(url)
     sleep(10)
     p.hotkey("space") 
def code(query):
    p.hotkey("winleft","r")
    p.write("cmd")
    p.press("enter")
    p.sleep(2)
    p.write("howdoi ")
    p.write(query)
    p.press("enter")


def weather(citydata="guntur"):
    url = 'https://wttr.in/{}'.format(citydata)
    res = r.get(url)
    print(res.text)



 #===============================================    
if __name__ == "__main__":


    while True:
        
        query = takeCommand().lower()
        print(query)

        if "good morning" in query:
            speak("good morning sir")
        
        elif "nova" in query:
            wishme()
        elif "time" in  query:
            time()
        elif "see you later" in query:
            bye()
        elif "vs code" in query:
            vscode()
        elif "---" in query:
            pass
        elif ("name") in query:
            name()
        elif "chrome" in query:  # quit to end the program
            speak("opening the Chrome")
            open_chrome()
        elif "search" in query:
            search()
        elif "logout" in query:
            speak('logging out in 5 second')
            sleep(5)
            os.system("shutdown - l")
        elif "shutdown" in query:
            speak('shutting down in 5 second')
            sleep(5)
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            speak('restarting in 5 second')
            sleep(5)
            os.system("shutdown /r /t 1")
        elif "music" in query:
            music()
        elif "joke" in query:
            speak(pyjokes.get_jokes())
        elif "hidden menu" in query:
            # Win+X: Open the hidden menu
            p.hotkey('winleft', 'x')
        elif "task" in query:
            # Ctrl+Shift+Esc: Open the Task Manager
            p.hotkey('ctrl', 'shift', 'esc')
        elif "taskview" in query:
             # Win+Tab: Open the Task view
            p.hotkey('winleft', 'tab')
        elif "screenshot" in query:
             # win+perscr
             p.hotkey('winleft', 'prtscr')
             speak("done")
        elif "exit" in query:
            p.hotkey('alt','f4')
        elif "setting" in query:
             # win+i = open setting
             p.hotkey('winleft', 'i')
        elif "enable code" in query:
            speak("code mode is enable")
            speak("ask your question")
            query_code=takeCommand().lower()
            code(query_code)
        elif "weather" in query:
            qlist=list(query.split(" "))
            print(qlist)
            for i in range(len(qlist)):
                if qlist[i]== 'in' or 'at':
                    k=weather(qlist[i+1])
                    exit
            else: 
                speak("can you please repeat it again")
        elif "---" in query:
            pass
        else: 
            speak("not found at database")
            chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"  # location
            webbrowser.get(chromepath).open_new_tab(url="www.google.com")
            sleep(1)
            p.hotkey("ctrl",'k')
            p.write(query)
            p.press("enter") 
        
                   