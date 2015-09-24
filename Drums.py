from music import *
import time

class Drums:
	CHANNEL = 9
	def __init__(self):
		self.beatNumber = 0
		self.beat = None
		self.isRain = False

	
	def startBeat(self,beat,tempo):
		beat()
		if self.beat is not None:
			self.beat.stop()
		self.beat = Timer(tempo/4.0,beat)
		self.beat.start()



	#Plays beats that have different drum sound for beats 1 and 4
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

	def electroBeat(self):
		if self.beatNumber == 0:
			Play.noteOn(40,127,self.CHANNEL)
		else:
			Play.noteOn(39,127,self.CHANNEL)
		self.beatNumber+=1
		self.beatNumber= self.beatNumber%4


	def raindrops(self,tempo,inst):
		self.isRain = True
		tempo = tempo/1000.0

		for i in range(16):
			Play.noteOn(122,90,15)
			time.sleep(.05)

		self.isRain = False



