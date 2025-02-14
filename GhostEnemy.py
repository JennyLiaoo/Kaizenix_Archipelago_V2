"""
Author: Jenny Liao
AndrewID: jliao2,
Section: 1A

Citations:
The image of the enemy is from: https://pop-shop-packs.itch.io/ghost-pixel-asset-pack
"""
from Enemy import Enemy
import math
from cmu_graphics import *

# The ghost enemy follows the player while ignoring any obstacles
class GhostEnemy(Enemy):
    # constructor which initializes all ghost enemy properties/attributes
    def __init__(self, x, y, health, size, radius, speed, atk):
        super().__init__(x, y, size, size, health, 10, atk, speed)
        self.possibleImages = [['Images/ghostLeft1.png', 'Images/ghostRight1.png'],
                               ['Images/ghostLeft2.png', 'Images/ghostRight2.png']]
        self.radius = radius   # ghost aggro radius
        self.size = size

    # the ghost is never colliding
    def isColliding(self, other):
        return False

    # moves the ghost so that it follows the player
    def move(self, player):
        disX = player.x - self.x
        disY = player.y - self.y
        self.changeImage(disX)
        # moves the ghost if the player is within aggro radius
        distance = math.sqrt((player.x - self.x) ** 2 + (player.y - self.y) ** 2)
        if (distance > self.radius):
            return
        ratio = self.speed / distance
        disX *= ratio
        disY *= ratio
        self.x += disX
        self.y += disY
