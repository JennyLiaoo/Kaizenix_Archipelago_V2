"""
Author: Jenny Liao
AndrewID: jliao2,
Section: 1A

Citations:
See image citations through Main.py
"""
from EnemySpawner import EnemySpawner
from GhostEnemy import GhostEnemy
from FollowerEnemy import FollowerEnemy
from PathEnemy import PathEnemy
from cmu_graphics import *

# a superclass for all scenes, depicting their attributes and behaviors
class Scene:
    def __init__(self, x, y, w, h, player,lvl):
        # enemy spawning variables
        self.spawner = EnemySpawner()
        self.spawner.setLevel(lvl)
        self.spawnLocations = []

        # establishing scene basics
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.w2 = self.w
        self.h2 = self.h
        self.background = 'Images/scene1.png'
        self.bgUpper = 'Images/scene1Upper.png'

        # keeping track of scenes last position before switching so we can restore that position
        self.lastPos = None

        # establishing scene entities
        self.player = player
        self.obstacles = []
        self.enemies = []
        self.statues = []

    # checks player collisions with the scene's enemies
    def playerCollision(self, enemies):
        if(self.player.immune == False):
            for enemy in enemies:
                if(self.player.isColliding(enemy) == True):
                    self.player.health -= enemy.atk     # deplete player health
                    self.player.immune = True

    # spawn new enemies
    def spawnEnemies(self, currentNumEnemies, spawnLocations):
        newEnemy = self.spawner.spawnEnemy(currentNumEnemies,spawnLocations)   # we might spawn an enemy
        if(newEnemy != None):       # if an enemy is given, it is our new enemy
            self.enemies.append(newEnemy)

    # used so we can restore the last scene's position after switching back from a different scene
    def setLastPos(self, x, y):
        self.lastPos = (x, y)

    # restore the scene's previous position
    def restoreScenePos(self):
        self.x, self.y = self.lastPos

    # update the player
    def updatePlayer(self, player):
        self.player = player

    # sets the scene's position
    def setPos(self, x, y):
        self.x = x
        self.y = y

    # updates the scene's and its entities' positions when the player 'moves'
    def add(self, xAdd, yAdd):
        self.x += xAdd
        self.y += yAdd
        for obs in self.obstacles:
            obs.add(xAdd, yAdd)
        for enemy in self.enemies:
            enemy.add(xAdd, yAdd)
        for statue in self.statues:
            statue.add(xAdd, yAdd)
        newSpawnLocation = []
        for spawn in self.spawnLocations:
            newSpawnLocation.append((spawn[0]+xAdd, spawn[1]+yAdd))
        self.spawnLocations = newSpawnLocation


    # draws all the enemies
    def drawEnemies(self):
        i = 0
        while(i < len(self.enemies)):
            if(self.enemies[i].health <=0):     # checks if the enemy is dead, and add to player exp
                self.player.exp += self.enemies[i].exp
                self.enemies.remove(self.enemies[i])
            else:
                self.enemies[i].redrawAll()
                i+=1

    # checks if we can move an enemy
    def checkMoveEnemy(self):
        for enemy in self.enemies:
            for obs in self.obstacles:
                if(enemy.checkMove(obs)):
                    break
            self.moveEnemies(enemy)

    # actually moves the enemy
    def moveEnemies(self, enemy):
        if(type(enemy) == FollowerEnemy or type(enemy) == GhostEnemy):
            enemy.move(self.player)
        elif(type(enemy)==PathEnemy):
            enemy.move(self.player,self.obstacles)
        else:
            enemy.move()


    # draws the upper layer of the background
    def drawUpper(self):
        drawImage(self.bgUpper, self.x,self.y, width=self.w,height=self.h,align = 'center')

    # draws the background (lower layer)
    def redrawAll(self):
        drawRect(self.x - self.w / 2 - 300, self.y - self.h / 2 - 300, self.w + 600, self.h + 600, fill='black')
        drawImage(self.background, self.x, self.y, width=self.w, height=self.h, align='center')
        self.y2 = self.y + self.h
        self.checkMoveEnemy()                                       # check if the enemies can move
        self.drawEnemies()
        self.spawnEnemies(len(self.enemies), self.spawnLocations)   # spawn new enemies




