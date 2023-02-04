import pyttsx3

# Initialize the engine
engine = pyttsx3.init()

# Get the list of available voices
voices = engine.getProperty('voices')

# Set the voice to 'english-us'
engine.setProperty('voice', voices[1].id)

# Speak the text
engine.say("Hello, How can I help you?")
engine.runAndWait()
