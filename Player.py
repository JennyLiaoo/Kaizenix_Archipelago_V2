"""
Author: Jenny Liao
AndrewID: jliao2,
Section: 1A

Citations:
Images from https://craftpix.net/
"""
from Weapon import Weapon
from cmu_graphics import *

# the class that holds all player information
class Player:
    def __init__(self, x, y):
        # player images
        self.possibleImages = [['Images/catBack1.png', 'Images/catFront1.png', 'Images/catLeft1.png', 'Images/catRight1.png'],
                               ['Images/catBack2.png', 'Images/catFront2.png', 'Images/catLeft2.png','Images/catRight2.png']]
        self.currentImage = self.possibleImages[0]
        self.playerImage = self.currentImage[0]

        # player location/dimensions
        self.x = x
        self.y = y
        self.size = 35
        self.direction = 'front'

        # player stats
        self.atk = 10
        self.totalHealth = 100
        self.health = self.totalHealth
        self.lvl = 0
        self.exp = 0
        self.speed = 15

        # player counters/status
        self.counter = 0    # frame counter
        self.immunityDuration = 50
        self.immuneCounter = 0
        self.immune = False
        self.cooldown = False
        self.cooldownCounter = 0
        self.cooldownDuration = 20
        self.teleportCounter = 0
        self.teleportTime = 50

        # player weapon
        self.weapon = Weapon(['Images/weapon0.png', 'Images/weapon1.png', 'Images/weapon2.png', 'Images/weapon3.png'], 10, self.size, self.size, 15)
        self.weaponDrawn = False



    # updates player position
    def add(self, xAdd, yAdd):
        self.x += xAdd
        self.y += yAdd


    # changes player image based on player direction
    def changeImage(self, imageIndex):
        self.playerImage = self.currentImage[imageIndex]

    # draws the player
    def redrawAll(self):
        drawImage(self.playerImage, self.x,self.y,  width=self.size,height=self.size)
        # increments immunity counter and displays the immunity bar
        if(self.immune==True):
            if(self.immuneCounter <self.immunityDuration):
                self.immuneCounter+=1
                drawRect(self.x, self.y - 20, self.size, 5, fill='blue')
                bar = self.size * self.immuneCounter // self.immunityDuration
                if (int(bar) > 0):
                    drawRect(self.x, self.y - 20, int(bar), 5, fill='grey')
            else:
                self.immune = False
                self.immuneCounter = 0

        # alternates between walking images
        if(self.counter%5==0 and self.counter < 10):
            self.currentImage = self.possibleImages[0]
        elif(self.counter%10==0):
            self.currentImage = self.possibleImages[1]
            self.counter = 0
        self.counter = self.counter+1

        # update attack cooldown duration
        if(self.cooldown == True):
            self.cooldownCounter += 1
            if (self.cooldownCounter > self.cooldownDuration):
                self.cooldown = False
                self.cooldownCounter = 0

        # draws the player's weapon
        if(self.weaponDrawn == True):
            self.weapon.redrawAll()
            if(self.weapon.drawnCounter >= self.weapon.timeAtk):
                self.weaponDrawn = False
                self.weapon.drawnCounter = 0

        # draws player health bar
        drawRect(self.x, self.y - 10, self.size, 5, fill='red')
        bar = self.size * self.health // self.totalHealth
        if (int(bar) > 0):
            drawRect(self.x, self.y - 10, int(bar), 5, fill='green')
        self.checkLvl()

    # changes the player's stats based on the amount of experience points it has
    def checkLvl(self):
        if(self.exp >= 70):
            self.lvl = 5
            self.totalHealth = 300
            self.immunityDuration = 30
            self.atk = 50
        elif(self.exp >= 50):
            self.totalHealth = 250
            self.lvl = 4
            self.atk = 40
            self.cooldownDuration = 10
        elif (self.exp >= 35):
            self.atk = 30
            self.lvl = 3
            self.totalHealth = 200
            self.immunityDuration = 40
        elif (self.exp >= 20):
            self.lvl = 2
            self.totalHealth = 150
            self.atk = 20
            self.cooldownDuration = 15
        elif(self.exp >= 10):
            self.atk = 15
            self.lvl = 1
            self.totalHealth = 120
            self.immunityDuration = 45

    # handles the player weapon when the player attacks
    def hitAnimation(self, enemies):
        # increment player animation
        self.cooldown = True
        self.weapon.changeLocation(self.direction, self.x, self.y, self.size, self.size)
        self.depleteEnemyHealth(enemies)
        self.weaponDrawn = True

    # checks if the player's weapon overlaps with any enemies (and depletes their health if it is)
    def depleteEnemyHealth(self, enemies):
        for enemy in enemies:
            if(self.weapon.checkCollisions(enemy) != None):
                enemy.health -= (self.weapon.atk+self.atk)

    # checks for player collision with obstacles, and from what direction it is colliding
    def checkCollisions(self, other):
        if(self.x + self.size >= other.x and self.x <= other.x+other.w and
                other.y + other.h - 5 <= self.y <= other.y + other.h + 5):
            return 'bottom'
        elif(self.y + self.size >= other.y and self.y <= other.y + other.h and
             self.x + self.size <= other.x+5 and self.x+self.size >=other.x-5):
            return 'left'
        elif (self.x + self.size >= other.x and self.x <= other.x + other.w and
              self.y + self.size >= other.y-5 and self.y+self.size <= other.y+5):
            return 'top'
        elif (self.y + self.size >= other.y and self.y <= other.y + other.h and
              other.x + other.w + 5 >= self.x >= other.x + other.w - 5):
            return 'right'

    # check for player overlap with enemies
    def isColliding(self, other):
        x1,y1,x2,y2 = self.x,self.y,self.x+self.size, self.y+self.size
        x3,y3,x4,y4 = other.x,other.y,other.x+other.w, other.y+other.h
        if(x2 <= x3 or x4 <=x1):
            return False
        if(y2<=y3 or y4 <= y1):
            return False
        return True

