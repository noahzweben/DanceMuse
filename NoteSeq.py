import time as time
from music import *

class NoteSeq:
	

	def __init__(self,notes=[C3,E3,G3],channel=5):
		self.notes = notes
		self.channel = channel
		Play.setInstrument(97,self.channel)


	def play(self,duration):
		for note in self.notes:
			Play.noteOn(note,127,self.channel)
			time.sleep(duration)
			Play.noteOff(note,self.channel)
