# A module of Automated effects #
from random import *
from Timer import *

def fx_random(minval, maxval, function, interval):
	"""randomly automates any function that takes a number as input)"""
	timer = Timer(interval,function,[mapValue(random(),0,1,minval,maxval)])
	return timer 