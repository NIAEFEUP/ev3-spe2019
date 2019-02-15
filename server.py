from flask import Flask
from flask_restful import Api, Resource, reqparse
from caller import CubeSolver

class Solver(Resource):

    def get(self, cube):
        return CubeSolver.solveCube(cube), 200


app = Flask(__name__)
api = Api(app)


api.add_resource(Solver, "/<string:cube>")
app.run(debug=True)