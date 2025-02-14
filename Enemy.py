"""
Author: Jenny Liao
AndrewID: jliao2,
Section: 1A

Citations:
The image of the enemy is from: https://admurin.itch.io/enemy-slime-1
"""
from cmu_graphics import *
import random


# The enemy class that is used to keep track of the enemies' properties
class Enemy:
    # constructor which initializes all enemy properties/attributes
    def __init__(self, x, y, w, h, health, range, atk, speed):
        self.possibleImages = [['Images/wizLeft1.png', 'Images/wizRight1.png'],
                               ['Images/wizLeft2.png', 'Images/wizRight2.png']]  # placeholder images
        self.totalHealth = health   # maximum enemy health
        self.health = health        # current enemy health
        self.range = range          # enemy attack range
        self.atk = atk
        self.x, self.y = x, y
        self.w = w
        self.h = h
        self.currentImage = self.possibleImages[0]
        self.playerImage = self.currentImage[0]  # current character sprite being displayed
        self.exp = self.getExp()  # the amount of experience points dropped by the enemy
        self.speed = speed
        self.counter = 0  # counter for animation frames

    # generates a random number to represent the amount of experience points dropped by the enemy
    def getExp(self):
        return random.choice([1, 2, 3, 4, 5])

    # Updates the enemy position based on where the player is relative to the scene
    def add(self, xAdd, yAdd):
        self.x += xAdd
        self.y += yAdd

    # updates the sprite image based on the direction of movement
    def changeImage(self, directionSign):
        if (directionSign > 0):
            self.playerImage = self.currentImage[1]
        else:
            self.playerImage = self.currentImage[0]

    # draws the enemy sprite and its health bar
    def redrawAll(self):
        # update sprite picture based on current frame
        if (self.counter % 5 == 0 and self.counter < 10):
            self.currentImage = self.possibleImages[0]
        elif (self.counter % 10 == 0):
            self.currentImage = self.possibleImages[1]
            self.counter = 0
        self.counter = self.counter + 1
        drawImage(self.playerImage, self.x, self.y, width=self.w, height=self.h)
        # draw health bar
        drawRect(self.x, self.y - 10, self.w, 5, fill='red')
        bar = self.w * self.health // self.totalHealth
        if (int(bar) != 0):
            drawRect(self.x, self.y - 10, int(bar), 5, fill='green')


    # all enemies have a function to check if they can move
    # this is automatically true unless a subclass overwrites this function with their own unique conditions
    def checkMove(self, other):
        return True