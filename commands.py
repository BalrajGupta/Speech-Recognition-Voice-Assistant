# only basic google search commands added. More functionality can easily be added later.
#oppens basic apps downloaded from the Microsoft store like Netflix,Instagram
import os
import win32com.client as wincl
from getanswers import Fetcher
class Commander:
    def __init__(self):
        self.confirm=['yes','affirmative','yeah','sure','confirm']
        self.cancel =['no',"don't","cancel","negative"]
    
    def discover(self,text):
        if "what" in text and "your name" in text:
            self.respond("My name is Assistant. What can I do for you?")
        
        if "open" or "launch" in text:
            app = text.split(" ",1)[-1]
            self.respond("Opening "+app)
            os.system('start '+app+':')
        
        
        else:
            f=Fetcher('https://www.google.com/search?q='+text)
            answer =f.lookup()
            self.respond(answer)
            
    
    def respond(self,text):  
        print(text)
        speak = wincl.Dispatch("SAPI.SpVoice")
        speak.Speak(text)
       
            
