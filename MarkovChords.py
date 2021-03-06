import csv
from random import *
from music import *
import copy

class MarkovChords:

	### A list of Chords using C3 as baseNote
	CHORDS_LIST = {"C":[C3,E3,G3],"Dm":[D3,F3,A3],"Em": [E3,G3,B3],"F":[F3,A3,C4],"G":[G3,B3,D3],\
	 "Am":[C3,E3,A3], "G/B":[B2,D3,G3], 'Cmaj7': [C3, E3, G3,B3], "Em7": [E3,G3,B3,D4],\
	 "Dm7": [D3,F3,A3,C4], "Am7": [A2,C3,E3,G3], "Fmaj7": [F2,A2, C3, E3]}

	def __init__(self,baseNote,filename):

		self.chords = copy.deepcopy(self.CHORDS_LIST)
		self.setChords(-C3,octave=False) #generates chords as intervals by stripping C3
	 	self.setChords(baseNote) #puts the chords in the correct key
	 	self.chordProbabilities = self.createProbabilities(filename)


	### Sets the Base of the Chord ###
	def setChords(self,baseNote, octave=True):
		"""Creates the chords given a startNote (because the chords are defined
		with intervals. 0 for C1,1 for CS1 . . .etc"""
		for chord in self.chords.keys():
			for i in range(len(self.chords[chord])):
				self.chords[chord][i]=self.chords[chord][i]+baseNote
				if octave:
					while self.chords[chord][i]<0:
						self.chords[chord][i]=self.chords[chord]+12


	@staticmethod
	def createProbabilities(filename):
		"""Creates the probability dictionary from Markov Spreadsheet""" 
		print "\nGenerating chord progression probabilities..."
		markovFile = open(filename, 'rU')
		markovReader = csv.reader(markovFile)
		chordsList = markovReader.next()[1:] #captures order of chords in header


		#Creates a dictionary that has each chord as a key, and the value of each key
		#is a list of chords, whose frequency depends on how probable they are to follow 
		# the key chord i.e {"Cmaj7":["Dm","Dm","C"]} if Dm 
		# had a .66 chance and C a .33 chance of occuring after a Cmaj7.

		chordProbability = {}
		for line in markovReader:
			myProbability= []
			probabilities = line[1:]
			for i in range(len(probabilities)):
				for j in range(int(probabilities[i])):
					myProbability.append(chordsList[i])
			chordProbability[line[0]]=myProbability
		print "Complete"

		return chordProbability

	def nextChord(self,currentChord):
		"""Progresses to a new chord dictated by the probability
		of new chord following the current chord"""
		randomIndex = mapValue(random(),0,1,0,99)
		nextOptions = self.chordProbabilities[currentChord]
		newChordName = nextOptions[randomIndex]
		newChordNotes = self.chords[newChordName]
		return newChordName,newChordNotes







