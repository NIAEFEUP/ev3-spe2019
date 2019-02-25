from reader import ColorReader
from mover import CubeMover
from time import sleep
from caller import CubeSolver
from requests import get
from serverInfo import serverInfo

cm = CubeMover()
cr = ColorReader(cm)


colorString = cr.getCubeString()
cubeString = CubeSolver.translateColors(colorString)
print(cubeString)
sol = get('http://'+ serverInfo['hostName'] + ':' + serverInfo['port'] +'/' + cubeString).text
print(sol)
cm.move(sol)