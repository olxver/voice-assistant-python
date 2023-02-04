


import speech_recognition as sr
import pyttsx3
import wikipediaapi
import random

# initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# initialize the tts engine
engine = pyttsx3.init()

# set the voice and rate
engine.setProperty('voice', 'en')
engine.setProperty('rate', 150)

# initialize Wikipedia
wiki = wikipediaapi.Wikipedia(
    language='en',
    extract_format=wikipediaapi.ExtractFormat.WIKI
)

while True:
    # reading main microphone as source
    # listening the speech and store in audio_text variable
    with sr.Microphone() as source:
        print("Listening...")
        audio_text = r.listen(source)


    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        # using google speech recognition
        recognized_text = r.recognize_google(audio_text)
        print("Text: "+recognized_text)

        exit_keywords = ["exit", "leave", "stop"] # list of keywords that the program listens for
        if any(keyword in recognized_text for keyword in exit_keywords): # if the keywords are found in the 'recognized_text' exit the program
            print("Exiting the program")
            break
        wiki_keywords = ["exit", "leave", "stop"]
        if any(keyword in recognized_text for keyword in wiki_keywords):  
            search_query = recognized_text.replace("search wiki", "").replace("what is", "").replace("tell me about", "").strip()
            page = wiki.page(search_query)
            if page.exists():
                summary = page.summary[0:250]
                engine.say("According to Wikipedia, " + summary)
                engine.runAndWait()
            else:
                engine.say("Sorry, I could not find any information on " + search_query)
                engine.runAndWait()
        greeting_keywords = ["hi", "hey", "hello"]
        if any(keyword in recognized_text for keyword in greeting_keywords):  
            rand = [
                "Hello there.",
                "Hey!",
                "Hi.",
                "Hello. What can I do for you?",
            ]
            randText = random.choice(rand)
            engine.say(randText)
            engine.runAndWait()

        else:
            engine.say("I'm not sure I understand. What do you mean by " + recognized_text)
            engine.runAndWait()

    except Exception as excep:
        print("Error: \n", excep) # if the code fails run this, e.g unable to reach google voice recognition




