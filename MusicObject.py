from music import *
from MusicFunctions import *

#Abstract class to help construct Melody and Chord objects 
class MusicObject:

	def __init__(self,key=MAJOR_SCALE,baseNote=C3,octaveRange=[C2,C4],\
		channel=0, instrument=97,volume=127):
		self.key = createKey(key,baseNote)
		self.channel = channel
		Play.setInstrument(instrument,self.channel)
		self.volume = volume
		self.octaveRange = octaveRange
		self.notes = None ##added in chord/melody call

	def setChannelVolume(self,volume):
		Play.setVolume(volume,self.channel)
		self.volume = volume

	def setInstrument(self,instrument):
		Play.setInstrument(instrument,self.channel)
	
	def play(self):
		for note in self.notes:
			Play.noteOn(note,self.volume,self.channel)
			
	def stop(self):
		for note in self.notes:
			Play.noteOff(note,self.channel)