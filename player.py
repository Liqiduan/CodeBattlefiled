from math import sqrt
from cocos.cocosnode import CocosNode
from cocos.layer import Layer
from cocos.actions import MoveTo
from cocos.tiles import HexMap

from human import Human

class Player(CocosNode):
    def __init__(self, map, name='Player'):
        CocosNode.__init__(self)

        self.map = map
        self.name = name
        self.human = Human(name)
        self.add(self.human)

    def move(self, direct):
        pos = self.map.get_neighbor(self.cell(), direct).center
        self.do( MoveTo(pos, 1) )

    def cell(self):
        return self.map.get_at_pixel(self.x, self.y)

    def where(self):
        c = self.cell()
        return c.x, c.y

class PlayerLayer(Layer):
    is_event_handler = True
    def __init__(self):
        Layer.__init__(self)
        self.players = {}
        self.action = None

    def add(self, player):
        self.players[player.name] = player
        Layer.add(self, player)

    def get(self, name):
        return self.players[name]
    
    def getAll(self):
        return self.players.values()

    def on_mouse_press(self, x, y, buttons, modifier):
        p = self.players.get('Hero')

        if not self.action == None:
            p.remove_action(self.action)

        self.action = p.do(
                MoveTo((x, y), duration=sqrt(x**2 + y**2)/32.0))
