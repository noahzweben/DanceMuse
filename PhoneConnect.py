from music import *
import time 
from chord import *
from osc import *
from math import *

class PhoneConnect():

	def __init__(self):
		self.prevTime = 0;
		self.c = Chord(octaveRange=[C2,B3])
		self.shakeTrigger = 6
		self.normalZ=35
		Play.setInstrument(27,c.channel)



	def playChord(self,message):

		args = message.getArguments()
		shake = args[2]
		print shake
		if abs(shake-normalZ)>shakeTrigger:
			c.shift([-5,5])

