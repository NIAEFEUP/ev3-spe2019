from motors import SensorMotor
from ev3dev2.motor import OUTPUT_C
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import ColorSensor


class Color:
    def __init__(self, listColorTuples, maximumDiff=15):
        self.maximumDiff = maximumDiff
        self.numberOfColors = 0
        self.r = 0
        self.g = 0
        self.b = 0
        self.add(listColorTuples)

    def add(self, listColorTuples):
        self.r *= self.numberOfColors
        self.g *= self.numberOfColors
        self.b *= self.numberOfColors

        for r,g,b in listColorTuples:
            self.r += r
            self.g += g
            self.b += b

        self.numberOfColors += len(listColorTuples)
        self.r /= self.numberOfColors
        self.g /= self.numberOfColors
        self.b /= self.numberOfColors

    def getTuple(self):
        return (self.r, self.g, self.b)
        


class ColorReader:
    def __init__(self, cubeMover):
        self.cubeMover = cubeMover
        self.colorSensor = ColorSensor(INPUT_1)
        self.sensorMotor = SensorMotor(OUTPUT_C)
        self.averageColors = {
            (201,174,51): 'O',
            (210,255,166): 'W',
            (142,84,17): 'R',
            (223,254,51): 'Y',
            (32,99,75): 'B',
            (46,189,66): 'G'
        }


    def readFace(self, positions=[0,1,2,3,4,5,6,7,8]):
        colorString = ""
        self.sensorMotor.toCenterPosition()
        colorString += self.getColor()
        for i in range(8):
            if i % 2 == 0:
                self.sensorMotor.toSidePosition()
            else:
                self.sensorMotor.toCornerPosition()
            colorString += self.getColor()
            self.cubeMover.move('H')
        self.sensorMotor.resetPosition()

        orderedString = ""
        for position in positions:
            orderedString += colorString[position]
        return orderedString

    def calibrate(self):
        self.sensorMotor.toSidePosition()
        self.colorSensor.calibrate_white()

    def readCube(self):
        faces = {}

        self.cubeMover.move(['F'])
        faces['B'] = self.readFace([6, 5, 4, 7, 0, 3, 8, 1, 2])
        self.cubeMover.move(['F'])
        faces['D'] = self.readFace([2, 1, 8, 3, 0, 7, 4, 5, 6])
        self.cubeMover.move(['F'])
        faces['F'] = self.readFace([2, 1, 8, 3, 0, 7, 4, 5, 6])
        self.cubeMover.move(['F'])
        faces['U'] = self.readFace([2, 1, 8, 3, 0, 7, 4, 5, 6])
        self.cubeMover.move(['F', 'R', 'F'])
        faces['L'] = self.readFace([4, 3, 2, 5, 0, 1, 6, 7, 8]) # Wrong
        self.cubeMover.move(['F', 'F'])
        faces['R'] = self.readFace([4, 3, 2, 5, 0, 1, 6, 7, 8]) # Wrong
        self.cubeMover.move(['R', 'F', 'r'])

        return faces

    def getCubeString(self):
        cubeString = ""
        faces = self.readCube()
        for face in ['U', 'R', 'F', 'D', 'L', 'B']:
            print(face + " " + faces[face])
            cubeString += faces[face]
        return cubeString


    def getColor(self):
        r,g,b = self.colorSensor.rgb
        min_diff = 255 * 3 + 1
        color = None
        for aR, aG, aB in self.averageColors:
            diff = abs(aR - r) + abs(aG - g) + abs(aB - b)
            if diff < min_diff:
                min_diff = diff
                color = self.averageColors[(aR, aG, aB)]
        # print(color, end=" ")
        return color

