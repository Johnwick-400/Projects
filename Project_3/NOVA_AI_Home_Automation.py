import pyttsx3  # pip install pyttsx3
import speech_recognition as sr
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

def text2int(textnum, numwords={}):
    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current
    
    
def name():
    speak('Hello sir i am nova')
 
 
 
 
 
 
 
 
 
 
 
 
    
def turnon_l1():
    x = r.get('http://192.168.50.198/turn_off1')
    if x == 200:
        print('Command sent successfully')
    else:
        print('Failed to send command')


def turnoff_l1():
    x = r.get('http://192.168.50.198/turn_on1')
    print(x)
    if x == 200:
        print('Command sent successfully')
    else:
      print('Failed to send command')



def turnoff_l2():
    x = r.get('http://192.168.50.198/turn_on2')
    print(x)
    if x == 200:
        print('Command sent successfully')
    else:
      print('Failed to send command')



def turnon_l2():
    x = r.get('http://192.168.50.198/turn_off2')
    if x == 200:
        print('Command sent successfully')
    else:
      print('Failed to send command')



def turnoff_l3():
    x = r.get('http://192.168.50.198/turn_on3')
    if x == 200:
        print('Command sent successfully')
    else:
      print('Failed to send command')



def turnon_l3():
    x = r.get('http://192.168.50.198/turn_off3')
    if x == 200:
        print('Command sent successfully')
    else:
      print('Failed to send command')



def turnoff_l4():
    x = r.get('http://192.168.50.198/turn_on4')
    if x == 200:
        print('Command sent successfully')
    else:
      print('Failed to send command')



def turnon_l4():
    x = r.get('http://192.168.50.198/turn_off4')
    if x == 200:
        print('Command sent successfully')
    else:
      print('Failed to send command')



def timer1_l1():
    speak("tell me how many seconds u want to set the timer for")
    query = takeCommand().lower()
    query.replace("seconds","")
    t1=text2int(query)
    x=r.post("http://192.168.50.198/onswitch1",data={'data': t1})
    if x == 200:
        print('Command sent successfully')
    else:
      print('Failed to send command')


def timer_l1():
    speak("tell me how many seconds u want to set the timer for")
    query = takeCommand().lower()
    query.replace("seconds","")
    t1=text2int(query)
    x=r.post("http://192.168.50.198/offswitch1",data={'data': t1})
    if x == 200:
        print('Command sent successfully')
    else:
      print('Failed to send command')      


def timer1_l2(t2):
    speak("tell me how many seconds u want to set the timer for")
    query = takeCommand().lower()
    query.replace("seconds","")
    t2=text2int(query)
    x=r.post("http://192.168.50.198/onswitch2",data={'data': t2})
    
    if x == 200:
        print('Command sent successfully')
    else:
      print('Failed to send command')


def timer_l2(t2):
    speak("tell me how many seconds u want to set the timer for")
    query = takeCommand().lower()
    query.replace("seconds","")
    t2=text2int(query)
    x=r.post("http://192.168.50.198/offswitch2",data={'data': t2})
    
    if x == 200:
        print('Command sent successfully')
    else:
      print('Failed to send command')


def timer1_l3(t3):
    speak("tell me how many seconds u want to set the timer for")
    query = takeCommand().lower()
    query.replace("seconds","")
    t3=text2int(query)
    x=r.post("http://192.168.50.198/onswitch3",data={'data': t3})
    if x == 200:
        print('Command sent successfully')
    else:
      print('Failed to send command')


def timer_l3(t3):
    speak("tell me how many seconds u want to set the timer for")
    query = takeCommand().lower()
    query.replace("seconds","")
    t3=text2int(query)
    x=r.post("http://192.168.50.198/offswitch3",data={'data': t3})
    if x == 200:
        print('Command sent successfully')
    else:
      print('Failed to send command')


def timer1_l4(t4):
    speak("tell me how many seconds u want to set the timer for")
    query = takeCommand().lower()
    query.replace("seconds","")
    t4=text2int(query)
    x=r.post("http://192.168.50.198/onswitch4",data={'data': t4})
    if x == 200:
        print('Command sent successfully')
    else:
      print('Failed to send command')

def timer_l4(t4):
    speak("tell me how many seconds u want to set the timer for")
    query = takeCommand().lower()
    query.replace("seconds","")
    t4=text2int(query)
    x=r.post("http://192.168.50.198/offswitch4",data={'data': t4})
    if x == 200:
        print('Command sent successfully')
    else:
      print('Failed to send command')


def turnoff_all():
    x = r.get('http://192.168.50.198/turn_on1')
    x = r.get('http://192.168.50.198/turn_on2')
    x = r.get('http://192.168.50.198/turn_on3')
    x = r.get('http://192.168.50.198/turn_on4')


def turnon_all():
    x = r.get('http://192.168.50.198/turn_off1')
    x = r.get('http://192.168.50.198/turn_off2')
    x = r.get('http://192.168.50.198/turn_off3')
    x = r.get('http://192.168.50.198/turn_off4')
    

















 #===============================================    

while True:
    query = takeCommand().lower()
    if "hey nova" in query:
        speak("Hello sir. How can I help you.")
    elif query in ['turn on light one', 'turn on right one',
                       'turn on light 1','turn on right 1']:
        turnon_l1()
    elif query in ['turn on light 2',
                    'turn on light to',
                    'turn on light two']:
        turnon_l2()
    elif query in ['turn on light three ', 'turn on right three',
                       'turn on light 3','turn on light gayatri','turn on right 3']:
        turnon_l3()
    elif query in ['turn on light for',
                    'turn on light phone',
                    'turn on light 4',
                    'turn on light fourth',
                    'turn on light four']:
        turnon_l4()
    elif query in ['turn off light one',
                    'turn off light 1']:
        turnoff_l1()
    elif query in ['turn off light 2',
                    'turn off light two',
                    'turn off right 2',
                    'turn off light to','turn off right to','turn off right two']:
        turnoff_l2()
    elif query in ['turn off light 3',
                    'turn off light three','turn off right three','turn off light 3']:
        turnoff_l3()
    elif query in ['turn off light 4',
                       'turn off light for',
                       'turn off light four','turn off right 4','turn off right four']:
        turnoff_l4()
    elif query in ['turn on all lights',
                   'turn on all lights',
                       'turn on hall lights']:
        turnon_all()
    elif "timer on light one" in query:
        timer_l1()
    elif "timer off light one" in query:
        timer1_l1()
    elif "timer on light two" in query:
        timer_l2()
    elif "timer off light two" in query:
        timer1_l2()
    elif "timer on light three" in query:
        timer_l3()
    elif "timer off light three" in query:
        timer1_l3()
    elif "timer on light four" in query:
        timer_l4()
    elif "timer off light four" in query:
        timer1_l4()
    elif "turn off all lights" in query:
        turnoff_all()
    
    #elif "bye" in query:
    #   bye()
    elif "---" in query:
        pass
    else: 
        speak("please try again") 