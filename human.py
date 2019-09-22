from cocos.text import Label
from cocos.sprite import Sprite

class Human(Sprite):
    def __init__(self, name="Hero"):
        self.name = name
        Sprite.__init__(self, "sources/man.gif")

        self.nameLabel = Label(name, 
                anchor_x='center', anchor_y="bottom")
        self.nameLabel.position = (0, self.height/2)
        self.add(self.nameLabel)

