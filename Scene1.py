"""
Author: Jenny Liao
AndrewID: jliao2,
Section: 1A

Citations:
See image citations through Main.py
"""
from Glow import Glow
from Scene import Scene
from Statue import Statue
from Obstacle import Obstacle
from cmu_graphics import *
class Scene1(Scene):
    def __init__(self, x, y, player):
        super().__init__(x, y, 1500, 1150, player, 1)
        self.background = 'Images/scene1.png'
        self.bgUpper = 'Images/scene1Upper.png'
        # establish enemy spawn locations
        self.spawnLocations = [(330,80), (630,530), (530,230),(0,80),(730,80),(130,530)]

        # create obstacles
        obs1 = Obstacle(100, 320, 190, 100)
        obs2 = Obstacle(400, 320, 180, 90)
        obs3 = Obstacle(255, 290, 30, 170)
        obs4 = Obstacle(400, 290, 30, 170)
        obs5 = Obstacle(255, 160, 175, 30)
        obs6 = Obstacle(95, 160, 5, 170)
        obs7 = Obstacle(100, 155, 495, 5)
        obs8 = Obstacle(585, 160, 5, 170)
        obs9 = Obstacle(160, 220, 15, 15)
        # bench
        obs10 = Obstacle(100, 220, 25, 70)
        obs11 = Obstacle(560, 220, 25, 70)
        # columns
        obs12 = Obstacle(95, 110, 40, 10)
        obs13 = Obstacle(550, 110, 40, 10)
        obs14 = Obstacle(120, 40, 40, 10)
        obs15 = Obstacle(520, 40,  40, 10)
        obs16 = Obstacle(195, -10, 40, 10)
        obs17 = Obstacle(445, -10, 40, 10)
        obs18 = Obstacle(325, -30, 40, 10)
        obs19 = Obstacle(330, 45, 20, 20)
        #border
        obs20 = Obstacle(-150, 710, 1050, 5)
        obs21 = Obstacle(-175, 560, 50, 200)
        obs22 = Obstacle(-185, -50, 5, 900)
        obs23 = Obstacle(-185, -55, 1000, 5)
        obs56 = Obstacle(920, -270, 100, 5)
        obs24 = Obstacle(700, -300, 220, 250)
        obs25 = Obstacle(1030, -300, 220, 250)
        obs26 = Obstacle(-130, -40, 140, 35)
        obs27 = Obstacle(80, -35, 15, 5)
        obs28 = Obstacle(-80, 10, 40, 35)
        obs29 = Obstacle(-120, 285, 15, 5)
        obs30 = Obstacle(-170, 380, 30, 55)
        obs31 = Obstacle(30, 430, 15, 5)
        # bottom left
        obs32 = Obstacle(-50, 680, 70, 10)
        obs33 = Obstacle(80, 450, 15, 5)
        obs34 = Obstacle(70, 600, 90, 15)
        # bottom
        obs35 = Obstacle(260, 560, 5, 5)
        obs36 = Obstacle(420, 600, 35, 5)
        obs37 = Obstacle(540, 575, 5, 5)
        obs38 = Obstacle(620, 580, 45, 10)
        obs39 = Obstacle(765, 450, 5, 5)
        obs40 = Obstacle(820, 640, 5, 5)
        obs41 = Obstacle(855, 640, 5, 50)
        obs57 = Obstacle(855, 660, 50, 5)
        obs42 = Obstacle(935, 350, 5, 400)
        #mid right
        obs43 = Obstacle(640, 40, 5, 5)
        obs44 = Obstacle(610, 285, 20, 5)
        obs45 = Obstacle(790, -5, 5, 5)
        obs46 = Obstacle(814, 73, 5, 5)
        obs47 = Obstacle(880, -25, 30, 70)
        obs48 = Obstacle(940, 170, 5, 5)
        #right
        obs49 = Obstacle(1130, 150, 40, 5)
        obs50 = Obstacle(1180, 240, 30, 100)
        obs51 = Obstacle(1090, 330, 5, 5)
        obs52 = Obstacle(1030, -25, 30, 90)
        obs53 = Obstacle(1170, -10, 5, 5)
        #right-border
        obs54 = Obstacle(935, 345, 350, 5)
        obs55 = Obstacle(1245, -30, 5, 400)


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
        self.obstacles.append(obs32)
        self.obstacles.append(obs33)
        self.obstacles.append(obs34)
        self.obstacles.append(obs35)
        self.obstacles.append(obs36)
        self.obstacles.append(obs37)
        self.obstacles.append(obs38)
        self.obstacles.append(obs39)
        self.obstacles.append(obs40)
        self.obstacles.append(obs41)
        self.obstacles.append(obs42)
        self.obstacles.append(obs43)
        self.obstacles.append(obs44)
        self.obstacles.append(obs45)
        self.obstacles.append(obs46)
        self.obstacles.append(obs47)
        self.obstacles.append(obs48)
        self.obstacles.append(obs49)
        self.obstacles.append(obs50)
        self.obstacles.append(obs51)
        self.obstacles.append(obs52)
        self.obstacles.append(obs53)
        self.obstacles.append(obs54)
        self.obstacles.append(obs55)
        self.obstacles.append(obs56)
        self.obstacles.append(obs57)

        # create statues
        self.statue1 = Statue(340, 180, 100, 60)
        self.statue2 = Statue(-60, 30, 200, 60)
        self.statues.append(self.statue1)
        self.statues.append(self.statue2)

        # create glows
        self.glow0 = Glow(100, 75, 30, 65, 'Images/glow1.png')
        self.glow1 = Glow(128, -5, 30, 60, 'Images/glow2.png', )
        self.glow2 = Glow( 196, -75, 40, 85, 'Images/glow3.png')
        self.glow3 = Glow(322, -100, 40, 85,'Images/glow3.png')
        self.glow4 = Glow( 448, -75, 40, 85, 'Images/glow3.png')
        self.glow5 = Glow( 530, -5, 30, 60, 'Images/glow2.png')
        self.glow6 = Glow( 552, 75, 30, 65, 'Images/glow1.png')
        self.glow7 = Glow(270, 140, 150, 140, 'Images/glowAll.png')
        self.glows = []
        self.glows.append(self.glow0)
        self.glows.append(self.glow1)
        self.glows.append(self.glow2)
        self.glows.append(self.glow3)
        self.glows.append(self.glow4)
        self.glows.append(self.glow5)
        self.glows.append(self.glow6)
        self.glows.append(self.glow7)

        # keep track of game over status
        self.gameWin = False

    # draw the upper layer of the background
    def drawUpper(self):
        drawImage(self.bgUpper, self.x+2,self.y, width=self.w+10,height=self.h+5,align = 'center')
        self.playerCollision(self.enemies)  # check player collisions with enemies
        for glow in self.glows:
            glow.redrawAll()
        for statue in self.statues:
            statue.chargeStatue(self.player, self.enemies)
            statue.redrawAll(28,110)

    # updates scene position
    def add(self, xAdd, yAdd):
        super().add(xAdd, yAdd)
        for glow in self.glows:
            glow.add(xAdd,yAdd)


    # draws glows for completed statues
    def drawGlow(self, completedStatues):
        counter = 0
        if(0 in completedStatues):
            self.glow0.drawn = True
            counter+=1
        if (1 in completedStatues):
            self.glow1.drawn = True
            counter += 1
        if (2 in completedStatues):
            self.glow2.drawn = True
            counter += 1
        if (3 in completedStatues):
            self.glow3.drawn = True
            counter += 1
        if (4 in completedStatues):
            self.glow4.drawn = True
            counter += 1
        if (5 in completedStatues):
            self.glow5.drawn = True
            counter += 1
        if (6 in completedStatues):
            self.glow6.drawn = True
            counter += 1
        if(counter == 7):
            self.glow7.drawn = True
            self.gameWin = True


