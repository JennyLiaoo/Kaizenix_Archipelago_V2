"""
Author: Jenny Liao
AndrewID: jliao2,
Section: 1A

Citations:
The image is from = https://itch.io/c/475845/game-assets
"""
from cmu_graphics import *

# the weapon used to attack enemies
class Weapon:

    def __init__(self, images, atk, width, height, timeAtk):
        self.images = images
        self.image = images[0]
        self.atk = atk
        self.height = height
        self.width = width
        self.imageWidth = width
        self.imageHeight = height
        self.attacking = False
        self.drawn = False
        self.drawnCounter = 0       # weapon is drawn for a certain amount of time
        self.timeAtk = timeAtk
        self.x, self.y = None, None


    # changes the image/direction of the weapon
    def changeImage(self, imageIndex, possibleImages=[]):
        self.playerImage = possibleImages[imageIndex]

    # changes the location of the weapon and the weapon's image depending on the player's direction and location
    def changeLocation(self, playerDirection, playerX, playerY, playerWidth, playerHeight):
        if(playerDirection == 'front'):
            self.image =self.images[2]
            self.x = playerX
            self.y = playerY+playerHeight
            self.imageWidth = self.width
            self.imageHeight = self.height
        elif (playerDirection == 'back'):
            self.image = self.images[0]
            self.x = playerX
            self.y = playerY - self.height
            self.imageWidth = self.width
            self.imageHeight = self.height
        elif (playerDirection == 'left'):
            self.image = self.images[3]
            self.x = playerX - self.height
            self.y = playerY
            self.imageWidth = self.height
            self.imageHeight = self.width
        elif (playerDirection == 'right'):
            self.image = self.images[1]
            self.x = playerX+playerWidth
            self.y = playerY
            self.imageWidth = self.height
            self.imageHeight = self.width

    # draws the weapon
    def redrawAll(self):
        drawImage(self.image, self.x, self.y, width=self.imageWidth, height=self.imageHeight)
        self.drawnCounter+=1

    # checks for the weapons overlap with enemies
    def checkCollisions(self, other):
        r1 = (self.x, self.y, self.x+self.imageWidth, self.y+self.imageHeight)
        r2 = (other.x, other.y , other.x + other.w, other.y+ other.h)
        if(r1[2] <= r2[0] or r2[2] <= r1[0]):
            return None
        if(r1[3]<=r2[1] or r2[3]<=r1[1]):
            return None
        return 1
