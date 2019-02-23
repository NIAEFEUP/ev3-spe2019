from flask import Flask
from flask_restful import Api, Resource, reqparse
from caller import CubeSolver
from get_solution import translateMoves


serverInfo = {
    'hostName': '10.236.232.1',
    'port': '5000'
}

class Solver(Resource):

    def get(self, cube):
        solution = CubeSolver.solveCube(cube)
        return  translateMoves(solution),  200


app = Flask(__name__)
api = Api(app)


api.add_resource(Solver, "/<string:cube>")
app.run(host=serverInfo['hostName'], port=serverInfo['port'])