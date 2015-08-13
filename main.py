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
melody_low = Melody(channel=10,octaveRange=[C1,B2],baseNote=C2,volume=100, instrument = 41)
melody_low.standardDuration([.25])
phoneIn = PhoneConnect()

print "Loading"
while (phoneIn.xAccel is None) or (phoneIn.pitch is None):
	pass


print "Begin Dancing"

for i in range(3,0,-1):
	print i
	time.sleep(.25)

#Start Dancing
tempo = phoneIn.getBeat() #captures tempo
#
if tempo<2000:
	bassChords = Chord(octaveRange=[C3,B4],instrument = 27)
	melody_high.setInstrument(27)
	drums.startBeat(drums.classicBeat,tempo)

bassChords.autoProgressChord(tempo)
melody_high.playMelody(bassChords,tempo)










