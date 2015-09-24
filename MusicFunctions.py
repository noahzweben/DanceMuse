from music import *
from math import *


### Functions for Enforcing a Key

def enforceKey(notes,key, baseNote = 0):
	"""Input notes as a list, enter a scale type (i.e. MINOR_SCALE) and the base note of the scale:
	0 for C, 1 for C# etc"""
	key = key[:] 
	if baseNote !=0:
		key = createKey(key,baseNote)

	#increments notes until they belong to the correct key
	for i in  range(len(notes)):
		while( (not isKey(notes[i],key)) or (notes[i] in notes[0:i]) ):
			notes[i] = notes[i]+1
	notes.sort()
	return notes


# Helper Functions
def createKey(key,baseNote):
	key = key[:]
	if baseNote != 0:
		for i in range(len(key)):
			key[i]=key[i]+baseNote 
	return key


def isKey(note,key):
	""""Checks if note is in a certain key"""
	if note % 12 in key: #reduces note to 1st octave
		return True
	else:
		return False


def enforceOctave(notes,rangeVal):
	"""Moves the pitches in list, notes, into an octave
	defined by rangeVal"""
	notesIn = notes[:]
	for i in range(len(notesIn)):
		while (notesIn[i]<min(rangeVal) or notesIn[i]>max(rangeVal)):
			if notesIn[i] < min(rangeVal):
				notesIn[i]=notesIn[i]+12
			else:
				notesIn[i]=notesIn[i]-12
	notesIn.sort()
	return notesIn




