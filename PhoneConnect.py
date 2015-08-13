import time
from osc import *

class PhoneConnect:
	# normal variable values for  phone in upright position
	NORMAL_XZ = 65
	NORMAL_Y = 35

	NORMAL_PITCH = 80


	SHAKETRIGGER = 7 # the lower the trigger, the more sensitive the program

	def __init__(self):

		oscIn = OscIn( 57110 )        # receive messages from OSC clients on port 57110
		self.xAccel = None
		self.yAccel = None
		self.zAccel = None
		self.pitch = None
		self.roll = None
		self.yaw = None

		self.beatTimes=[]
		oscIn.onInput("/.*", self.update)    



	def update(self,message):
		OSCaddress = message.getAddress()
		args = message.getArguments()

		if OSCaddress == "/accelerometer":
			self.xAccel,self.yAccel,self.zAccel = args

		if OSCaddress == "/gyro":
			self.pitch,self.roll,self.yaw = args[3:]


	def getBeat(self):
		prevTime=0
		beatTimes = []
		while len(beatTimes)<4:
			if ( (self.yAccel - self.NORMAL_Y > self.SHAKETRIGGER) and (self.pitch > 70) ):
				currentTime = time.time()
				interval = currentTime-prevTime
				if interval > .65:
					prevTime = currentTime
					beatTimes.append(interval)
					print "Beat captured in", 3-(len(beatTimes)-1)
		total=0
		for i in range(1,len(beatTimes)):
			total = total+beatTimes[i]
		averageBeat = total/(float(len(beatTimes)-1))*1000
		return averageBeat


