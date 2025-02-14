"""
Author: Jenny Liao
AndrewID: jliao2,
Section: 1A

Citations:
The image of the enemy is from: https://monopixelart.itch.io/forest-monsters-pixel-art
"""
from Enemy import Enemy
import math
from cmu_graphics import *


# The follower enemy follows players that are in their aggro radius. However, it can get stuck on obstacles.
class FollowerEnemy(Enemy):
    # constructor which initializes all follower enemy properties/attributes
    def __init__(self, x, y, health, size, radius, speed, atk):
        super().__init__(x, y, size, size, health, 10, atk, speed)
        self.possibleImages = [['Images/mushLeft1.png', 'Images/mushRight1.png'],
                               ['Images/mushLeft2.png', 'Images/mushRight2.png']]
        self.radius = radius  # enemy aggro radius
        self.directionCannotMove = []  # tracks all directions that have obstacles in the way
        self.size = size
        self.canMove = True

    # checks if the enemy has collided with an obstacle
    def checkMove(self, other):
        collidingWith = self.isColliding(other)
        if (collidingWith != []):
            self.canMove = False
            return True
        else:
            self.canMove = True
            return False

    # checks all directions the enemy is colliding with the obstacles from
    def isColliding(self, other):
        self.directionCannotMove = []
        if (self.x + self.size >= other.x and self.x <= other.x + other.w and self.almostEqual(self.y,
                                                                                               other.y + other.h)):
            self.directionCannotMove.append('bottom')
        elif (self.y + self.size >= other.y and self.y <= other.y + other.h and self.almostEqual(self.x + self.size,
                                                                                                 other.x)):
            self.directionCannotMove.append('left')
        elif (self.x + self.size >= other.x and self.x <= other.x + other.w and self.almostEqual(self.y + self.size,
                                                                                                 other.y)):
            self.directionCannotMove.append('top')
        elif (self.y + self.size >= other.y and self.y <= other.y + other.h and self.almostEqual(self.x,
                                                                                                 other.x + other.w)):
            self.directionCannotMove.append('right')
        return self.directionCannotMove

    # moves the follower enemy towards the player
    def move(self, player):
        disX = player.x - self.x
        disY = player.y - self.y
        self.changeImage(disX)
        # checks if the player is within enemy aggro radius
        distance = math.sqrt((player.x - self.x) ** 2 + (player.y - self.y) ** 2)
        if (distance > self.radius):
            return
        ratio = self.speed / distance
        disX *= ratio
        disY *= ratio
        if (self.canMove):
            self.x += disX
            self.y += disY
        else:       # undoes the movement if enemy is colliding with an obstacle, ensures that enemy gets unstuck
            if ('right' in self.directionCannotMove):
                self.x -= disX
            if ('left' in self.directionCannotMove):
                self.x -= disX
            if ('top' in self.directionCannotMove):
                self.y -= disY
            if ('bottom' in self.directionCannotMove):
                self.y -= disY

    # returns true if two values are almost equal to one another
    def almostEqual(self, num1, num2):
        if (abs(num1 - num2) < 5):
            return True
        return False
