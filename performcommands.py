# basic google search commands added. 
# opens  apps downloaded from the Microsoft store like Netflix,Instagram
# searches wikipedia to give descriptive info
# take notes
# tell the weather
import os
import win32com.client as wincl
from webanswers import Fetcher
import getcommands as gc
import requests
import subprocess
from pyowm import OWM
import re
import datetime
import wikipedia
import geocoder as geo


class Commander:
    def __init__(self):
        self.confirm=['yes','affirmative','yeah','sure','confirm']
        self.cancel =['no',"don't","cancel","negative"]

    def respond(self,text):  
        
        speak = wincl.Dispatch("SAPI.SpVoice")
        print(text)
        speak.Speak(text)
        
    def note(self,text):
        date = datetime.datetime.now()
        file_name = str(date).replace(":", "-") + "-note.txt"
        with open(file_name, "w") as f:
            f.write(text)
        subprocess.Popen(["notepad.exe", file_name])
    
    def getfromwiki(self,reg_ex):
        answer=""
        try:
            if reg_ex:
                topic = reg_ex.group(1)
                ny = wikipedia.page(topic)            
                answer =ny.content[:500]
                answer=answer[1:answer.rindex('.')+1].encode('utf-8')
        except :
            answer ="Sorry. Nothing Found."

        return answer 
    
    def getweather(self,city):

        obj = OWM(API_key='25ef120c4b2a885708316bab31e416e9')
        x= obj.weather_at_place(city)
        weather= x.get_weather()
        temp = weather.get_temperature(unit='celsius')
        cond= weather.get_detailed_status()
        answer='Currently in %s, the current temperature is %0.2f degree Celsius and there is a %s.' % (city,temp['temp'], cond)
        return answer

    def doCommand(self,text):
        #SMALL TALK
        if "what" in text and "your name" in text or text== 'hello' or text =='hi':
            
            self.respond("Hi. My name is Easy Assistant. What can I do for you?")
        
        #HELP
        elif  text =="help" or text =="what can yo do" :
            self.respond("Hi. You can use me to do the following\n1. Open Apps by saying open\n2. make notes\n3. Ask about the weather\n4. Ask me about any topic ")

        #OPEN APPS DOWNLOADED FROM MICROSOFT STORE
        elif "open" in text  or "launch" in text:
                
            app = text.split(" ",1)[-1]
            self.respond("Opening "+app)
            os.system('start '+app+':')

        #MAKE A NOTE IN NOTEPAD
        elif ('make'in text or 'take' in text) and 'note' in text or "write this down"in text or "remember this" in text:
            self.respond("What do you want me to write down?") 
            tonote= gc.getCommand()
            self.note(tonote)
            self.respond("I've made a note of that.")
       
        #GET WEATHER INFO
        elif('tell' in text or "what's" or "how is" in text) and('weather'in text or 'the day' in text or 'today' in text):
            reg_ex = re.search('weather in (.*)', text)
            if reg_ex:
                city = reg_ex.group(1)

            elif re.search('day in (.*)', text):
                reg_ex=re.search('day in (.*)', text)
                city = reg_ex.group(1)
            else:
                g = geo.ip('me')
                city=str(g.city)
            city=city.title()
            answer= self.getweather(city)
            self.respond(answer)
        
        # GET DESCRIPTIVE INFO FROM WIKIPEDIA
        elif ('tell me' or 'i want to know ' in text) and 'about' in text :
            
            reg_ex = re.search('about (.*)', text)
            answer= self.getfromwiki(reg_ex)
            self.respond(answer)
            
        # GOOGLE QUERIES
        elif 'what' in text or 'who' in text or 'whom' in text or 'when' in text or 'how' in text or 'where' in text or 'when' in text:
                
                f=Fetcher()
                answer =f.lookup('https://www.google.com/search?q='+text)
                self.respond(answer)

        else:
            self.respond("Sorry. I can't help with that yet.")
                
