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
class Scene6(Scene):
    def __init__(self, x, y, player):
        super().__init__(x, y, 1000, 1700, player,3)
        self.background = 'Images/scene6.png'
        self.bgUpper = 'Images/scene6Upper.png'
        # establish enemy spawn locations
        self.spawnLocations = [(650, -900),(855, -400),(830, 240)]

        # create obstacles
        # border
        obs1 = Obstacle(320, -5, 5, 550)
        obs2 = Obstacle(300, 130, 420, 5)
        obs3 = Obstacle(300, 330, 600, 5)
        obs4 = Obstacle(730, -725, 5, 840)
        obs5 = Obstacle(920, -900, 5, 1300)
        obs6 = Obstacle(100, -720, 600, 5)
        obs7 = Obstacle(100, -930, 800, 5)
        obs8 = Obstacle(150, -1000, 5, 300)
        # pillars and statue
        obs9 = Obstacle(260, -820, 60, 20)
        obs10 = Obstacle(355, -820, 60, 15)
        obs11 = Obstacle(455, -820, 55, 20)
        # other objects
        obs12 = Obstacle(667, -740, 5, 5)
        obs13 = Obstacle(830, -920, 60, 40)


        self.obstacles.append(obs1)
        self.obstacles.append(obs2)
        self.obstacles.append(obs3)
        self.obstacles.append(obs4)
        self.obstacles.append(obs5)
        self.obstacles.append(obs6)
        self.obstacles.append(obs7)
        self.obstacles.append(obs8)
        self.obstacles.append(obs9)
        self.obstacles.append(obs10)
        self.obstacles.append(obs11)
        self.obstacles.append(obs12)
        self.obstacles.append(obs13)

        # create statues
        self.statue1 = Statue(385, -820, 700, 70)
        self.statues.append(self.statue1)

    # draw the upper layer of the background
    def drawUpper(self):
        drawImage(self.bgUpper, self.x-4, self.y-5, width=self.w+5, height=self.h+5, align='center')
        self.playerCollision(self.enemies)
        for statue in self.statues:
            statue.chargeStatue(self.player, self.enemies)
            statue.redrawAll(35, 130)


