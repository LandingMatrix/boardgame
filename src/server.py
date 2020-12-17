from flask import Flask, request
from json import dumps

app = Flask(__name__)


@app.route('/player/register', methods=['POST']) #POST, PUT, GET, DELETE
def player_register_route():
    return dumps({'start': True})

@app.route('/game/start', methods=['POST']) #POST, PUT, GET, DELETE
def game_start_route():
    return dumps({'start': True})

if __name__ == '__main__':
    app.run(port=0) #host='0.0.0.0'
