# DanceMuse
# Dynamically writing computer-generated music based on dancer's movements
This is a package meant to be used with JythonMusic (described in full and downloadable at http://www.jythonmusic.org). 

This package contains the following musical classes -- Chord, Melody, and Drum -- as well as a PhoneConnect class that allows you to dynamically control the music through an OSC app on a Smartphone with acceleromter and gyroscope data.

Chord:
The chord class has numerous features. It is essentially a collection of notes with methods allowing these notes to be automatically and randomly shifted at a determined tempo. The musical progression of the chords is determined by a MARKOV CHAIN TABLE excel file that lists 15 common chords, and the likelihood of progressing to all other chords given a starting chord. 

Melody:
The melody object takes a chord instance as an input. Then, based on the notes in the chord and the chord progression, it dynamically writes an accompanying melody. There are methods to add in harmonies as well.

Drum:
The drum class describes a few different drum beats such as a more classical drumbeat and an electronic beat. These progress according to a given tempo.

PhoneConnect:
The PhoneConnect class connects to a smartphone's gyroscope and accelerometer through OSC. It uses the data from these sensors to determine the beat at which a dancer is moving.

The main file uses these various classes to construct a dynamically and randomly generated musical piece that reacts to the tempo at which dance.

--Continuing implementation--
* Want to continue to work on the musical "rules" of the composition to achieve more robust and differing pieces.
* Currently, the tempo is set at the beginning of the dance, want the program to be able to react dynamically to the dancer's tempo throughout the piece.
* Add more connections between dancer's movement and musical effects (i.e. dancer leans --> gyroscope changes output --> start a major/minor third harmony )