"""
Author: Jenny Liao
AndrewID: jliao2,
Section: 1A

Citations:
See image citations through Main.py
"""
from Scene import Scene
from Statue import Statue
from Obstacle import Obstacle
from cmu_graphics import *

# for increasing maximum recursion depth
import sys
sys.setrecursionlimit(10**6)
class Scene4(Scene):
    def __init__(self, x, y, player):
        super().__init__(x, y, 900, 1000, player,4)

        self.background = 'Images/scene4.png'
        self.bgUpper = 'Images/scene4Upper.png'
        # establish enemy spawn locations
        self.spawnLocations = [(325, 500)]

        # create obstacles
        # border
        obs1 = Obstacle(115, 200, 10, 400)
        obs2 = Obstacle(115, 235, 120, 5)
        obs3 = Obstacle(430, 235, 120, 5)
        obs4 = Obstacle(550, 200, 10, 400)
        obs6 = Obstacle(115, 610, 500, 5)
        #statue
        obs5 = Obstacle(300, 410, 80, 40)


        self.obstacles.append(obs1)
        self.obstacles.append(obs2)
        self.obstacles.append(obs3)
        self.obstacles.append(obs4)
        self.obstacles.append(obs5)
        self.obstacles.append(obs6)

        # create statues
        self.statue1 = Statue(340, 430,500, 100)
        self.statues.append(self.statue1)



    # draw the upper layer of the background
    def drawUpper(self):
        drawImage(self.bgUpper, self.x, self.y+5, width=self.w+10, height=self.h, align='center')
        self.playerCollision(self.enemies)
        for statue in self.statues:
            statue.chargeStatue(self.player, self.enemies)
            statue.redrawAll(50,200)




