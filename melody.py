from random import *
from music import *
from MusicFunctions import *
from chord import *

class Melody(MusicObject):

	def __init__(self,key=MAJOR_SCALE,baseNote=C3,octaveRange=[C3,B4],\
		channel=10,volume = 50, instrument = 41):

		MusicObject.__init__(self,key,baseNote,octaveRange,channel,instrument,volume)

		self.availableNotes = createKey(key,baseNote)
		self.notes = [0]
		self.autoPlay=None
		self.isHarmony = False
		#Makes eigth and quarter notes the most likely followed by
		# half, dotted half, and whole notes
		self.durations = 5*[.125]+8*[.25]+2*[.5]+[.75]+[1]

	def playMelody(self, chord,tempo):
		chordNotes = enforceOctave(chord.notes,self.octaveRange)

		#Makes it highly likely that a note from the current chord will be in the melody
		noteChoices = self.availableNotes+70*chordNotes
		noteChoices = [i for i in noteChoices if (i%12 !=5)] #sounds bad for some reason -- need 
		#to work with the chordNotes bcs FACE is getting turned int0
		# ACEF to fit octave causing poor sound quality

		randomIndex = int(random()*len(noteChoices))
		nextNote = noteChoices[randomIndex]
		
		self.stop()
		self.notes[0] = nextNote

		#Plays a key-enforced harmony, adds interval amount determined in harmonize
		if self.isHarmony:
			self.notes = [self.notes[0]]+[self.notes[0]+self.harmonyAmount]
			self.notes = enforceKey(self.notes,self.key)

		# If harmony is off, just play the root of the melody
		else: 		
			self.notes = self.notes[0:1]

		self.notes = [i for i in self.notes if (i%12 != 5+self.baseNote%12)]

		self.play()

		#Picks a random duration from list of possible durations
		randomTime = int(random()*len(self.durations))
		duration = int(tempo*self.durations[randomTime])


		#Starts the melody
		if self.autoPlay is not None:
			self.autoPlay.stop()
		self.autoPlay = Timer(duration,self.playMelody,[chord,tempo])
		self.autoPlay.start()

	def standardDuration(self,duration):
		self.durations = [duration]


	def harmonize(self, amount):
		self.isHarmony = True
		self.harmonyAmount = amount
	def stopHarmonize(self):
		self.isHarmony = False




