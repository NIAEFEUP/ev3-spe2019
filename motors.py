from ev3dev2.motor import LargeMotor, MediumMotor
from time import sleep

class BasicMotor:
	def __init__(self, motorModel, output):
		self.motor = motorModel(output)
		self.reset()

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
		sleep(0.5)

	def rotate90(self):
		self.motor.on_for_degrees(100,270)
		sleep(0.5)

	def rotate45(self):
		self.halfTurn = not self.halfTurn
		self.motor.on_for_degrees(100,135)
		sleep(0.5)

	def rotate180R(self):
		self.motor.on_for_degrees(-100,270 * 2)
		sleep(0.5)

	def rotate90R(self):
		self.motor.on_for_degrees(-100,270)
		sleep(0.5)

	def rotate45R(self):
		self.halfTurn = not self.halfTurn
		self.motor.on_for_degrees(-100,135)
		sleep(0.5)

class FlipMotor(BasicMotor):
	def __init__(self, output):
		BasicMotor.__init__(self, LargeMotor, output)
		self.locked = False
	
	def __del__(self):
		if self.locked:
			self.release()
		BasicMotor.__del__(self)

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


class SensorMotor(BasicMotor):
	def __init__(self, output):
		BasicMotor.__init__(self, MediumMotor, output)
		self.position = 0
		self.sidePosition = 450
		self.cornerPosition = 410
		self.centerPosition = 540

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
		self.motor.on_for_degrees(-100,degrees)
		sleep(0.5)

	def move_back(self, degrees):
		if degrees == 0:
			return
		self.position -= degrees
		self.motor.on_for_degrees(100,degrees)
		sleep(0.5)
