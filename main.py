import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

r = sr.Recognizer()
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.runAndWait()

def take_command():
    while (1):
        try:
            with sr.Microphone() as source2:
                print("listening...")
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                command = r.recognize_google(audio2)
                command = command.lower()
                # print("Did you say " + command)
                # SpeakText(MyText)

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("unknown error occured")
        return command

def run_virtual_assistant():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play","")
        SpeakText("Playing "+song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        SpeakText("Current time is "+time)
    elif "who the heck is" in command:
        person = command.replace("who the heck is","")
        info = wikipedia.summary(person, 1)
        print(info)
        SpeakText(info)
    elif "date" in command:
        SpeakText("Sorry, I have a headache")
    elif "are you single" in command:
        SpeakText("I am in a relationship with wifi")
    elif "joke" in command:
        SpeakText(pyjokes.get_joke())
    elif "who is" in command:
        person = command.replace("who is","")
        info = wikipedia.summary(person, 1)
        print(info)
        SpeakText(info)
    elif "who am i" in command:
        SpeakText("You are Istiak")
    elif "am i single" in command:
        SpeakText("Of course not! You are in relationship with Quantum World.")
    else:
        SpeakText("Please say the command again")

while True:
    run_virtual_assistant()