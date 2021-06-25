import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyjokes
import pywhatkit
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Alisha. how may i help you this time")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
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


def sendmail(to, content):
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
            speak("Hope that helps, i can tell you more if you ask me briefly")

        elif 'who is' in query:
            person = query.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            speak(info)
            speak("If you still want to know more, then try to be more precise.")

        elif 'hello' in query:
            speak('Hi there, Whats up')

        elif 'who are you' in query:
            speak('I am your friend, Alisha')

        elif 'our university ' in query:
            speak("It is situated near second stage")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'college website' in query:
            speak("Opening in new tab")
            webbrowser.open("msruas.ac.in")

        elif 'students portal' in query:
            speak("why not! Here you go")
            webbrowser.open("ruasportal.msruas.ac.in")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing you ' + song)
            pywhatkit.playonyt(song)

        elif 'joke' in query:
            speak(pyjokes.get_joke())
            speak("If you want to listen to more then say yes or else tell me when you are done")

        elif 'yes' in query:
            speak(pyjokes.get_joke())
            speak("do you still want to listen to more jokes")

        elif 'i am done' in query:
            speak("Hope i gave a smile on your face. keep smiling. As it is very good for your health")

        elif 'play music' in query:
            music_dir = 'D:\\Favourite\\songs\\good_vives'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'thank you' in query:
            speak("Its my pleasure to serve you, just speak out my name anytime you need me")

        elif 'email to Amar' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "djlovesallbut5467yo@gmail.com"
                sendmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")
