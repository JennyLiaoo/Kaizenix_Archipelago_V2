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
class Scene3(Scene):
    def __init__(self, x, y, player):
        super().__init__(x, y, 1300, 1000, player,3)
        self.background = 'Images/scene3.png'
        self.bgUpper = 'Images/scene3Upper.png'
        # establish enemy spawn locations
        self.spawnLocations = [(1100, 340), (1400, 240)]

        # create obstacles
        # border
        obs1 = Obstacle(320, 80, 5, 150)
        obs17 = Obstacle(320, 310, 5, 200)
        obs2 = Obstacle(320, 430, 1200, 5)
        obs3 = Obstacle(320, 80, 1200, 5)
        obs4 = Obstacle(1520, 100, 5, 400)
        #other obstacles
        obs5 = Obstacle(320, 80, 80, 55)
        obs6 = Obstacle(550,125, 5, 5)
        obs7 = Obstacle(685, 80, 70, 100)
        obs8 = Obstacle(745, 80, 5, 5)
        obs9 = Obstacle(1000, 110, 5, 5)
        obs10 = Obstacle(880, 150, 5, 5)
        obs14 = Obstacle(1200, 150, 5, 5)
        obs15 = Obstacle(770, 420, 5, 5)
        obs16 = Obstacle(890, 400, 40, 20)
        # statue and pillars
        obs11 = Obstacle(1240, 240, 55, 30)
        obs12 = Obstacle(1400, 160, 60, 40)
        obs13 = Obstacle(1400, 370, 60, 40)


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
        self.obstacles.append(obs14)
        self.obstacles.append(obs15)
        self.obstacles.append(obs16)
        self.obstacles.append(obs17)

        # create statues
        self.statue1 = Statue(1265, 250, 400, 70)
        self.statues.append(self.statue1)

    # draw the upper layer of the background
    def drawUpper(self):
        drawImage(self.bgUpper, self.x, self.y, width=self.w, height=self.h, align='center')
        self.playerCollision(self.enemies)
        for statue in self.statues:
            statue.chargeStatue(self.player, self.enemies)
            statue.redrawAll(30,140)
