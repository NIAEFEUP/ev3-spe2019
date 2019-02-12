from ev3dev2.motor import OUTPUT_A, OUTPUT_C, OUTPUT_B
from motors import FlipMotor, BaseMotor, SensorMotor
from time import sleep


bm = FlipMotor(OUTPUT_B)
am = BaseMotor(OUTPUT_A)
sm = SensorMotor(OUTPUT_C)

#Rotação do motor do sensor
sm.move_back(100)

for i in range(2):
    sm.move(500)
    sleep(0.5)
    sm.move(80)
    sleep(0.5)
    sm.move_back(580)
    sleep(0.5)

#Rotação ainda não está certa

sm.reset()