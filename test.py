from reader import ColorReader
from mover import CubeMover
from time import sleep
from caller import CubeSolver
from get_solution import translateMoves
from requests import get

cm = CubeMover()
cr = ColorReader(cm)


colorString = cr.getCubeString()
print(colorString)
cubeString = CubeSolver.translateColors(colorString)
print(cubeString)
sol = get('http://10.236.232.1:5000/' + cubeString).text
print(sol)
m = translateMoves(sol[:len(sol) - 2])
print(m)
cm.move(m)

# F - W
# U - O
# R - B
# L - G
# B - Y
# D - R