import cocos

from random import randint

from cocos.layer import Layer
from cocos.scene import Scene
from cocos.text import Label
from cocos.actions import ScaleTo
from cocos.actions import Place

from player import Player
from player import PlayerLayer

class Battlefiled(Scene):
    def __init__(self):
        super(Battlefiled, self).__init__()
        
        self.background = Layer()
        self.player = PlayerLayer()

        self.map = cocos.tiles.load('map.tmx')['map']
        self.map.set_view(0,0,16*32,16*32)

        self.add(self.background)
        self.add(self.map)
        self.add(self.player)

        label = Label(
                'Battlefiled',
                font_name = 'Times New Roman',
                font_size = 32,
                anchor_x='center', anchor_y='center'
                )
        label.position = 512, 20
        self.background.add(label)

    def newPlayer(self, name):
        p = Player(self.map, name)

        width = len(self.map.cells) - 1
        height = len(self.map.cells[0]) - 1
        x,y = randint(0, width), randint(0, height)
        p.position = tuple(self.map.cells[x][y].center)

        self.player.add(p)
