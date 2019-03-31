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
        self.averageColors = {(37.44444444444444, 166.11111111111111, 62.111111111111114): 'Y', (197.0, 245.22222222222223, 46.333333333333336): 'G', (185.33333333333334, 251.77777777777777, 158.66666666666666): 'B', (24.555555555555557, 88.0, 72.22222222222223): 'W', (126.11111111111111, 70.55555555555556, 14.666666666666666): 'O', (180.77777777777777, 159.0, 47.333333333333336): 'R'}


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

    def calibrateSensor(self):
        self.colorSensor.calibrate_white()

    def calibrate(self):
        self.averageColors = {}
        self.cubeMover.move(['f'])
        self.averageColors[self.calibrateFace()] = 'G'
        self.cubeMover.move(['f'])
        self.averageColors[self.calibrateFace()] = 'Y'
        self.cubeMover.move(['f'])
        self.averageColors[self.calibrateFace()] = 'B'
        self.cubeMover.move(['f'])
        self.averageColors[self.calibrateFace()] = 'W'
        self.cubeMover.move(['f', 'R', 'f'])
        self.averageColors[self.calibrateFace()] = 'R'
        self.cubeMover.move(['f', 'f'])
        self.averageColors[self.calibrateFace()] = 'O'
        self.cubeMover.move(['R', 'f', 'r'])
        print(self.averageColors)

    def calibrateFace(self):
        sumR = 0
        sumG = 0
        sumB = 0
        self.sensorMotor.toCenterPosition()
        r,g,b = self.colorSensor.rgb
        sumR += r
        sumB += b
        sumG += g
        for i in range(8):
            if i % 2 == 0:
                self.sensorMotor.toSidePosition()
            else:
                self.sensorMotor.toCornerPosition()
            r,g,b = self.colorSensor.rgb
            sumR += r
            sumB += b
            sumG += g
            self.cubeMover.move('H')
        self.sensorMotor.resetPosition()
        return (sumR/9, sumG/9, sumB/9)
        

    def readCube(self):
        faces = {}

        self.cubeMover.move(['f'])
        faces['B'] = self.readFace([6, 5, 4, 7, 0, 3, 8, 1, 2])
        self.cubeMover.move(['f'])
        faces['D'] = self.readFace([2, 1, 8, 3, 0, 7, 4, 5, 6])
        self.cubeMover.move(['f'])
        faces['F'] = self.readFace([2, 1, 8, 3, 0, 7, 4, 5, 6])
        self.cubeMover.move(['f'])
        faces['U'] = self.readFace([2, 1, 8, 3, 0, 7, 4, 5, 6])
        self.cubeMover.move(['f', 'R', 'f'])
        faces['L'] = self.readFace([4, 3, 2, 5, 0, 1, 6, 7, 8]) # Wrong
        self.cubeMover.move(['f', 'f'])
        faces['R'] = self.readFace([4, 3, 2, 5, 0, 1, 6, 7, 8]) # Wrong
        self.cubeMover.move(['R', 'f', 'r'])

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

