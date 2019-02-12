from ev3dev2.motor import OUTPUT_A, OUTPUT_C, OUTPUT_B
from motors import FlipMotor, BaseMotor, SensorMotor


bm = FlipMotor(OUTPUT_B)
am = BaseMotor(OUTPUT_A)
sm = SensorMotor(OUTPUT_C)

bm.reset()
am.reset()
sm.reset()
