from flask import Flask, request, jsonify

from flask_cors import CORS, cross_origin
from game_logic import TicTacToe

app = Flask(__name__)
CORS(app)
game = TicTacToe()

@app.route('/start', methods=['POST'])
def start_game():
    game.reset()
    return jsonify(message="Game started", board = game.board), 200


# endpoint to make a move
@app.route('/move', methods=['POST'])
def make_move():
    data = request.get_json()
    player = data['player']
    position = data['position']
    game.make_move(player, position)
    return jsonify(board=game.board, status = game.status()), 200


# endpoint to GET the status of a game
@app.route('/status' , methods=['GET'])
def get_status():
    return jsonify(board=game.board, status = game.status()) , 200


if __name__ == '__main__':
    app.run(debug=True)