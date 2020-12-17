from flask import Flask, request, render_template
from json import dumps

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/player/register', methods=['POST']) #POST, PUT, GET, DELETE
def player_register_route():
    return dumps({'start': True})

@app.route('/game/start', methods=['POST']) #POST, PUT, GET, DELETE
def game_start_route():
    pass

if __name__ == '__main__':
    app.run(port=80) #host='0.0.0.0'
