import subprocess
import re


class CubeSolver:    
    solutionParser = re.compile(r"[A-Z][\w ']+$")

    @staticmethod
    def solveCube(cubeString):
        output = subprocess.check_output(['./solver', cubeString], stderr=None)
        strOutput = "".join( chr(x) for x in output)
        return CubeSolver.solutionParser.search(strOutput).group()



sol = CubeSolver.solveCube('DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD')
print(sol)