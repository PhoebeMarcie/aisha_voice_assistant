import speech_recognition as sr
import webbrowser
import datetime
import subprocess
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime


# Commands that Aisha responds to

NOTE_STRS =["make a note", "remember this", "write this down"]
LOCATION_STRS=["find place", "locate a place", "look for a place", "find a place"]
EXIT_STRS=["thank you ", "sleep", "exit", "goodbye", "rest now", "enough"]#to exit
r = sr.Recognizer()


# get voice data through the microphone.
def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            Aisha_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            Aisha_speak('Sorry I did not get that')
        except sr.RequestError:
            Aisha_speak('Sorry, my speech service is down')
        return voice_data
        
def Aisha_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":","-")+ "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])

def respond(voice_data):
    if 'what is your name' in voice_data:
        Aisha_speak('My name is Aisha')
    if 'who are you' in voice_data:
        Aisha_speak('My name is Aisha, I am a voice assistant. How can I help?')
    if 'what is the time' in voice_data:
        Aisha_speak(ctime())
    if 'what time is it' in voice_data:
        Aisha_speak(ctime())
    if 'search'  in voice_data:
        search = record_audio('what do you want to search for?')
        url =  'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        Aisha_speak('Here is what i found for ' + search)
    if 'play music' in voice_data:
         webbrowser.open("https://www.youtube.com/", new=2)
         Aisha_speak('Opening Youtube')
    if 'play songs' in voice_data:
            music_dir = 'E:\\music\\favourites'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            Aisha_speak('Playing music from your PC')
    if 'movie time' in voice_data:
         webbrowser.open("https://www.youtube.com/", new=2)
         Aisha_speak('Opening Youtube')
    # if 'find location' in voice_data:
    #     location = record_audio('what is the location?')
    #     url =  'https://google.nl/maps/place/' + location + '/&amp;'
    #     webbrowser.get().open(url)
    #     Aisha_speak('Here is the location of  ' + location)
    # if 'find place' in voice_data:
    #     place = record_audio('what is the location?')
    #     url =  'https://google.nl/maps/place/' + place + '/&amp;'
    #     webbrowser.get().open(url)
    #     Aisha_speak('Here is the location of  ' + place)
    for phrase in LOCATION_STRS:
        if phrase in voice_data:
            place = record_audio('what is the location?')
            url =  'https://google.nl/maps/place/' + place + '/&amp;'
            webbrowser.get().open(url)
            Aisha_speak('Here is the location of  ' + place)


    for phrase in NOTE_STRS:
        if phrase in voice_data:
            Aisha_speak('What would you like me to note down?')
            note_text = record_audio().lower()
            note(note_text)
            Aisha_speak('I have made a note of that.')

    for phrase in EXIT_STRS:
        if phrase in voice_data:
            exit()
    # if 'exit' in voice_data or 'sleep' in voice_data or 'bye sakura' in voice_data:
    #     exit()
    
    
    
time.sleep(1)
Aisha_speak('How can i help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
