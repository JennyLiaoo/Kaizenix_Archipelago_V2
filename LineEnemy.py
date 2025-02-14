"""
Author: Jenny Liao
AndrewID: jliao2,
Section: 1A

Citations:
The image of the enemy is from: https://admurin.itch.io/enemy-slime-1
"""
from Enemy import Enemy
from cmu_graphics import *

# The line enemy moves up and down or left and right (in a line)
class LineEnemy(Enemy):
    # constructor which initializes all line enemy properties/attributes
    def __init__(self, x, y, health, direction, speed,atk, size):
        super().__init__(x, y,size, size, health, 10, atk, speed)
        self.possibleImages = [['Images/slimeLeft1.png', 'Images/slimeRight1.png'],
                               ['Images/slimeLeft2.png', 'Images/slimeRight2.png']]
        self.direction = direction  # tracks if the enemy is moving in the x or y direction
        self.directionSign = 1      # tracks if the enemy is moving positively or negatively
        self.size = size

    # checks if the enemy has collided with an obstacle, and changes its direction
    def checkMove(self, other):
        if (self.isColliding(other) == 'bottom'):
            self.y+=self.speed
            self.directionSign = -self.directionSign
        elif (self.isColliding(other) == 'top'):
            self.y-=self.speed
            self.directionSign = -self.directionSign
        elif (self.isColliding(other) == 'left'):
            self.x -= self.speed
            self.directionSign = -self.directionSign
        elif (self.isColliding(other) == 'right'):
            self.x+=self.speed
            self.directionSign = -self.directionSign

    # moves the enemy forwards in the direction it is going
    def move(self):
        if(self.direction == 'x'):
            self.x+=self.directionSign * self.speed
        else:
            self.y+= self.directionSign * self.speed

    # This function returns whether or not the enemy collides with the obstacle and from which direction
    def isColliding(self, other):
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

    # draws the line enemy
    def redrawAll(self):
        self.changeImage(self.directionSign)
        super().redrawAll()

