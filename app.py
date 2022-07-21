import json
from flask import Flask, Response, jsonify, request
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv

from constants.constants import VALID_POSITIONS
from enums.moves import Moves
from src.board import Board
from src.computer import Computer

load_dotenv('.env')
app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route("/")
def hello_world():
    return jsonify("Hello, World!")

@app.post('/api/get-move')
@cross_origin(supports_credentials=True)
def getMove():
    req = request.get_json()
    if any(req.get(key,None) is None for key in ['board', 'player', 'difficulty']):
        response = json.dumps({'error': 'Missing required parameters'})
        return Response(response, status=422, mimetype='application/json')
    flatBoard = sum(req['board'],[])
    flatBoard = [None if x == "None" or x == "" else x for x in flatBoard]
    board = Board.getBoardObj(flatBoard)
    player = req['player']
    opponent = Moves.X.value if player == Moves.O.value else Moves.O.value
    
    ai = Computer(int(req['difficulty']), player, opponent)
    move = ai.getMove(board)
    
    response = json.dumps({"data": {"position": move, "coordinates": VALID_POSITIONS[move]}})
    return Response(response, status=200, mimetype='application/json')
