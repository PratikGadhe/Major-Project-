import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    # Try using a female voice (optional)
    if len(voices) > 1:
        engine.setProperty('voice', voices[1].id)  # On most systems, 1 = female
    
    engine.setProperty('rate', 150)  # Speed
    engine.setProperty('volume', 1.0)  # Max volume
    engine.say(text)
    engine.runAndWait()
