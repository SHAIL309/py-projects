import pyttsx3
from PyDictionary import PyDictionary
class speaking:
	def speak(self, audio):
		
		# intial const of pytssx3 and sapi5 as it's parameter
		engine = pyttsx3.init('sapi5')
		
		# calling getter setter of pyttsx3
		voices = engine.getProperty('voices')
		
		# method for speaking of assistnat
		engine.setProperty('voices', voices[0].id)
		engine.say(audio)
		engine.runAndWait()
class GFG:
	def dictionary(self):
		speak =speaking()
		dic = PyDictionary()
		speak.speak("which wird do u want to find meaning of ??? \n:")
		query = str(input())
		word  = dic.meaning(query)
		print(len(word))

		for state in words:
			print(word[state])
			speak.speak("the meaning is " + str(word[state]))
if __name__ == '__main__':
	GFG()
	GFG.dictionary(self=None)