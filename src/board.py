#imports

class Board():
    def __init__(self):
        with properties as open("tiles.txt"):
            for line in properties:
                print(line)
                #create estate


class Estate():
    def __init__(self, position, name, set, value): #automated with text file
        self.owner = None
        self.position = position
        self.name = name
        self.set = set # "Brown"?
        self.value = value
        self.house_price = 0
        self.rent = [] #default, set (double), 1 house, 2 house, 3 house, 4 house, hotel
        self.level = 0 #index for rent
        self.mortgaged = False

#sets: Brown, Light blue, Magenta, Orange, Red, Yellow, Green, Dark Blue, Train, Utility
