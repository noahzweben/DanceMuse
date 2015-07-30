from music import *
from random import *
from MusicFunctions import *

class Chord:

	chords = [[C3,E3,G3],[C3,DS3,G3],[C3,DS3,GS3],[C3,E3,A3],[C3,F3,GS3],[B2,DS3,GS3],[D3,F3,A3]]

	def __init__(self,channel=0,chord =[C3,E3,G3], key = MAJOR_SCALE, baseNote = 0,octaveRange =None):
		self.notes = chord
		self.channel = channel
		Play.setInstrument(97)
		self.volume = 127
		self.key = createKey(key,baseNote)
		self.octaveRange = octaveRange

		self.timers = {}

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


### Random and Automated Effects ####	
	

	def randomNewChord(self, chords, interval=0, ): 
		"""Randomly switches chord to one in supplied set every
		interval seconds"""

		randomindex = int(len(chords)*random())
		newNotes = chords[randomindex]
		self.newNotes(newNotes)

		if interval !=0:
			if "randomNewChord" not in self.timers.keys():
				self.timers["randomNewChord"] = Timer(interval,self.randomNewChord,[chords])
			self.timers["randomNewChord"].setDelay(interval)
			self.timers["randomNewChord"].start()

	def stopRandomNewChord(self):
		if "randomNewChord" in self.timers.keys():
			self.timers["randomNewChord"].stop()
			del self.timers["randomNewChord"]

	######################

	# Automates shifting the chord up and down. 
	def autoShift(self, amount, interval, notes=[],  inKey=True): 

		self.shift(amount,notes, inKey)
		self.stopAutoShift()
		self.timers["autoShift"] = Timer(interval,self.shift,[amount,notes,inKey])
		self.timers["autoShift"].start()


	def stopAutoShift(self):
		if "autoShift" in self.timers.keys():
			self.timers["autoShift"].stop()
			del self.timers["autoShift"]

##############
	


	def wahPeddle(self,speed,minVal,maxVal):
		"""Creates wah volume effect at variable speed wah's per minute"""

		self.stopWah()
		self.timers["wahPeddle"] = OscillatorTimer(speed,minVal,maxVal,1,self.setChannelVolume)
		self.timers["wahPeddle"].start()

	def stopWah(self):
		if "wahPeddle" in self.timers.keys():
			self.timers["wahPeddle"].stop()
			del self.timers["wahPeddle"]
	
### Helper Function for wahPeddle ###
	def setChannelVolume(self,volume):
		Play.setVolume(volume,self.channel)
		self.volume = volume


########



	def stopFX(self):
		for timer in self.timers.keys():
			self.timers[timer].stop()
			del self.timers[timer]





		