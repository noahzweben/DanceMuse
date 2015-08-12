import time
from osc import *

class PhoneConnect:

	def __init__(self):

		oscIn = OscIn( 57110 )        # receive messages from OSC clients on port 57110
		self.xAccel = None
		self.yAccel = None
		self.zAccel = None
		self.pitch = None
		self.roll = None
		self.yaw = None
		oscIn.onInput("/.*", self.update)    


	def update(self,message):
		OSCaddress = message.getAddress()
		args = message.getArguments()

		if OSCaddress == "/accelerometer":
			self.xAccel,self.yAccel,self.zAccel = args

		if OSCaddress == "/gyro":
			self.pitch,self.roll,self.yaw = args[3:]
