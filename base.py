from ev3dev2.motor import LargeMotor, OUTPUT_A, MediumMotor, OUTPUT_C, OUTPUT_B
from time import sleep

class BasicMotor:
	def __init__(self, output):
		self.motor = LargeMotor(output)
		self.reset()

	def reset(self):
		self.motor.reset()
		self.motor.on_for_degrees(0,0,brake=False)
		self.motor.stop()


class BaseMotor(BasicMotor):
	def __init__(self, output):
		BasicMotor.__init__(self,output)

	def rotate90(self):
		self.motor.on_for_degrees(100,270)
		sleep(0.5)

	def rotate45(self):
		self.motor.on_for_degrees(100,135)
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
		self.state = 1
	
	def flip(self):
		if self.state != 1:
			return
			
		self.motor.on_for_degrees(40,180)
		sleep(0.5)
		self.motor.on_for_degrees(-40,90)
		sleep(0.5)
		self.motor.on_for_degrees(-40,90)
		sleep(0.5)

	def lock(self):
		if self.state != 1:
			return
		self.motor.on_for_degrees(40,90)
		sleep(0.5)
		self.state = 2

	def release(self):
		if self.state == 1:
			return
		self.motor.on_for_degrees(-40,90)
		sleep(0.5)
		self.state = 1


class SensorMotor:
	def __init__(self, output):
		self.motor = MediumMotor(output)
		self.reset()

	def reset(self):
		self.motor.reset()
		self.motor.on_for_degrees(0,0,brake=False)
		self.motor.stop()

	def move(self, degrees):
		self.motor.on_for_degrees(-100,degrees)
		sleep(0.5)

	def move_back(self, degrees):
		self.motor.on_for_degrees(100,degrees)
		sleep(0.5)

bm = FlipMotor(OUTPUT_B)
am = BaseMotor(OUTPUT_A)
sm = SensorMotor(OUTPUT_C)