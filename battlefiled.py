from cocos.layer import Layer
from cocos.scene import Scene
from cocos.text import Label

from player import PlayerLayer

class Battlefiled(Scene):
    def __init__(self):
        super(Battlefiled, self).__init__()
        
        self.background = Layer()
        self.map = Layer()
        self.item = Layer()
        self.player = PlayerLayer()

        self.add(self.player)
        self.add(self.background)
        self.add(self.item)
        self.add(self.map)

        label = Label(
                'Battlefiled',
                font_name = 'Times New Roman',
                font_size = 32,
                anchor_x='center', anchor_y='center'
                )
        label.position = 320, 50
        self.background.add(label)

