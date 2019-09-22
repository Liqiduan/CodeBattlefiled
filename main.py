from cocos.director import director
from battlefiled import Battlefiled
from player import Player

director.init(1600,800)

battlefiled = Battlefiled()
battlefiled.newPlayer("Hero")

director.run(battlefiled)
