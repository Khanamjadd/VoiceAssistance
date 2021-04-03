import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import datetime
import random
import string




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning Mr. Amjad!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon Mr. Amjad!")
    else:
        speak("Good Evening Mr. Amjad!")
    speak("I am Jarvis, Sir please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    

    except Exception as e:
        print("Say that again please...")
        return "None"

    return query



if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak(f'searching {query}')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak("According to the wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = "C:\\Users\\sachin\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, random.choice(songs)))
            

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {strTime} o'clock right now") 

        elif 'write' in query:
            speak("Mr. Amjad, What should I have to write in messege?")
           
            with open("newMsg.txt", 'a') as f:
                msg = takeCommand()    
                a = f.writelines()
            print(msg)
            speak(msg)      

        elif 'quit' in query:
            speak("Thank you mr. amjad, have a great time ahead ")  
            quit()