import cocos

from random import randint

from cocos.layer import Layer
from cocos.scene import Scene
from cocos.text import Label
from cocos.actions import ScaleTo
from cocos.actions import Place

from player import Player
from player import PlayerLayer

class Poisoner():
    warnning_color = (200,200,200)
    poison_color = (255,192,192)

    def __init__(self, map):
        self.map = map
        self.posion_center = (0,0)
        self.posion_radius = 0

    def filterPoisoned(self, objs):
        ret = []
        x, y = self.posion_center
        r = self.posion_radius
        for i in objs:
            if (i.x - x)**2 + (i.y - y)**2 > r**2:
                ret.append(i)
        return ret

    def setWarningRegion(self, center, r):
        self.highlightRegion(center, r, self.warnning_color)

    def setPoisonRegion(self, center, r):
        self.posion_center = center
        self.posion_radius = r
        self.highlightRegion(center, r, self.poison_color)

    def highlightRegion(self, center, r, color):
        x, y = self.map.get_at_pixel(center[0], center[1]).center
        for l in self.map.cells:
            for c in l:
                px, py = c.center
                if (px - x)**2 + (py - y)**2 < r**2:
                    continue

                cx, cy = c.position
                self.map.set_cell_color(cx, cy, color)

class Battlefiled(Scene):
    is_event_handler = True

    def __init__(self):
        super(Battlefiled, self).__init__()
        
        self.background = Layer()
        self.player = PlayerLayer()

        self.map = cocos.tiles.load('sources/map.tmx')['map']
        self.map.set_view(0,0,16*32,16*32)

        self.add(self.map)
        self.add(self.background)
        self.add(self.player)

        label = Label(
                'Battlefiled',
                font_name = 'Times New Roman',
                font_size = 32,
                anchor_x='center', anchor_y='center'
                )
        label.position = 512, 20
        self.background.add(label)

        self.posion = Poisoner(self.map)
        self.posion.setPoisonRegion((64,64),128)

        self.schedule_interval(self.schedWork, 1)

    def schedWork(self, i):
        players = self.player.getAll()
        for p in self.posion.filterPoisoned(players):
            p.human.hurt(10)

    def newPlayer(self, name):
        p = Player(self.map, name)

        width = len(self.map.cells) - 1
        height = len(self.map.cells[0]) - 1
        x,y = randint(0, width), randint(0, height)
        p.position = tuple(self.map.cells[x][y].center)

        self.player.add(p)

