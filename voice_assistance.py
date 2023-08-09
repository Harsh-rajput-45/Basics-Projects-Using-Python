# pip install pyaudio

import pyttsx3  # pip install pyttsx3 for text to speech conversion
import speech_recognition as sr  # pip install speechRecognition
import datetime           
import wikipedia  # pip install wikipedia
import webbrowser   # pip install webbrowser
import os           # pip install os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hi Harsh !")
    


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
       # speak("Listening...")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
       # speak("Recognizing...")
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        # speak("Say that again please...")
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening Youtube for you")
            print("Opening Youtube for you")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening google for you")
            webbrowser.open("google.com")
        elif 'open whatsapp' in query:
            speak("Opening Whatsapp for you")
            webbrowser.open('whatsapp.com')
        elif 'open facebook' in query:
            speak("Opening facebook for you")
            webbrowser.open('facebook.com')
        elif 'open instagram' in query:
            speak("Opening instagram for you")
            webbrowser.open('instagram.com')
        elif 'open amazon' in query:
            speak("Opening Amazon for you")
            webbrowser.open('amazon.in')
        elif 'open flipkart' in query:
            speak("Opening flipkart for you")
            webbrowser.open('flipkart.in')  
        elif 'open stackoverflow' in query:
            speak("Opening stackoverflow for you")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\song'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "D:\PYTHON"
            os.startfile(codePath)
        elif 'email to our team' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "......@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry harsh. I am not able to send this email")
        else:
            print("No query matched")
            
