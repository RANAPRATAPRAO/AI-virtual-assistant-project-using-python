# dependicies required for the project
# 1. pip install pyttsx3.
# this will convert text to speech
# 2. pip install speechRecognition
# this will take command from the user
# 3. install 'pyaudio' library also here
# 4. pip install "wikipedia" for search
# 5. pip install "pyautogui" for the screenshot of the live
# screen

# text to speech
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb  # for chromme search
import os  # for the shutdown lock and sleep
import pyautogui

engine = pyttsx3.init()


# engine.say("this is rana")
#  engine.runAndWait()
# End of text to speech


# here we created one function speak who convert text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# fuction for the date time
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)


# time()

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    Date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(Date)
    speak("month")
    speak(month)
    speak("annd year is")
    speak(year)


# date()

# greeting function for us
def greetMe():
    speak("welcome back sir ")
    # speak("the ccurrent time is")
    # time()
    # speak("the current date is")
    # date()
    speak("jarvis at your service please tell me how can I help you")


# greetMe()


# speech recognition to take input command from the user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("say that again please")
        return "None"
    return query


# takeCommand()

# send email function
def sendmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('chumtiya000@gmail.com', 'Rana@123')
    server.sendmail('chumtiya000@gmail.com', to, content)
    server.close()


# function for screent shot
def screenshot():
    img = pyautogui.screenshot()
    img.save("D:\pythonProject2\jarvis\main.png")


# the main funnction
if __name__ == "__main__":
    greetMe()
    while True:
        query = takeCommand().lower()
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            speak("searching....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif "send email" in query:
            try:
                speak("what should I say ")
                content = takeCommand()
                to = "sumitkumarbaatiah@gmail.com"
                sendmail(to, content)
                speak(content)
            except Exception as e:
                print(e)
                speak("unable to send email")
        elif "search in chrome" in query:
            speak("what should i search, sir")
            chromepath = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')
        # for system shutdown and restart
        elif "logout" in query:
            os.system("shutdown -1")
        elif "shutdown" in query:
            os.system("shutdown /t /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        # play songs
        elif "play songs" in query:
            song_dir = "D:\java_dsa\apti"
            songs = os.listdir(song_dir)
            os.startfile(os.path.join(song_dir, songs[0]))
        # remembering the things
        elif 'remember that ' in query:
            speak("what should i remember")
            data = takeCommand()
            speak("you said me to remember  that" + data)
            remember = open('data.txt', 'w')  # for remember the things we have to create one file
            remember.write(data)
            remember.close()
        # asking the remember the things
        elif "do you know anything " in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember this" + remember.read())
        # for screenshot
        elif "screenshot" in query:
            screenshot()
            speak(" done sir")
        # for offline the assistent
        elif "offline" in query:
            speak("ok sir , have a great day")
            quit()
