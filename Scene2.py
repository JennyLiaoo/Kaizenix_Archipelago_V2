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

class Scene2(Scene):
    def __init__(self, x, y, player):
        super().__init__(x, y, 1300, 1250, player, 2)
        self.background = 'Images/scene2.png'
        self.bgUpper = 'Images/scene2Upper.png'
        # establish enemy spawn locations
        self.spawnLocations = [(-230, -250),(220, -200),(670, 150)]

        # create obstacles
        # square
        obs1 = Obstacle(10, -90, 60, 40)
        obs2 = Obstacle(10, -310, 60, 40)
        obs3 = Obstacle(10, -500, 60, 40)
        obs4 = Obstacle(210, -500, 60, 40)
        obs5 = Obstacle(410, -500, 60, 40)
        obs6 = Obstacle(410, -310, 60, 40)
        obs7 = Obstacle(410, -90, 60, 40)
        obs8 = Obstacle(210, -120, 60, 40)
        #statue + coffin
        obs9 = Obstacle(210, -360, 65, 35)
        obs10 = Obstacle(180, -275, 120, 40)
        # trees
        obs11 = Obstacle(-100, -250, 10, 10)
        obs12 = Obstacle(300, -520, 10, 10)
        obs13= Obstacle(505, -215, 10, 10)
        obs14 = Obstacle(335, 65, 10, 10)
        obs15 = Obstacle(35,220, 10, 10)
        obs16 = Obstacle(700, 125, 10, 10)
        #border
        obs17 = Obstacle(-320, -330, 5, 550)
        obs18 = Obstacle(-320, 270, 1200, 5)
        obs19 = Obstacle(870, 40, 5, 200)
        obs20 = Obstacle(550, 70, 300, 5)
        obs21 = Obstacle(555, -600, 5, 680)
        obs24 = Obstacle(-90, -590, 1000, 5)
        obs22 = Obstacle(-90, -600, 5, 280)
        obs23 = Obstacle(-300, -330, 200, 5)
        # other things
        obs25 = Obstacle(-320, -10, 30, 60)
        obs26 = Obstacle(-90, -15, 60, 30)
        obs27 = Obstacle(-320, 180, 150, 80)
        obs28 = Obstacle(220, 210, 40, 30)
        obs29 = Obstacle(420, 210, 40, 25)
        obs30 = Obstacle(820, 190, 40, 80)
        obs31 = Obstacle(820, 80, 40, 40)


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
        self.obstacles.append(obs21)
        self.obstacles.append(obs22)
        self.obstacles.append(obs23)
        self.obstacles.append(obs24)
        self.obstacles.append(obs25)
        self.obstacles.append(obs26)
        self.obstacles.append(obs27)
        self.obstacles.append(obs28)
        self.obstacles.append(obs29)
        self.obstacles.append(obs30)
        self.obstacles.append(obs31)

        # create statues
        self.statue1 = Statue(240, -350, 300, 75)
        self.statues.append(self.statue1)

    # draw the upper layer of the background
    def drawUpper(self):
        drawImage(self.bgUpper, self.x, self.y-10, width=self.w, height=self.h, align='center')
        self.playerCollision(self.enemies)
        for statue in self.statues:
            statue.chargeStatue(self.player, self.enemies)
            statue.redrawAll(40,130)

