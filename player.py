from cocos.layer import Layer
from cocos.sprite import Sprite
from cocos.actions import MoveTo

class PlayerLayer(Layer):
    def __init__(self):
        Layer.__init__(self)
        self.players = {}

    def add(self, player):
        player.position = 320,240
        self.players[player.name] = player
        Layer.add(self, player)

    def get(self, name):
        return self.players[name]

class Player(Sprite):
    def __init__(self, name="Hero"):
        Sprite.__init__(self, "man.gif")
        self.name = name

    def move(self, x, y):
        self.do( MoveTo((x,y), 1) )
