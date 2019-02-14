import subprocess
import re

class CubeSolver:    
    solutionParser = re.compile(r"[A-Z][\w ']+$")

    @staticmethod
    def solveCube(cubeString):
        output = subprocess.check_output(['./solver', cubeString], shell=True)
        strOutput = "".join( chr(x) for x in output)
        return CubeSolver.solutionParser.search(strOutput).group()
    
    @staticmethod
    def translateColors(colorString):
        dic = {}
        dic[colorString[4]] = 'U'
        dic[colorString[13]] = 'R'
        dic[colorString[22]] = 'F'
        dic[colorString[31]] = 'D'
        dic[colorString[40]] = 'L'
        dic[colorString[49]] = 'B'
        cubeString = ""
        for c in colorString:
            cubeString += dic[c]
        return cubeString
