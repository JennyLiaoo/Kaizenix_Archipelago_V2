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
class Scene5(Scene):
    def __init__(self, x, y, player):
        super().__init__(x, y, 1300, 700, player,2)
        self.background = 'Images/scene5.png'
        self.bgUpper = 'Images/scene5Upper.png'
        # establish enemy spawn locations
        self.spawnLocations = [(600, 100)]

        # create obstacles
        # border
        obs1 = Obstacle(820, 200, 150, 5)
        obs2 = Obstacle(-280, 450, 1200, 5)
        obs3 = Obstacle(295, -5, 5, 600)
        obs4 = Obstacle(300, 45, 700, 5)
        obs5 = Obstacle(820, 200, 5, 300)
        obs6 = Obstacle(370, 200, 370, 80)
        obs7 = Obstacle(295, 200, 100, 5)

        #statue
        obs8 = Obstacle(325, 120, 30, 20)
        # other objects
        obs9 = Obstacle(400, 60, 5, 5)
        obs10 = Obstacle(450, 75, 80, 20)
        obs11 = Obstacle(655, 85, 5, 10)
        obs12 = Obstacle(395, 150, 20, 20)
        obs20 = Obstacle(955, 60, 5, 120)
        obs13 = Obstacle(930, 60, 45, 15)
        obs14 = Obstacle(930, 180, 45, 15)
        obs15 = Obstacle(300, 410, 70, 40)
        obs16 = Obstacle(510, 310, 5, 5)
        obs17 = Obstacle(710, 300, 20, 20)
        obs18 = Obstacle(678, 350, 5, 5)
        obs19 = Obstacle(770, 420, 20, 20)

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
        self.obstacles.append(obs18)
        self.obstacles.append(obs19)
        self.obstacles.append(obs20)

        # create statues
        self.statue1 = Statue(350, 120, 600, 60)
        self.statues.append(self.statue1)


    # draw the upper layer of the background
    def drawUpper(self):
        drawImage(self.bgUpper, self.x+3, self.y, width=self.w+5, height=self.h, align='center')
        self.playerCollision(self.enemies)
        for statue in self.statues:
            statue.chargeStatue(self.player, self.enemies)
            statue.redrawAll(40,90)
