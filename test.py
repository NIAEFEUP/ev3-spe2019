from reader import ColorReader
from mover import CubeMover
from time import sleep

cm = CubeMover()
cr = ColorReader(cm)

# cr.calibrate()
cr.getCubeString()