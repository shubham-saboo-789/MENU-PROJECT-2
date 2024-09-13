import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

text = "Hello, how are you?"

# Convert text to speech
engine.say(text)

# Wait for the speech to finish
engine.runAndWait()
