import json
from flask import Flask, Response, jsonify, request
from constants.constants import VALID_POSITIONS

from enums.moves import Moves
from src.board import Board
from src.computer import Computer


app = Flask(__name__)

@app.route("/")
def hello_world():
    return jsonify("Hello, World!")

@app.post('/api/get-move')
def getMove():
    req = request.get_json()
    print(req)
    if any(req.get(key,None) is None for key in ['board', 'player', 'difficulty']):
        response = json.dumps({'error': 'Missing required parameters'})
        print(req, type(req))
        return Response(response, status=422, mimetype='application/json')
    print('it got here')
    flatBoard = sum(req['board'],[])
    flatBoard = [None if x == "None" else x for x in flatBoard]
    board = Board.getBoardObj(flatBoard)
    player = req['player']
    opponent = Moves.X.value if player == Moves.O.value else Moves.O.value
    
    ai = Computer(int(req['difficulty']), player, opponent)
    move = ai.getMove(board)
    
    response = json.dumps({"data": {"position": move, "coordinates": VALID_POSITIONS[move]}})
    return Response(response, status=200, mimetype='application/json')
