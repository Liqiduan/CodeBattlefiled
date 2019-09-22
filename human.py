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

        barPosition = (-self.width/2, self.height/2)
        self.bloodBar = Sprite("sources/bloodBar.png", 
                position=barPosition, anchor=(1,1))
        self.healthBar = Sprite("sources/healthBar.png", 
                position=barPosition, anchor=(0,0))
        self.shieldBar = Sprite("sources/shieldBar.png", 
                position=barPosition, anchor=(0,0))

        self.add(self.bloodBar, z = 0)
        self.add(self.healthBar, z = 1)
        self.add(self.shieldBar, z = 2)

        self.health = 100
        self.shield = 0
        self.updateHealth()

    def hurt(self, harm):
        if self.shield > 0:
            if harm > self.shield:
                harm = harm - self.shield
                self.shield = 0
            else:
                self.shield = self.shield - harm
                harm = 0

        if harm > self.health:
            self.health = 0
        else:
            self.health = self.health - harm

        self.updateHealth()

    def updateHealth(self):
        if self.shield > 0:
            self.shieldBar.opacity = 255
            self.shieldBar.scale_x = self.shield/100
        else:
            self.shieldBar.opacity = 0

        if self.health > 0:
            self.healthBar.opacity = 255
            self.healthBar.scale_x = self.health/100
        else:
            self.healthBar.opacity = 0

