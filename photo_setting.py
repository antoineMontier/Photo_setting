import os
import pyautogui
import time
import sys
import pyperclip

class Date:
    def __init__(self, year, month, day, hour, minute, second):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d} {self.hour:02d}:{self.minute:02d}:{self.second:02d}"

def find_date():
    date_position = pyautogui.locateOnScreen('picture.png')
    date_X = date_position[0] # width position  (X)
    date_Y = date_position[1] # height position (Y)
    # perform double clic to select the date : 
    pyautogui.leftClickHandler


time.sleep(3)
find_date()


""""
1491
523
48
45

1491
468
48
45
"""