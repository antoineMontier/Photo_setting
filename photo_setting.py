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
		return

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
		if not date_str.startswith("20") :
			print("Invalid date, date is ", date_str, " in filename ", filen)
			return None
		year 	= date_str[:4]
		month  	= date_str[4:6]
		day		= date_str[6:]

		hour 	= time_str[:2]
		min		= time_str[2:4]
		sec		= time_str[4:]

		return Date(int(year), int(month), int(day), int(hour), int(min), int(sec))

	return None

def check_date(date):
	if date == None:
		return False
	if(date.year < 2003 or date.year > 2023):
		return False
	if(date.month < 1 or date.month > 12):
		return False
	if(date.day < 1 or date.day >30):
		return False
	if(date.hour < 1 or date.hour >24):
		return False
	if(date.minute < 1 or date.minute >60):
		return False
	if(date.second < 1 or date.second >60):
		return False
	return True # all test passed


def set_date(d):
	#find the pen : to modify the date
	# Define the search region
	search_region = (1470, 217, 449, 304)

	# Search for the image in the specified region
	image_location = pyautogui.locateOnScreen("pen.png", region=search_region)

	if image_location:
		center_x = image_location.left + image_location.width  // 2
		center_y = image_location.top  + image_location.height // 2
	else:
		print("Image not found in the specified region.")

	# perform a click on the pen : 
	pyautogui.leftClick(center_x, center_y)



time.sleep(3)
set_date(None)

"""
# Get the current mouse cursor position
mouse_x, mouse_y = pyautogui.position()

print("X :", mouse_x)
print("Y :", mouse_y)
"""

"""
top-left : 
X : 1470
Y : 217

top-right :
X : 1919
Y : 174

bottom-left :
X : 1472
Y : 521

bottom-right :
X : 1919
Y : 532
"""










"""
nb_photos = 0
time.sleep(3)
date = find_date()
if not check_date(date):
	print ("date is not correct : ", date)
else:
	nb_photos += 1
"""







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