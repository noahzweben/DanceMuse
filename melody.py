from random import *
from music import *
from MusicFunctions import *
from chord import *

class Melody:

	def __init__(self,key=MAJOR_SCALE,baseNote=C3,rangeVal=[C3,B4],channel=10,volume = 50):
		self.availableNotes = createKey(key,baseNote)
		self.currentNote = 0
		self.rangeVal = rangeVal
		self.channel = channel
		Play.setInstrument(41,self.channel)
		self.volume = volume
		self.autoPlay=None

	def playMelody(self,chord,tempo):
		chordNotes = enforceOctave(chord.notes,self.rangeVal)
		noteChoices = self.availableNotes+70*chordNotes
		noteChoices = [i for i in noteChoices if (i!=F3 and i!=F4)] #sounds bad for some reaason -- need 
		#to work with the chordNotes bcs FACE is getting turned int ACEF to fit octave --> dissonance
		randomIndex = int(random()*len(noteChoices))
		nextNote = noteChoices[randomIndex]

		Play.noteOff(self.currentNote,self.channel)
		Play.noteOn(nextNote,self.volume,self.channel)
		self.currentNote = nextNote

		tempos = [.125,.25,.125,.25,.125,.25,.5,.75]
		randomTime = int(random()*len(tempos))
		duration = int(tempo*1000*tempos[randomTime])
		#print chordNotes,nextNote

		if self.autoPlay is not None:
			self.autoPlay.stop()
			self.autoPlay = Timer(duration,self.playMelody,[chord,tempo])
			self.autoPlay.start()

		else:
			self.autoPlay = Timer(duration,self.playMelody,[chord,tempo])
			self.autoPlay.start()





		##set up timer where you basically just set the delay randomly and pause and unpause it

m = Melody(volume = 70)
m2 = Melody(channel=11,rangeVal=[C4,B5],baseNote=C4,volume=50)
c = Chord()
c.autoProgressChord(1500)
m.playMelody(c,1.5)
m2.playMelody(c,1.5)

	