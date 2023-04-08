global distoken
import tkinter as tk

from cusi import *



from json_edits import *

import keyboard

import asyncio as asio

from Get_distoken import *
from Get_input import *

root = tk.Tk()
root.geometry("490x490")
root.title("I need a title for the app")
ico = tk.PhotoImage(file = "Code\Python_stuff\monitor_desktop_icon_251871.ppm")
root.iconphoto(True, ico)

getdistoken(root)










root.mainloop()


