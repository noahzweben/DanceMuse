from music import *
from chord import *
from osc import *
from math import *
from melody import *
from Drums import *
import time

c = Chord()
shakeTrigger = 10
normalZ=35
prevTime = 0
beenSet = False
beatTimes=[]
interval = 0
averageBeat = 0
m2 = Melody(channel=11,octaveRange=[C4,B5],baseNote=C4,volume=100, instrument = 0)
d = Drums()


def playChord(message):
	global prevTime, beenSet, beatTimes, interval, averageBeat, m2
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



	if beenSet == True and abs(shake-normalZ)>shakeTrigger:
		interval = currentTime-prevTime
		if interval>.75:
			print "harmony"
			m2.harmonize(4)

	if len(beatTimes)==4 and beenSet == False:
		beenSet = True
		total=0
		for i in range(1,len(beatTimes)):
			total = total+beatTimes[i]
		averageBeat = total/(float(len(beatTimes)-1))*1000
		print averageBeat
		
		if averageBeat>2000:
			Play.setInstrument(97,c.channel)
			m2.setInstrument(41)
		else: 
			Play.setInstrument(27,c.channel)


	
		c.autoProgressChord(averageBeat)
		m2.playMelody(c,averageBeat/2.0)
		if averageBeat<2000:
			d.startBeat(d.classicBeat,averageBeat/2.0)
		else:
			d.startBeat(d.classicBeat,averageBeat*2)
		



oscIn = OscIn( 57110 )  
oscIn.onInput("/accelerometer", playChord)



