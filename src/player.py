import data
import random

class Player():
    def __init__(self, name):
        self.name = name
        self.id = len(data.data['players'])
        self.balance = None #updates at game_start

    def join(self, game):
        if data.data['game_host'] == None:
            raise ValueError("Game does not exist")
        if self in game.players:
            raise ValueError("Player is already in game")
        else:
            game.players.append(self)

    def leave(self, game):
        if self in game.players:
            game.players.remove(self)
        else:
            raise ValueError("Player is not in game")

        if game.players == []:
            game.abort(self)

    def stats(self):
        return {
            'name': self.name,
            'balance': self.balance
        }

    def end_turn(self, game):
        pass

    def roll_dice(self):
        return random.randint(1, 6)

    def make_trade(self, game, player):
        pass

def get_player(id):
    for player in data.data['players']:
        if player.id == id:
            return player:
    return None

def get_player_stats(id):
    player = get_player(id)
    if not player:
        raise ValueError('ID does not exist')

    return {
        'name': player.name,
        'balance': player.balance
    }
