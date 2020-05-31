import time
from performcommands import Commander
import getcommands as gc
import sys

if __name__ == "__main__":

    
    cmd= Commander()    
    wakeword = 'easy assistant'
    while True:
         
        command =gc.getCommand(0)
        if command == wakeword:
            command= gc.getCommand(1)

            if command in['quit','goodbye','exit','bye','bye-bye','stop','end']:
                cmd.respond("OK Bye.")
                sys.exit()
            
            cmd.doCommand(command)
        
