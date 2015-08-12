from music import *


class Drums:
	CHANNEL = 9
	def __init__(self):
		self.beatNumber = 0
		self.beat = None

	
	def startBeat(self,beat,tempo):
		beat()
		if self.beat is not None:
			self.beat.stop()
		self.beat = Timer(tempo/4.0,beat)
		self.beat.start()




	def classicBeat(self):
		if self.beatNumber == 0:
			Play.noteOn(45,127,self.CHANNEL)
			Play.noteOn(BDR,127,self.CHANNEL)
			Play.noteOn(ABD,127,self.CHANNEL)


		elif self.beatNumber == 3:
			Play.noteOn(44,127,self.CHANNEL)
		else:
			Play.noteOn(BDR,127,self.CHANNEL)
		self.beatNumber+=1
		self.beatNumber= self.beatNumber%4



