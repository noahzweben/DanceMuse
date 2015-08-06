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
		self.durations = 4*[.125]+5*[.25]+2*[.5]+[.75]+[1]

	def playMelody(self,chord,tempo):
		chordNotes = enforceOctave(chord.notes,self.octaveRange)
		noteChoices = self.availableNotes+100*chordNotes
		noteChoices = [i for i in noteChoices if (i%12 !=5)] #sounds bad for some reaason -- need 
		#to work with the chordNotes bcs FACE is getting turned int ACEF to fit octave --> dissonance
		randomIndex = int(random()*len(noteChoices))
		nextNote = noteChoices[randomIndex]
		
		self.stop()
		self.notes[0] = nextNote
		self.play()

		randomTime = int(random()*len(self.durations))
		duration = int(tempo*1000*self.durations[randomTime])
		#print chordNotes,nextNote

		if self.autoPlay is not None:
			self.autoPlay.stop()
			self.autoPlay = Timer(duration,self.playMelody,[chord,tempo])
			self.autoPlay.start()

		else:
			self.autoPlay = Timer(duration,self.playMelody,[chord,tempo])
			self.autoPlay.start()

	def standardDuration(self,duration):
		self.durations = [duration]


	def addHarmony(self, upper=True,lower=0):
		pass




		##set up timer where you basically just set the delay randomly and pause and unpause it

m = Melody(volume = 100,instrument = 0)
m1 = Melody(channel=12,octaveRange=[C1,C2],baseNote=C1,volume=100, instrument = 27)
m2 = Melody(channel=11,octaveRange=[C4,B5],baseNote=C4,volume=100, instrument = 27)
c = Chord(volume = 127, instrument = 27)
c.autoProgressChord(2000)
m.playMelody(c,2)
m2.playMelody(c,2)
m1.playMelody(c,2)
	