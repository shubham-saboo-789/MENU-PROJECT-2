import pyttsx3




def text_speech_api(text):
    print(text)
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Convert text to speech
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()

