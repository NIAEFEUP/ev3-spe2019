from ev3dev2.motor import OUTPUT_A, OUTPUT_B
from motors import FlipMotor, BaseMotor

class CubeMover:
    def __init__(self):
        self.flipper = FlipMotor(OUTPUT_B)
        self.base = BaseMotor(OUTPUT_A)

    def move(self, moveList):
        for move in moveList:
            if move == 'F':
                self.flipper.flip()
            elif move == 'R':
                self.base.rotate90()
            elif move == 'r':
                self.base.rotate90R()
            elif move == 'T':
                self.flipper.lock()
                self.base.rotate90()
                self.flipper.release()
            elif move == 't':
                self.flipper.lock()
                self.base.rotate90()
                self.flipper.release()