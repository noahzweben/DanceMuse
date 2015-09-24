from music import *
from chord import *
from PhoneConnect import *
from math import *
from melody import *
from Drums import *
import time

### initialize variables
bassChords = Chord()
drums = Drums()
melody_high = Melody(channel=11,octaveRange=[C4,B5],baseNote=C4,volume=100, instrument = 41)
melody_low = Melody(channel=10,octaveRange=[C1,B2],baseNote=C2,volume=127, instrument = 18)
phoneIn = PhoneConnect()


#Waits for OSC connection to beign loading data 
print "Loading"
while (phoneIn.xAccel is None) or (phoneIn.pitch is None): #Waits for OSC connection to beign loading data 
	pass
print "Begin Dancing"

for i in range(3,0,-1):
	print i
	time.sleep(.25)

#Start Dancing
tempo = phoneIn.getBeat() #captures tempo
print tempo/1000.0

#Changes instrument types based on how fast you are dancing
if tempo<1000:
	tempo *= 2

if tempo<2000:
	bassChords = Chord(octaveRange=[C3,B4],instrument = 30,volume=80)
	melody_high.setInstrument(30)
	drums.startBeat(drums.electroBeat,tempo)

bassChords.autoProgressChord(tempo)
melody_high.playMelody(bassChords,tempo)
#melody_low.playMelody(bassChords,tempo*2)










