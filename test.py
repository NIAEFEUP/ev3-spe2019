from ev3dev2.motor import OUTPUT_C, OUTPUT_A, OUTPUT_B
from ev3dev2.sensor import INPUT_1, INPUT_2
from ev3dev2.sensor.lego import ColorSensor
from motors import SensorMotor, BaseMotor, FlipMotor
from time import sleep

sm = SensorMotor(OUTPUT_C)
bm = BaseMotor(OUTPUT_A)
fm = FlipMotor(OUTPUT_B)

cs = ColorSensor(INPUT_1)
# sm.toSidePosition()
# cs.calibrate_white()
#Rotação do motor do sensor

for i in range(1):
    sm.toCenterPosition()
    print(cs.color_name + " " + str(cs.rgb))
    for i in range(8):
        if i % 2 == 0:
            sm.toSidePosition()
        else:
            sm.toCornerPosition()
        print(cs.color_name + " " + str(cs.rgb))
        bm.rotate45()
    sm.resetPosition()
    print()

# sm.move_back(360)

#Rotação ainda não está certa

