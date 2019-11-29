import pyttsx3
import win32com.client
engine = pyttsx3.init(driverName='sapi5')
engine.say('Sally sells seashells by the seashore.')
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()