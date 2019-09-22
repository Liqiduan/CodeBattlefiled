from cocos.director import director
from battlefiled import Battlefiled
from player import Player

director.init()

battlefiled = Battlefiled()
p1 = Player()
battlefiled.player.add(p1)

director.run(battlefiled)
