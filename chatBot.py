import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def greet(): 
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning Sir!')
    elif hour>=12 and hour<=16:
        speak('Good Afternoon Sir!')
    else:
        speak('Good Evening Sir!')
    speak(" I'm Veronica. How Can i help You Today?")        

def takeInstructions():
    recognize = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...........')
        recognize.pause_threshold=1
        recognize.energy_threshold=1500
        audio = recognize.listen(source)
        
    try :
        print('Recognizing........')
        query = recognize.recognize_google(audio, language='en-in')
        print("You Said ", query)
    except Exception as e:
        print(e)
        speak("Sorry! i didn't get you!")
        return "None"
    return query       
    
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__=='__main__':
    greet()
    while True:
        query = takeInstructions().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            print('Searching Wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            print('According To Wikipedia')
            speak('According To Wikipedia')
            print(results)
            speak(results)
        elif 'open google' in query:
            speak('Opening Google')
            webbrowser.open('Google.com')
        elif 'open stackoverflow' in query:
            speak('Opening StackOverFlow')
            webbrowser.open('stackoverflow.com')
        elif 'the time' in query:
            timeInString = datetime.datetime.now().strftime("%H:%M:%S")
            print("Time : ", timeInString)
            speak("Sir! The time is {}".format(timeInString))
        elif 'open youtube' in query:
            webbrowser.open('Youtube.com')
            speak('Opening YouTube')
        elif 'open code' in query:
            codeLocation = "C:\\Users\\Dell pc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak('Opening VS code')
            os.startfile(codeLocation)
        elif 'quit' in query:
            speak('I will be in the Background, call me when needed')
            break
        elif 'who are you' in query:
            print("Hyy, i'm Veronica ,a virtual assistant developed by Shubhanshu Jain, used for  personal assistance of  Shubhanshu for his daily assistance like searching Wikipedia, playing audiobooks, opening WebPages and other real-time information, such as time.")    
            speak("Hy, i'm Veronica ,a virtual assistant developed by Shubhanshu Jain, used for  personal assistance of  Shubhanshu for his daily assistance like searching Wikipedia, playing audiobooks, opening WebPages and other real-time information, such as time.")
        else :
            speak("It's not relevant, try something else!")