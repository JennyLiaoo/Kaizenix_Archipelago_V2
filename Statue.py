"""
Author: Jenny Liao
AndrewID: jliao2,
Section: 1A

"""
import math
from cmu_graphics import *


# keeps track of statue id, its restoration range, and its charge
class Statue:
    id = 0

    def __init__(self, x, y, charge, range):
        self.range = range
        self.x = x
        self.y = y
        self.totalCharge = charge
        self.charge = 0  # current statue charge
        self.completed = False  # fully restored status
        self.id = Statue.id
        Statue.id += 1


    # checks if the statue is being charged
    def chargeStatue(self, player, enemies):
        if (self.completed and player.health >= player.totalHealth):
            return
        centerX = player.x + player.size / 2
        centerY = player.y + player.size / 2
        # can only heal if the statue is completed, the player is nearby, and no violence is occurring
        if (self.completed and distance(centerX, centerY, self.x, self.y) <= self.range and
                player.health < player.totalHealth and player.immune == False and player.cooldown == False):
            for enemy in enemies:
                if (distance(enemy.x + enemy.w / 2, enemy.y + enemy.h / 2, self.x, self.y) < self.range):
                    return
            player.health += 0.2
            return
        # can only restore if the player is nearby, and no violence is occurring
        elif (distance(centerX, centerY, self.x,
                       self.y) <= self.range and player.immune == False and player.cooldown == False):
            for enemy in enemies:
                if (distance(enemy.x + enemy.w / 2, enemy.y + enemy.h / 2, self.x, self.y) < self.range):
                    return
            self.charge += 1
        # update its completion
        if (self.charge >= self.totalCharge):
            self.completed = True


    # calculates the distance between the player and the statue
    def distance(self, x1, y1, x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    # update statue position relative to scene position
    def add(self, xAdd, yAdd):
        self.x += xAdd
        self.y += yAdd

    # draws the statue and its restoration progress
    def redrawAll(self, x, y):
        drawRect(self.x - x, self.y - y, self.range, 10, fill='red')
        bar = self.range * self.charge // self.totalCharge
        if (int(bar) > 0):
            drawRect(self.x - x, self.y - y, int(bar), 10, fill='green')
