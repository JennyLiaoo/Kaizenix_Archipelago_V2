"""
Author: Jenny Liao
AndrewID: jliao2,
Section: 1A
"""
from CrossEnemy import CrossEnemy
from FollowerEnemy import FollowerEnemy
from LineEnemy import LineEnemy
from PathEnemy import PathEnemy
from cmu_graphics import *
from GhostEnemy import GhostEnemy
import random


# spawns enemy randomly based on scene level
class EnemySpawner:
    def __init__(self):
        self.lvl = 0

    # update scene level
    def setLevel(self,lvl):
        self.lvl = lvl

    # spawns all the enemies randomly based on scene level
    def spawnEnemy(self, currentNumEnemies, spawnLocations):
        maxNumEnemies = 1
        if(self.lvl == 1):
           maxNumEnemies = 8
        elif(self.lvl == 2):
            maxNumEnemies = 6
        elif(self.lvl == 3):
            maxNumEnemies = 8
        if (currentNumEnemies >= maxNumEnemies):
            return
        enemyGenerated = random.randint(1, 2000)

        # can have line or cross enemies
        if (self.lvl == 1):
            if(enemyGenerated <= 8):
                typeEnemy = random.randint(1, 2)
                location = random.randint(0, len(spawnLocations) - 1)
                if(typeEnemy == 1):
                    return LineEnemy(spawnLocations[location][0], spawnLocations[location][1],
                                     random.randint(30, 40), 'x', random.randint(1, 3),
                                     random.randint(10, 20), 35)
                elif(typeEnemy == 2):
                    return CrossEnemy(spawnLocations[location][0], spawnLocations[location][1],
                                      random.randint(40, 50), 'y', random.randint(2, 3),
                                    35, random.randint(15, 20))

        # can have line, cross, follower enemies
        elif(self.lvl==2):
            if(enemyGenerated <= 10):
                typeEnemy = random.randint(1, 3)
                location = random.randint(0, len(spawnLocations) - 1)
                if (typeEnemy == 1):
                    return LineEnemy(spawnLocations[location][0], spawnLocations[location][1],
                                     random.randint(80, 100),'x', random.randint(2, 3),
                                     random.randint(20, 30), 35)
                elif (typeEnemy == 2):
                    return CrossEnemy(spawnLocations[location][0], spawnLocations[location][1],
                                      random.randint(90, 100),'y', 3, 35,
                                      random.randint(25, 35))
                elif (typeEnemy == 3):
                    return FollowerEnemy(spawnLocations[location][0], spawnLocations[location][1],
                                         random.randint(100, 120), 35, random.randint(200, 300),
                                         random.randint(2, 3),  random.randint(20, 30))

        # can have line, cross, follower, ghost enemies
        elif (self.lvl == 3):
            if (enemyGenerated <= 12):
                typeEnemy = 4
                location = random.randint(0, len(spawnLocations) - 1)
                if (typeEnemy == 1):
                    return LineEnemy(spawnLocations[location][0], spawnLocations[location][1],
                                     random.randint(150, 200),'x', random.randint(2, 3),
                                     random.randint(20, 30), 35)
                elif (typeEnemy == 2):
                    return CrossEnemy(spawnLocations[location][0], spawnLocations[location][1],
                                      random.randint(180, 200),'y', 3, 35,
                                      random.randint(30, 40))
                elif (typeEnemy == 3):
                    return FollowerEnemy(spawnLocations[location][0], spawnLocations[location][1],
                                         random.randint(100, 120), 35, random.randint(250, 350),
                                         3, random.randint(30, 35))
                else:
                    return GhostEnemy(spawnLocations[location][0], spawnLocations[location][1],
                                         random.randint(100, 120), 35, random.randint(250, 350),
                                      3, random.randint(30, 35))

        # can have path finding enemies
        elif(self.lvl == 4):
            if (enemyGenerated <= 5):
                location = random.randint(0, len(spawnLocations) - 1)
                return PathEnemy(spawnLocations[location][0], spawnLocations[location][1],
                                 random.randint(300, 350), 3,
                                 random.randint(30, 50), 90)
