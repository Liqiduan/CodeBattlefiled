from cocos.sprite import Sprite
from cocos.actions import MoveTo

class Player(Sprite):
    def __init__(self, name="Hero"):
        Sprite.__init__(self, "man.gif")
        self.name = name

    def move(self, x, y):
        self.do( MoveTo((x,y), 1) )
