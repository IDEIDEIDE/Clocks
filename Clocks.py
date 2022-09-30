#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 09:19:37 2022

@author: clockshield
"""

from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time
root = Tk()
root.geometry("600x450")
clock_image = ImageTk.PhotoImage(Image.open("clock.jpg"))


india_label = Label(root, text = "India")
india_label.place(relx = 0.2, rely = 0.05, anchor = CENTER)

india_clock = Label(root)
india_clock["image"]= clock_image
india_label.place(relx = 0.2, rely = 0.5, anchor = CENTER)
    
india_time = Label(root)
india_time.place(relx = 0.2, rely = 0.75, anchor = CENTER)


usa_label = Label(root, text = "USA")
usa_label.place(relx = 0.7, rely = 0.05, anchor = CENTER)

usa_clock = Label(root)
usa_clock["image"]=clock_image
usa_label.place(relx = 0.7, rely = 0.5, anchor = CENTER)

usa_time = Label(root)
usa_time.place(relx = 0.7, rely = 0.75, anchor = CENTER)

class India():
    def times(self):
        home = pytz.timezone('Asia/Kolkata')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        india_time["text"] = "Time :" + current_time
        india_time.after(200,self.times)
class usa():
    def times(self):
        home = pytz.timezone('US/Central')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        usa_time["text"] = "Time :" + current_time
        usa_time.after(200,self.times)
        
        
obj_india = India()
obj_usa = usa()        
india_button = Button(root, text = "Show Time", command = obj_india.times)
india_button.place(relx = 0.2, rely = 0.9, anchor = CENTER)


usa_button = Button(root, text = "Show Time", command = obj_usa.times)
usa_button.place(relx = 0.7, rely = 0.9, anchor = CENTER)
root.mainloop()