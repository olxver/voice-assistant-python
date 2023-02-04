# voice-assistant-python
a voice assistant written in python using speech_recognition and pyttsx3

- don't rely on this, this is just an example of what you can do with speech_recognition and pyttsx3 to make a 'voice assistant'

-----------------------
how to run on your own machine:

- download the files from here into a folder

- download python from https://www.python.org/downloads

- run in a command prompt: `pip install -r requirements.txt`

- when it finishes run the file by running: `py voice_rec.py` or `py example-tts.py`
- this may be different on macOS, Linux distros and Windows

- you can add different commands to this (scroll down to see how you can add)



how you can add your own commands to this:



```
import speech_recognition as sr
import pyttsx3

# initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# initialize the tts engine
engine = pyttsx3.init()

# set the voice and rate
engine.setProperty('voice', 'en')
engine.setProperty('rate', 150)

while True:
    with sr.Microphone() as source:
        print("Listening...")
        audio_text = r.listen(source)


  
    try:
        # using google speech recognition
        recognized_text = r.recognize_google(audio_text)
        print("Text: "+recognized_text)
        
        
        # create some keywords that you can say to the computer
        
        keywords = ["hello", "hi"] # add multiple with commas (you can change this to anything you like, just make sure you can say it)
        if any(keyword in recognized_text for keyword in keywords):  # check if the keywords are in the recognized text, if so run this
          print("hello world")
           engine.say("Hello World!") # with pyttsx3 say this (edit this to anything you like)
           engine.runAndWait()



    except Exception as excep:
        print("Error: \n", excep) #if unable to run, print this with the exception
```


- you can add anything you want to this, e.g apis or even deep learning models.
- mind, this can have some bugs so report them in 'issues' section
