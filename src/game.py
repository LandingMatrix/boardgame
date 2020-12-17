#imports
import player
import data
import random

class Game():
    def __init__(self, host):
        if data.data['game_host'] != None:
            raise ValueError("Game already exists")
        else:
            self.players = [host]
            data.data['game_host'] = host.id
            self.round = None
            self.is_over = None

    def start(self, host):
        if data.data['game_host'] != host.id:
            raise ValueError("Only host can start game")
        else:
            #set up variables
            self.round = 0
            self.is_over = False

            #shuffle players
            random.shuffle(self.players)

            for player in self.players:
                player.balance = 1500

            #enter main game loop

    def next_round(self):
        for player in self.players:
            player.make_move()


    def abort(self, host):
        if data.data['game_host'] == host.id:
            self.players = []
            self.is_over = True
            data.data['game_host'] = None
        elif self.players == []:
            self.is_over = True
            data.data['game_host'] = None
        else:
            raise ValueError("You do not have permission to abort game")

        is_success = (data.data['game_host'] == None)
        return is_success

if __name__ == '__main__':
    host = player.Player('Jordan')

    game = Game(host) #create_game in game

    player1 = player.Player('Thomas')
    player1.join(game)

    player2 = player.Player('Kean')
    player2.join(game)

    game.start(host)

    while !game.is_over:
        round = game.next_round()
