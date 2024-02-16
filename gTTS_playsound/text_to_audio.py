from gtts import gTTS
from playsound import playsound
def save_audio(text):
    print(text)
    tts=gTTS(text)
    tts.save('a.mp3')
    speak_to_text('a.mp3')
def speak_to_text(audio_path):
    playsound(audio_path)

save_audio("Hello Guy's! Aur bataao maje mein ho? thoda padh wadh "
           "liya karo kabhi kabhi And listen one thing! My voice is "
           "designed by vishal and this is first speaking program of vishal")
# save_audio("")