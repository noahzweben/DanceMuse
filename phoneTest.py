from music import *
from chord import *
from osc import *
from math import *
import time

c = Chord()
shakeTrigger = 10
normalZ=35
prevTime = 0
beenSet = False
beatTimes=[]
interval = 0
averageBeat = 0

def playChord(message):
	global prevTime, beenSet, beatTimes, interval, averageBeat
	currentTime = time.time()
	args = message.getArguments()
	shake = args[2]
	if abs(shake-normalZ)>shakeTrigger:
		interval=currentTime-prevTime
		if interval>.65:
			prevTime=currentTime
			beatTimes.append(interval)
			if len(beatTimes)<=4:
				print "Beat in", 3-(len(beatTimes)-1)

	if len(beatTimes)==4 and beenSet == False:
		beenSet = True
		total=0
		for i in range(1,len(beatTimes)):
			total = total+beatTimes[i]
		averageBeat = total/(float(len(beatTimes)-1))
		print averageBeat
		
		if averageBeat>2:
			Play.setInstrument(97,c.channel)
		else: 
			Play.setInstrument(27,c.channel)


		c.autoProgressChord(averageBeat*1000)


oscIn = OscIn( 57110 )  
oscIn.onInput("/accelerometer", playChord)



