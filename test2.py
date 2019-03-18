from reader import ColorReader
from mover import CubeMover
from time import sleep
from caller import CubeSolver
from get_solution import translateMoves

cm = CubeMover()
#cr = ColorReader(cm)

#colorString = "ORBGRGOYGWWORGWRYOGBRWWYGGYRRBBOOWBGYYYOBBROYWWBOYGWRB"
#print(colorString)
#cubeString = CubeSolver.translateColors(colorString)
#print(cubeString)
#cm.move(translateMoves(cubeString))

while True:
	x = input('Move')
	cm.move(translateMoves(x))
