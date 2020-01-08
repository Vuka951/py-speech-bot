import speech_recognition as sr

r = sr.Recognizer()

def record_audio():
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print('No abla!')
        except sr.RequestError:
            print('Server Dead!')
        return voice_data

print('Whachu want')
voice_data = record_audio()
print(voice_data)