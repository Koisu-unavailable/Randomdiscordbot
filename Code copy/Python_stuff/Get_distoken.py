global distoken
import tkinter as tk

from cusi import *



from json_edits import *

import keyboard

import asyncio as asio



def getdistoken(rooty):
    distoken = None
    root = rooty
    inputtoken = tk.Entry(width = 40)

    inputtoken.pack()


    notokentext = tk.Label(root,text = "You haven't entered your discord token yet", font = 24)
    notokentext.pack()
    def gettoken():
        distoken = inputtoken.get()
        if distoken != "":
            test = tk.Label(root, text = f"This is the token you inputed: {distoken[1:4]}(the rest is censored),  don't share it with anyone", font = 24, wraplength=500)
            test.pack()
            importoken(distoken)
    
    

        return notokentext.pack_forget()

    Enter = tk.Button(root, text="ENTER", command=gettoken)
    Enter.pack()
    return