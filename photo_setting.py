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

def get_filename():
	pyautogui.hotkey("ctrl", "a") # select all
	pyautogui.hotkey("ctrl", "c") # copy   all
	page_text = pyperclip.paste()
	# split the text to take only the name of the file
	page_array = page_text.splitlines()

	#possible extensions of filenames
	extensions = {"jpg", "mp4", "png"}

	filename = "-"

	for line in page_array:
		for ext in extensions:
			if line.endswith(ext):
				filename = line
	
	if filename == "-" :
		print ("ERROR : no ext : \n",  page_text)

	print ("filename : ", filename)

	return filename

def find_date():
	filen = get_filename()
	filen = filen.split(".")[0] # remove extension
	if filen.startswith("Snapchat") : # no date info in the title of snapchat files
		return None
	
	if filen.startswith("IMG") :  
		infos = filen.split("_")
		date_str = infos[1]
		time_str = infos[2]
		print("date ", date_str, "time ", time_str)


time.sleep(3)
find_date()



"""
Press question mark to see shortcut keys available
Info
Add a description
Add a description
DETAILS
24 Aug
Thu, 03:37
GMT+02:00
VID_31501031_045248_335.mp4
0.9 MP
720 × 1280
Uploaded from a web browser
Backed up (1.9 MB)
Original quality. Learn more
Add a location
Video – Portrait – 24 Aug 2023, 03:37:20
"""