import speech_recognition	
import pyttsx3
from datetime import date, datetime

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
voices = robot_mouth.getProperty('voices')
robot_mouth.setProperty('voice', voices[1].id) 

while True: 
	with speech_recognition.Microphone() as mic:
		print("PASSWORD")
		audio = robot_ear.record(mic, duration = 7)	
		print(".........")					
	try:
		you = robot_ear.recognize_google(audio, language="en-us")							
	except:
		you = ""
	if "909" in you:
		robot_brain = "correct"
		print("Robot :" + robot_brain)
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	elif you == "":
		robot_brain = "enter PASSWORD"

	else:
		robot_brain = "PASSWORD is wrong"


	print("Robot :" + robot_brain)
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()
print("----------")
hour=datetime.now().hour
if hour >= 6 and hour<12:
    welcome_0 = "Good Morning Sir!"
elif hour>=12 and hour<18:
    welcome_0 = "Good Afternoon Sir!"
elif hour>=18 and hour<24:
    welcome_0 = "Good Evening sir"
welcome_2 = "How can I help you,boss"
print("T.U.E.S.D.A.Y :" + welcome_0)
print("T.U.E.S.D.A.Y :" + welcome_2)
robot_mouth.say(welcome_0 + welcome_2)
robot_mouth.runAndWait()

while True: 
	with speech_recognition.Microphone() as mic:
		print("T.U.E.S.D.A.Y: I'm listening ")
		audio = robot_ear.record(mic, duration=5)						#listen
	print("T.U.E.S.D.A.Y: i got it")
	try:
		you = robot_ear.recognize_google(audio, language="en-us")							#language="vi"   nghe tiếng việt
	except:
		you = ""

	print("You :" + you)
	if "hello" in you:
		robot_brain = "hello boss"
	elif you == "" :
		robot_brain = "what can i help you ?"
	elif "today" in you:
		today = date.today()
		robot_brain = today.strftime("%B %d, %Y")
	elif "time" in you:
		now = datetime.now()
		robot_brain = now.strftime("%H hours %M minutes %S seconds")
	elif "handsome" in you:
		robot_brain = "of course"	
	elif "bye" in you:
		robot_brain = "see you boss"
		print("T.U.E.S.D.A.Y :" + robot_brain)
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	else:
		robot_brain ="i don't know that "

	print("T.U.E.S.D.A.Y :" + robot_brain)
	print("----------")
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()