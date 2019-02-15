from reader import ColorReader
from mover import CubeMover
from time import sleep
from caller import CubeSolver

cm = CubeMover()
cr = ColorReader(cm)


colorString = cr.getCubeString()
print(colorString)
cubeString = CubeSolver.translateColors(colorString)
print(cubeString)
# sol = CubeSolver.solveCube(cubeString)
# print(sol)

# F - W
# U - O
# R - B
# L - G
# B - Y
# D - R