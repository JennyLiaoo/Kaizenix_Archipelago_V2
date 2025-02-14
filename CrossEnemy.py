"""
Author: Jenny Liao
AndrewID: jliao2,
Section: 1A

Citations:
The image of the enemy is from: https://admurin.itch.io/enemy-slime-1
"""
from LineEnemy import LineEnemy
from cmu_graphics import *
import random


# The cross enemy class that is used to define an enemy that moves up, down, left and right randomly (in a cross)
class CrossEnemy(LineEnemy):
    # constructor which initializes all cross enemy properties/attributes
    def __init__(self, x, y, health, direction, speed, size, atk):
        super().__init__(x, y, health, direction, speed, atk, size)
        self.possibleImages = [['Images/slimeLeft1.png', 'Images/slimeRight1.png'],
                               ['Images/slimeLeft2.png', 'Images/slimeRight2.png']]
        self.direction = direction  # tracks if the enemy is moving in the x or y direction
        self.directionSign = 1      # tracks if the enemy is moving positively or negatively
        self.size = size

    # checks if the enemy has collided with an obstacle, and from what direction it collided from
    def checkMove(self, other):
        collided = False
        if (self.isColliding(other) == 'bottom'):
            self.y += self.speed  # undoes the movement
            collided = True
        elif (self.isColliding(other) == 'top'):
            self.y -= self.speed
            collided = True
        elif (self.isColliding(other) == 'left'):
            self.x -= self.speed
            collided = True
        elif (self.isColliding(other) == 'right'):
            self.x += self.speed
            collided = True
        if (collided):  # changes the direction of the enemy if it collided with an obstacle
            self.changeDirection()

    # randomly changes the direction of the enemy
    def changeDirection(self):
        self.directionSign, self.direction = self.randomize(self.directionSign, self.direction)

    # This function acts as a randomizer, and is used as a helper to change the direction of the enemy
    def randomize(self, oldDirectionSign, oldDirection):
        diceRoll1 = random.randrange(0, 2)
        diceRoll2 = random.randrange(0, 2)
        # change the sign
        if (diceRoll1 == 0):
            directionSign = 1
        else:
            directionSign = -1
        # change the direction
        if (diceRoll2 == 0):
            direction = 'x'
        else:
            direction = 'y'
        # if the sign and direction remains the same, we try again to avoid repeating the same direction
        if ((directionSign, direction) == (oldDirectionSign, oldDirection)):
            return self.randomize(oldDirectionSign, oldDirection)
        else:
            return directionSign, direction
