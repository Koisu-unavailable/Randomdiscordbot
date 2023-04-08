global distoken
import tkinter as tk
from cusi import *
from json_edits import *
import keyboard
import asyncio as asio
from Get_distoken import *
import json_edits


class getinput:

       
    def obtain(self,rooty,question):
            entered = entery.get()
            if question != "token":
                if entered != "":
                    is_not_tokentext = tk.Label(rooty, text=f"You entered: {entered} is the correct?")
                    is_not_tokentext.pack()
                    importoken(entered)
            else:
                if entered != "":
                    censor = tk.Label(rooty, text= f"The first charaters are {entered[1:4]} is this correct?")
                    censor.pack()
                    importoken(entered)
            return entered
    def __init__(self, rootyy,question):
        global entery
        entery = tk.Entry(width=40)
        entery.pack()
        done = tk.Button(rootyy, text= "ENTER",command = getinput.obtain(self,rootyy,"token"))
        done.pack()
        notokentext = tk.Label(rootyy,text = f"You haven't entered your the bot's {question} yet", font = 24)
        notokentext.pack()

        
        text = tk.Label(rootyy,text = f"Input the bot's {question}")
        text.pack()

        return
    
            
        
        