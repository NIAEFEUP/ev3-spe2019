from ev3dev2.motor import LargeMotor, MediumMotor
from time import sleep

class BasicMotor:
	def __init__(self, output):
		self.motor = LargeMotor(output)
		self.reset()

	def __del__(self):
		self.motor.stop()

	def reset(self):
		self.motor.reset()
		self.motor.on_for_degrees(0,0,brake=False)
		self.motor.stop()


class BaseMotor(BasicMotor):
	def __init__(self, output):
		BasicMotor.__init__(self,output)

	def rotate180(self):
		self.motor.on_for_degrees(100,270 * 2)
		sleep(0.5)

	def rotate90(self):
		self.motor.on_for_degrees(100,270)
		sleep(0.5)

	def rotate45(self):
		self.motor.on_for_degrees(100,135)
		sleep(0.5)

	def rotate180R(self):
		self.motor.on_for_degrees(-100,270 * 2)
		sleep(0.5)

	def rotate90R(self):
		self.motor.on_for_degrees(-100,270)
		sleep(0.5)

	def rotate45R(self):
		self.motor.on_for_degrees(-100,135)
		sleep(0.5)

class FlipMotor(BasicMotor):
	def __init__(self, output):
		BasicMotor.__init__(self,output)
		self.locked = False
	
	def flip(self):
		if self.locked:
			return
			
		self.motor.on_for_degrees(40,180)
		sleep(0.5)
		self.motor.on_for_degrees(-40,90)
		sleep(0.5)
		self.motor.on_for_degrees(-40,90)
		sleep(0.5)

	def lock(self):
		if self.locked:
			return
		self.motor.on_for_degrees(40,90)
		sleep(0.5)
		self.locked = True

	def release(self):
		if not self.locked:
			return
		self.motor.on_for_degrees(-40,90)
		sleep(0.5)
		self.locked = False

class BasicMediumMotor:
	def __init__(self, output):
		self.motor = MediumMotor(output)
		self.reset()

	def __del__(self):
		self.motor.stop()

	def reset(self):
		self.motor.reset()
		self.motor.on_for_degrees(0,0,brake=False)
		self.motor.stop()

class SensorMotor(BasicMediumMotor):
	def __init__(self, output):
		BasicMediumMotor.__init__(self, output)
		self.position = 0
		self.sidePosition = 450
		self.cornerPosition = 410
		self.centerPosition = 540

	def __del__(self):
		self.resetPosition()
		self.motor.stop()

	def resetPosition(self):
		self.move_back(self.position)

	def toSidePosition(self):
		self.move(self.sidePosition - self.position)

	def toCornerPosition(self):
		self.move(self.cornerPosition - self.position)

	def toCenterPosition(self):
		self.move(self.centerPosition - self.position)

	def move(self, degrees):
		if degrees == 0:
			return
		self.position += degrees
		self.motor.on_for_degrees(-100,degrees)
		sleep(0.5)

	def move_back(self, degrees):
		if degrees == 0:
			return
		self.position -= degrees
		self.motor.on_for_degrees(100,degrees)
		sleep(0.5)
