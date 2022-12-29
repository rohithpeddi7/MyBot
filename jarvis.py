import pyttsx3
import datetime
import speech_recognition as sr
import time
user = "gaurav" #Change name as per user's name

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    '''
    It basically outputs the text passed as speech and stdout.
    '''
    engine.say(text)
    print(text)
    engine.runAndWait()

def wishMe():
    '''
    Wishes the user
    '''
    hour = int(datetime.datetime.now().hour)
    if (hour<12):
        speak("Good morning "+user+"!")
    elif (hour<=16):
        speak("Good afternoon "+user+"!")
    else:
        speak("Good evening "+user+"!")

    speak("I'm Jarvis! Please tell me how can I help you?")

def takeCommand():
    '''
    Takes the command from user as audio
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"{user} said {query}")
    except:
        print('Sorry! Please say that again')
        return "None"

if __name__=="__main__":
    wishMe()
    takeCommand()