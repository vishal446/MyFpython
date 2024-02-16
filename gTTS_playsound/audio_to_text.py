import speech_recognition as sr
voice=sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Now")
    audio=voice.listen(source)
    try:
        text=voice.recognize_google(audio)
        print("You said:",text)
    except:
        print("Your voice in not clear")