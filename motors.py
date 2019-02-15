from ev3dev2.motor import LargeMotor, MediumMotor
from time import sleep

class BasicMotor:
	def __init__(self, motorModel, output, sleepTime=0.25):
		self.motor = motorModel(output)
		self.reset()
		self.sleepTime=sleepTime

	def __del__(self):
		self.motor.stop()

	def reset(self):
		self.motor.reset()
		self.motor.on_for_degrees(0,0,brake=False)


class BaseMotor(BasicMotor):
	def __init__(self, output):
		BasicMotor.__init__(self, LargeMotor, output)
		self.halfTurn = False

	def __del__(self):
		if self.halfTurn:
			self.rotate45()
		BasicMotor.__del__(self)

	def rotate180(self):
		self.motor.on_for_degrees(100,270 * 2)
		sleep(self.sleepTime)

	def rotate90(self):
		self.motor.on_for_degrees(100,270)
		sleep(self.sleepTime)

	def rotate45(self):
		self.halfTurn = not self.halfTurn
		self.motor.on_for_degrees(100,135)
		sleep(self.sleepTime)

	def rotate180R(self):
		self.motor.on_for_degrees(-100,270 * 2)
		sleep(self.sleepTime)

	def rotate90R(self):
		self.motor.on_for_degrees(-100,270)
		sleep(self.sleepTime)

	def rotate45R(self):
		self.halfTurn = not self.halfTurn
		self.motor.on_for_degrees(-100,135)
		sleep(self.sleepTime)

class FlipMotor(BasicMotor):
	def __init__(self, output):
		BasicMotor.__init__(self, LargeMotor, output)
		self.locked = False
		self.speed = 50
	
	def __del__(self):
		if self.locked:
			self.release()
		BasicMotor.__del__(self)

	def flip(self):
		if self.locked:
			return
			
		self.motor.on_for_degrees(self.speed,180)
		sleep(self.sleepTime)
		self.motor.on_for_degrees(-self.speed,90)
		sleep(self.sleepTime)
		self.motor.on_for_degrees(-self.speed,90)
		sleep(self.sleepTime)

	def lock(self):
		if self.locked:
			return
		self.motor.on_for_degrees(self.speed,90)
		sleep(self.sleepTime)
		self.locked = True

	def release(self):
		if not self.locked:
			return
		self.motor.on_for_degrees(-self.speed,90)
		sleep(self.sleepTime)
		self.locked = False


class SensorMotor(BasicMotor):
	def __init__(self, output):
		BasicMotor.__init__(self, MediumMotor, output)
		self.position = 0
		self.sidePosition = 480
		self.cornerPosition = 440
		self.centerPosition = 600

	def __del__(self):
		self.resetPosition()
		BasicMotor.__del__(self)

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
		self.motor.on_for_degrees(50,degrees)
		sleep(self.sleepTime)

	def move_back(self, degrees):
		if degrees == 0:
			return
		self.position -= degrees
		self.motor.on_for_degrees(-50,degrees)
		sleep(self.sleepTime)
