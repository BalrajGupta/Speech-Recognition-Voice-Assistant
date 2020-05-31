import speech_recognition as sr
import pyaudio
import wave



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

def getCommand( status):
    
    r= sr.Recognizer()
    if status == 1: 
        print("Listening...")
        playaudio("audiofiles/start.wav")
    with sr.Microphone() as source:
        audio = r.listen(source)
    if status == 1:
        playaudio("audiofiles/end.wav")
    recognized=""
    
    try:
        recognized= r.recognize_google(audio).lower()
    except:
        if status == 1:
            recognized ="Couldn't get you bro".lower()

        else:
            recognized ="...".lower()

    
    print(recognized.title())
    return recognized
    
 