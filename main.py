from cocos.director import director
from battlefiled import Battlefiled
from player import Player

director.init()

battlefiled = Battlefiled()
battlefiled.newPlayer("Hero")

director.run(battlefiled)
