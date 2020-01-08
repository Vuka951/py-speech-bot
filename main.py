import speech_recognition as sr
import webbrowser
import time

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print('No abla!')
        except sr.RequestError:
            print('Server Dead!')
        return voice_data

def respond(voice_data):
    print(f'You said: {voice_data}')
    if voice_data in ['whatsapp', 'sup']:
        print('Not much')
    elif voice_data in ['who you', 'who are you']:
        print('Ugly Pussy Nigga')
    elif voice_data in ['time beach', 'time bich', 'time bitch']:
        print(time.ctime())
    elif voice_data == 'google':
        search = record_audio('Google what?')
        url = f'https://google.com/search?q={search}'
        webbrowser.get().open(url)
        print(f'Catch this fade for {search}')
    elif voice_data == 'find':
        place = record_audio('Find What?')
        url = f'https://google.nl/maps/place/{place}/&amp;'
        webbrowser.get().open(url)
        print(f'Im sippin tea in {place}, WHAT THE FUKC IS UP')
    elif voice_data == 'die':
        exit()

print('Whachu want')

while True:
    voice_data = record_audio().lower()
    respond(voice_data)
