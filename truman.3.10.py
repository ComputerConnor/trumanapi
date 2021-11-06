# Truman is you're virtual assistant like cortona. You can add some codes for you comfortable like you can add some more websites.
import pyttsx3
import datetime
import time
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import python_weather
import json
import pyjokes
import subprocess
import asyncio
from subprocess import call
from tkinter import *
from urllib.request import urlopen
from ursina import *
from PyDictionary import PyDictionary
from threading import Timer

engine = pyttsx3.init('sapi5')
engine.setProperty('voice',"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0")
joke=pyjokes.get_joke(language='en', category= 'all')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning sir")

    elif hour >= 12 and hour < 18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")

    speak(" i am Truman. please tell me how may i assist you?")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-gb')
        print(f"User said, {query}\n")
    except Exception as e:
        print(e)
        speak("say that again please?...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ai.computerconnor@gmail.com','Jarvis101')
    server.sendmail('ai.computerconnor@gmail.com', to, content)
    server.close()

def print_and_speak(text):
            print(text)
            engine.say(text)
            engine.runAndWait()

def on_press(z):
    exit()

#functions
dictionary=PyDictionary()
def reminder():
    t = Timer(30.0, reminder)
    t.start()


if __name__ == '__main__':
    wishMe()
    while True:

        query = takeCommand().lower()

        if 'speed' in query or 'set speed to' in query or 'jetspeed' in query:
            query = query.replace("speed", "")
            query = query.replace("set speed to", "")
            query = query.replace("jetspeed", "")
            engine.setProperty("rate", query)

        #peeps
        elif 'who is Truman Vincent' in query:
            speak("Some Guy Who Goes to Pickwick on the Weekend, plays guitar, does crossfit, and is hunkalicious.")

        elif 'who is Connor Jordan' in query or 'who is computer Connor' in query:
            speak("the guy who made me :)")

        elif 'who is Frankie Hall' in query:
            speak("that guy you don't owe money to")
        #end of peeps (more soon to come)

        elif 'wikipedia' in query or 'who is' in query or 'what is' in query:                                         
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            query = query.replace("who is", "")
            query = query.replace("what is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'what does' in query or 'what is the definition of' in query or 'mean' in query:
            query = query.replace("what does", "")
            query = query.replace("what is the definition of", "")
            query = query.replace("mean", "")
            print(dictionary.meaning(query))
            speak(dictionary.meaning(query))

        elif 'open youtube' in query:
            speak("right away sir")
            webbrowser.open("https://www.youtube.com")

        elif 'play my mix on youtube' in query or 'open my mix on youtube' in query or 'shuffle my mix on youtube' in query or 'shuffle my music on youtube' in query or 'shuffle my music' in query:
            speak("right away sir")
            webbrowser.open("https://www.youtube.com/watch?v=awToXost0Wc&list=RDMMawToXost0Wc&index=1")

        elif 'open google' in query:  
            speak("right away sir")                                   
            webbrowser.open("https://www.google.com")

        elif 'open stackoverflow' in query:   
            speak("right away sir")                           
            webbrowser.open("https://www.stackoverflow.com")
        
        elif 'open github' in query:
            speak("right away sir")
            webbrowser.open("https://github.com/ComputerConnor")         

        elif 'open' in query:
            query = query.replace("open ", "")
            if (query=='Brave'):
                call(["brave.exe"])
            if (query=='files'):
                query = query.replace("open ", "")
                subprocess.Popen(r'explorer /select,"C:/Users/Connor/Desktop"')
            speak("opened, sir")  

        elif 'what time is it' in query or 'what is the time' in query or "what's the time" in query:                                       
            srtTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {srtTime}")
        
        elif 'email mother dearest' in query or 'email mom' in query or 'email ma' in query:                              
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "prcccjordan@sbcglobal.net"                           
                sendEmail(to, content)
                speak("Email has been send!")
            except Exception as e:                                    
                print(e)
                speak("Sorry Connor sir. I am not able to send this email")

        elif 'email father dearest' in query or "email father" in query or "email dad" in query:                               
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "prcccjordan@att.net"                            
                sendEmail(to, content)
                speak("Email has been send!")
            except Exception as e:                                     
                print(e)
                speak("Sorry Connor sir. I am not able to send this email")

        elif 'email me' in query:                               
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "cj9366455@gmail.com"                             
                sendEmail(to, content)
                speak("Email has been send!")
            except Exception as e:                                     
                print(e)
                speak("Sorry Connor sir. I am not able to send this email")

        elif 'get weather' in query or "what's the weather" in query or 'what is the temperature' in query or 'what is the weather' in query or "what's the weather" in query or 'weather' in query or 'get the weather' in query:
            async def getweather():
                # declare the client. format defaults to metric system (celcius, km/h, etc.)
                client = python_weather.Client(format=python_weather.IMPERIAL)
                
                weather = await client.find("Germantown Tennessee")
                
                print(weather.current.temperature)
                
                for forecast in weather.forecasts:
                    print(str(forecast.date), forecast.sky_text, forecast.temperature)

                speak(str(weather.current.date))
                speak(str(weather.current.sky_text))
                speak(str(weather.current.temperature))

                
                await client.close()

            if __name__ == "__main__":
                loop = asyncio.get_event_loop()
                loop.run_until_complete(getweather())

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "who made you" in query or "who created you" in query or 'who designed you' in query:
            speak("I have been created by ComputerConnor.")

        elif "who are you" in query or 'what are you' in query:
            speak("I am your virtual assistant created by ComputerConnor")

        elif 'search' in query or 'play' in query:
             
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)
        
        elif "what's your purpose" in query or 'what is your purpose' in query or 'why were you designed' in query or 'what are your intentions' in query:
            
            speak("ComputerConnor got bored so he made me. That's literally the reason.")

        elif 'news' in query or 'what are the news' in query or "what's the news" in query:
             
            try:
                jsonObj = urlopen('https://newsapi.org/v2/top-headlines?country=us&apiKey=81494e2dcdd64b8198d1351b9ade12c0')
                data = json.load(jsonObj)
                i = 1
                 
                speak('here are some top news')
                print('''=============== NEWS  ============'''+ '\n')
                 
                for item in data['articles']:
                     
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    speak(item['description'] + '\n')
                    i += 1
                def input(key):
                    if key == 'enter':
                        exit()

            except Exception as e:
                 
                print(str(e))

        elif 'tell me a joke' in query:                                         
            print_and_speak(joke)

        elif 'come back in 30 minutes' in query:
            def countdown(m, s):
                total_seconds = m * 60 + s
                while total_seconds > 0:
                    timer = datetime.timedelta(seconds = total_seconds)
                    print(timer, end="\r")
                    time.sleep(1)
                    total_seconds -= 1
                    speak("Bzzzt! The countdown is at zero seconds!")
                    m = 30
                    s = 0
                    countdown(int(m), int(s))
                    speak("I'll come back in 30 minutes, sir")

        elif 'thank you' in query or 'stop' in query:                                         
            speak("you're welcome sir")
            exit()
        
        elif 'stop' in query:
            subprocess.call(["taskkill","/F","/IM","Code.exe"])

        elif 'terminate' in query:
            query = query.replace("terminate ", "")
            if (query=='Brave'):
                subprocess.call(["taskkill","/F","/IM","brave.exe"])
            if (query=='files'):
                subprocess.call(["taskkill","/F","/IM","explorer.exe"])
            speak("terminated, sir")

        elif 'turn off computer' in query or 'turn off the computer' in query or 'shut off the computer' in query or 'shut down the computer' in query:
            os.system("shutdown.exe /h")

        #later
        #elif 'remind me' in query:
            #query = query.replace("remind me", "")
            #speak("I will remind you of Truman")+Timer

            #elif 'lets chat' in query or 'lets talk' in query:
            #speak(first_question)