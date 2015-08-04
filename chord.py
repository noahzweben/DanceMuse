from music import *
from random import *
from MusicFunctions import *
from MarkovChords import *

class Chord:

	chordProg = MarkovChords(C2,'./myproj/markov.csv')

	def __init__(self,channel=0,chord =[C3,E3,G3], key = MAJOR_SCALE, baseNote = 0,octaveRange =None):
		self.notes = chord
		self.channel = channel
		Play.setInstrument(97,self.channel)
		self.volume = 127
		self.key = createKey(key,baseNote)
		self.octaveRange = octaveRange
		self.timers = {}
		self.currentChord = "C"

	def play(self,duration = 0):
		for note in self.notes:
			Play.noteOn(note,self.volume,self.channel)
			# else:
			# 	Play.note(note,127,duration) ### CHECK THAT THIS IS RIGHT PARAMETER ORDER

	def end(self):
		for note in self.notes:
			Play.noteOff(note,self.channel)



######## Chord Changes ###############
	def newNotes(self, newNotes, nowStart = True):
		"""
		Changes the chord playing. If nowStart is set to True, will start playing
		immediately
		"""

		self.end()
		if type(newNotes) == int:
			newNotes = [newNotes]
		self.notes = newNotes
		if nowStart == True: 
			self.play()

	def shift(self,amount, notes= [], inKey = True, nowStart = True,):
		""" Shifts the chord by the specified amount. If amount is given as list i.e. [-4,4] will shift 
		randomly within that interval. If notes is set, will only shift the notes 
		of the chord corresponding to the note indexes supplied"""
	
		if type(amount)==list:
			maxval,minval = amount
			shiftVal = mapValue(random(),0,1,minval,maxval)
		else:
			shiftVal = amount
			
		if len(notes)==0:
			notes = range(len(self.notes))

		newNotes = self.notes[:]
		for i in notes:
			newNotes[i] = newNotes[i] + shiftVal

		if inKey == True:
			newNotes = enforceKey(newNotes,self.key)

		if self.octaveRange is not None:
			newNotes = enforceOctave(newNotes,self.octaveRange)

		self.newNotes(newNotes, nowStart = nowStart)

	def randomChord(self,rangeVal=[-12,12],inKey=True,nowStart = True):
		newNotes = []
		for i in range(len(self.notes)):
			maxval,minval = rangeVal
			shiftVal = mapValue(random(),0,1,minval,maxval)
			newNotes.append(self.notes[i]+shiftVal)
		
		if inKey == True:
			newNotes = enforceKey(newNotes,self.key)
		if self.octaveRange is not None:
			newNotes = enforceOctave(newNotes,self.octaveRange)

		self.newNotes(newNotes, nowStart = nowStart)

	def progressChord(self,nowStart = True):
		self.currentChord,newNotes = self.chordProg.nextChord(self.currentChord)
		self.newNotes(newNotes, nowStart = nowStart)


### Random and Automated Effects ####	s
	def autoRandomChord(self,interval,rangeVal=[-12,12],inKey = True):
		self.randomChord(rangeVal,inKey)
		self.stopFX("autoRandomChord")
		self.timers["autoRandomChord"]= Timer(interval, self.randomChord,[rangeVal,inKey])
		self.timers["autoRandomChord"].start()




	def autoProgressChord(self, interval=0): 
		"""Switches chord to one in supplied set every
		interval seconds. If amount is set to 'R' will 
		just shift randomly within supplied chords"""

		self.progressChord()
		self.stopFX("autoProgressChord")
		self.timers["autoProgressChord"] = Timer(interval,self.progressChord)
		self.timers["autoProgressChord"].start()



	######################

	# Automates shifting the chord up and down. 
	def autoShift(self, amount, interval, notes=[],  inKey=True): 

		self.shift(amount,notes, inKey)
		self.stopFX("autoShift")
		self.timers["autoShift"] = Timer(interval,self.shift,[amount,notes,inKey])
		self.timers["autoShift"].start()




##############
	


	def wahPeddle(self,speed,minVal,maxVal):
		"""Creates wah volume effect at variable speed wah's per minute"""

		self.stopFX("wahPeddle")
		self.timers["wahPeddle"] = OscillatorTimer(speed,minVal,maxVal,1,self.setChannelVolume)
		self.timers["wahPeddle"].start()


	
### Helper Function for wahPeddle ###
	def setChannelVolume(self,volume):
		Play.setVolume(volume,self.channel)
		self.volume = volume


########


	def stopFX(self, effect):
		if effect in self.timers.keys():
			self.timers[effect].stop()
			del self.timers[effect]

	def stopAllFX(self):
		for timer in self.timers.keys():
			self.timers[timer].stop()
			del self.timers[timer]





		