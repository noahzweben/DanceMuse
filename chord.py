from music import *
from random import *
from MusicFunctions import *
from MarkovChords import *
from MusicObject import *


#Contains variables and methods that work with chords
class Chord(MusicObject):

	def __init__(self,channel=0,chord =[C3,E3,G3], key = MAJOR_SCALE, baseNote = 0,\
		octaveRange =[C2,C4], instrument = 97, volume = 127):
		MusicObject.__init__(self,key,baseNote,octaveRange,channel,instrument,volume)
		
		self.notes = chord
		self.timers = {}
		self.currentChord = "C"
		baseValue = octaveRange[0]

		#Creates chord progressions probabilities from a Markov Chain Table excel file
		self.chordProg = MarkovChords(baseValue,'./myproj/DanceMuse/markov.csv')

######## Chord Changes ###############


	def shift(self,amount, notes= [], inKey = True, nowStart = True,):
		""" Shifts the chord by the specified amount. If amount is given as
		list i.e. [-4,4] will shift randomly within that interval. 
		If notes is set, will only shift the notes 
		of the chord corresponding to the note indexes supplied"""
	
		if type(amount)==list:
			maxval,minval = amount
			### Generates a random value between minval and maxval
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
		"""Shifts to a random new chord with all pitches within rangeVal of their
		original value"""
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
		#Uses the Markov Probabilities to change to a new chord
		self.currentChord,newNotes = self.chordProg.nextChord(self.currentChord)
		self.newNotes(newNotes, nowStart = nowStart)



### Random and Automated Effects ####	
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
		if interval !=0:
			self.stopFX("autoProgressChord")
			self.timers["autoProgressChord"] = Timer(interval,self.progressChord)
			self.timers["autoProgressChord"].start()

	# Automates shifting the chord up and down. 
	def autoShift(self, amount, interval, notes=[],  inKey=True): 

		self.shift(amount,notes, inKey)
		self.stopFX("autoShift")
		self.timers["autoShift"] = Timer(interval,self.shift,[amount,notes,inKey])
		self.timers["autoShift"].start()


	def wahPeddle(self,speed,minVal,maxVal):
		"""Creates wah volume effect at variable speed wah's per minute"""
		#NEED TO FIX THE TIMING ON THIS
		self.stopFX("wahPeddle")
		self.timers["wahPeddle"] = OscillatorTimer(speed,minVal,maxVal,1,self.setChannelVolume)
		self.timers["wahPeddle"].start()



	def stopFX(self, effect):
		if effect in self.timers.keys():
			self.timers[effect].stop()
			del self.timers[effect] 
			#I've noticed that the more timers there are, the less effective they are, 
			#so delete them when not in use.

	def stopAllFX(self):
		for timer in self.timers.keys():
			self.timers[timer].stop()
			del self.timers[timer]





		