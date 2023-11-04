import pyttsx3
import pywhatkit 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import pyaudio
import random
import googletrans
from googletrans import *
import googlesearch

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
ran_num= random.randint(1,3)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<6:
        speak("Just sleep! I also have to sleep.")

    elif hour>=6 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")   

    else:
        speak("Good Evening")  

    speak("This is Friday. Please tell how i can help you!!")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception :
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('gamerindianpartime2003@gmail.com', 'Gamerindianpartime@2003')
    server.sendmail('subhradip007das@gmail.com', to, content)
    server.close()

def translaet(n):
    translating=googletrans.Translator()
    try:
        translated= translating.translate(n, dest="hi")
        return translated.text

    except:
        speak("Please check the spellings..")

if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\SUBHRADIP PC\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)

        elif 'mail to sd' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "subhradip007das@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry SD. I am not able to send this email")   

        elif 'do you love me' in query:
            
            if (ran_num==1):
                speak("Sorry! Better luck next time..") 
                reply=takeCommand()
                if 'fuck' in reply:
                    speak("That's rude")
            if (ran_num==2):
                speak("Ofcourse i do. But do you?") 
                reply=takeCommand()
                if 'no' in reply:
                    speak("That's rude")
            if (ran_num==3):
                speak("No. The world will not allow us!") 
                reply=takeCommand()
                if 'fuck' in reply:
                    speak("That's rude")

        elif 'hello friday' in query:
            speak("Yes sir, always at your service")

        elif 'who are you' in query:
            speak("I am an artificial intelligence, made by Subhradip Das. I can answer you whatever you ask. THank u")

        elif 'translate this' in query:
            word=input(speak("Enter the word or sentence"))
            word=takeCommand().lower()
            print(translaet(word))


        elif 'exit this program' in query:
            exit()
        
        elif 'play' in query:
            query=query.replace("play", "")
            reply1="https://www.youtube.com/results?search_query="+query
            speak(f"Playing {query}")

            pywhatkit.playonyt(query)
            exit()
        elif query==None:
            speak("I am waiting")

        else:
            speak("lemme search it")
            pywhatkit.search(query)
            try:
                answer= wikipedia.summary(query,sentences="2")
                speak(answer)
            
            except:
                speak("I am sorry sir, but still cannot figure it out")
            
