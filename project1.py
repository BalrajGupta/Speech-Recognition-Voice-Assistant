import time
import speech_recognition as sr
import pyaudio
import wave
from commands import Commander    
import sys

r= sr.Recognizer()
cmd= Commander()
def playaudio(filename):
    chunk = 1024
    f = wave.open(filename,'rb')
    pa = pyaudio.PyAudio()
    stream = pa.open(
        format = pa.get_format_from_width(f.getsampwidth()),
        channels = f.getnchannels(),
        rate = f.getframerate(),
        output =True
        )
    datastream = f.readframes(chunk)
    while datastream:
        stream.write(datastream)
        datastream= f.readframes(chunk)
        
    stream.close()
    pa.terminate()

    
def initSpeech():
    
    print("Listening...")
    playaudio("audiofiles/start.wav")
    with sr.Microphone() as source:
        print("Say Something bro")
        audio = r.listen(source)
    playaudio("audiofiles/end.wav")
    
    recognized=""
    
    try:
        recognized= r.recognize_google(audio)
    except:
        print("Couldnt get you bro.")
        return
    
    
    print(recognized)
    if recognized in['quit','goodbye','exit','bye','stop']:
       sys.exit()
       
    if stat is True:   
        cmd.discover(recognized)
    
    
        
stat=True
while stat == True:
    time.sleep(2)    
    initSpeech()
