from reader import ColorReader
from mover import CubeMover
from time import sleep
from caller import CubeSolver
from requests import get
from serverInfo import serverInfo

from ev3dev2.sensor import INPUT_2
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sound import Sound

sound = Sound()
ts = TouchSensor(INPUT_2)

cm = CubeMover()
cr = ColorReader(cm)

while True:
    print('ready')
    sound.beep()
    ts.wait_for_pressed()
    colorString = cr.getCubeString()
    cubeString = CubeSolver.translateColors(colorString)
    print(cubeString)
    sol = get('http://'+ serverInfo['hostName'] + ':' + serverInfo['port'] +'/' + cubeString)
    print(sol)
    if (sol.status_code == 200):
        cm.move(sol.text)