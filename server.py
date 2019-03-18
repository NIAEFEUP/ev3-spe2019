from flask import Flask
from flask_restful import Api, Resource, reqparse
from caller import CubeSolver
from get_solution import translateMoves
from serverInfo import serverInfo
import pycuber as pc

class Solver(Resource):

    def get(self, cube):
        solution = CubeSolver.solveCube(cube)
        print(solution)
        tSolution = translateMoves(solution)
        print(tSolution)
        return  tSolution,  200


app = Flask(__name__)
api = Api(app)


api.add_resource(Solver, "/<string:cube>")
app.run(host=serverInfo['hostName'], port=serverInfo['port'])