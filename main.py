import speech_recognition as sr
import webbrowser
import pyttsx3
import musliclibrary
recognizer=sr.Recognizer()
engine=pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def aiProcess(command):
    completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {
            "role": "you are a virtual assistant name neko skilled in general task alexa and google",
            "content":command
        }
    ]
    )
    return completion.choices[0].message.content
def processCommand(c):
    if "open google"in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook"in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif c.lower().startswith("play"):
        song=c.lower().spilt(" ")[1]
        link=musliclibrary.music[song]
        webbrowser.open(link)
    else:
        output=aiProcess(c)
        speak(output)





    


if __name__ == "__main__":
    speak("Initializing neko....")
    while True:
        r=sr.Recognizer()
        print("recognizing")
        
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio=r.listen(source,timeout=2,phrase_time_limit=1)
            word=r.recognize_google(audio)
            if(word.lower()=="hello"):
                speak("yup")
                with sr.Microphone()as source:
                    print("Neko active...")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)

                    processCommand(command)
        except Exception as e:
            print("neko error;{0}".format(e))
