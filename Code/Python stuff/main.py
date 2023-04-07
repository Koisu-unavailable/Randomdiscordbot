import tkinter as tk
from cusi import *
import json
from json_edits import *
import keyboard


root = tk.Tk()
root.geometry("490x490")





inputtoken = tk.Entry(width = 40)

inputtoken.pack()
def getinput(distoken):
    if keyboard.is_pressed('a') == True:
        distoken = inputtoken.get(); print(distoken)
        test = tk.Label(text = f"This is the token you inputed:", font = 24)
        test.pack()
    else:
        notokentext = tk.Label(text = "You haven't entered your discord token yet", font = 24)
        notokentext.pack()

    return distoken
root.after(3000, getinput(0))
getinput(0)



root.mainloop()


