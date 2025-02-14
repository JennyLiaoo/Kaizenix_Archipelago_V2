"""
Author: Jenny Liao
AndrewID: jliao2,
Section: 1A

Citations:
The image of the enemy is from: https://lionheart963.itch.io/wizard
"""
from Enemy import Enemy
import heapq
from cmu_graphics import *

# The path enemy uses pathfinding to navigate around obstacles and move towards the player
class PathEnemy(Enemy):
    # constructor which initializes all path enemy properties/attributes
    def __init__(self, x, y, health, speed, atk, size):
        super().__init__(x, y, size, size, health, 10, atk, speed)
        self.possibleImages = [['Images/wizLeft1.png', 'Images/wizRight1.png'],
                               ['Images/wizLeft2.png', 'Images/wizRight2.png']]
        self.size = size

    """This is an implementation of the A* pathfinding algorithm.
    I made this function with the help of the following resources:
     - https://www.youtube.com/watch?v=NTTTjQDfmyA
     - https://www.youtube.com/watch?v=Hd0D68guFKg
     - https://www.youtube.com/watch?v=2JNEme00ZFA
     - https: // www.youtube.com / watch?v = wGSQ486Y4sc
     - https://www.youtube.com/watch?v=EcTWha6JHvE
     - I used ChatGPT to help me better understand heapq, the A* algorithm, identify mistakes, and provide suggestions
    """
    def findPath(self, player, obstacles):
        # Initialize the starting position and goal
        start = (self.x, self.y)
        goal = (player.x, player.y)

        # a priority queue storing positions to evaluate
        openSet = []
        # each element int the heapq is stored as a tuple in the form (fScore, position)
        # where fScore is the estimated cost of reaching the goal from the given position
        heapq.heappush(openSet, (0, start))

        cameFrom = {}  # a dictionary that maps each position to where you came from and how you got here
        gScore = {start: 0}  # a dictionary that tracks the cost from the starting point to each position
        fScore = {start: self.heuristic(start[0], start[1], player)}  # tracks estimated cost from starting point to pos

        # while there are still positions to explore, keep looping
        while openSet:
            placeholder, current = heapq.heappop(openSet)  # We retrieve the position with the lowest fScore

            # If the current position collides with the player, we have found a path! YAY!
            if self.isColliding(player, current[0], current[1]):
                return self.reconstructPath(cameFrom, current)

            # Move up, down, left, right to explore all possible moves
            for move in [(0, self.speed), (self.speed, 0), (-self.speed, 0), (0, -self.speed)]:
                nextPos = (current[0] + move[0], current[1] + move[1])

                # if the path enemy collides with an obstacle, it is not a valid move
                if not self.canMove(nextPos[0], nextPos[1], obstacles):
                    continue

                newGScore = gScore[current] + 1

                # If nextPos is unvisited or the path is less costly than the other paths we have found, we put this one
                if nextPos not in gScore or newGScore < gScore[nextPos]:
                    # we calculate our new costs for the path
                    gScore[nextPos] = newGScore
                    fScore[nextPos] = newGScore + self.heuristic(nextPos[0], nextPos[1], player)
                    heapq.heappush(openSet, (fScore[nextPos], nextPos))
                    cameFrom[nextPos] = (current, move)  # Record how we got here

        return None  # returns None if no possible paths to the player is found

    # This function helps us estimate how far the currentPos is from the PlayerPos
    def heuristic(self, x, y, player):
        return abs(x - player.x) + abs(y - player.y)

    # This function rebuilds the path using the cameFrom dictionary (which kept track of how we reached each position)
    def reconstructPath(self, cameFrom, current):
        path = []
        while current in cameFrom:
            current, move = cameFrom[current]
            path.append(move)
        return path[::-1]  # Reverse the path to get it in the right order (start to goal)

    # verifies that the enemy is not hitting any obstacles (a.k.a the legality check in backtracking)
    def canMove(self, x, y, obstacles):
        for obs in obstacles:
            if (self.checkHittingObstacle(x, y, obs)):
                return False
        return True

    # checks if the enemy and obstacle are touching
    def checkHittingObstacle(self, x, y, other):
        if (x + self.size >= other.x and x <= other.x + other.w and
                other.y + other.h - 5 <= y <= other.y + other.h + 5):
            return True
        elif (y + self.size >= other.y and y <= other.y + other.h and
              other.x + 5 >= x + self.size >= other.x - 5):
            return True
        elif (x + self.size >= other.x and x <= other.x + other.w and
              other.y - 5 <= y + self.size <= other.y + 5):
            return True
        elif (y + self.size >= other.y and y <= other.y + other.h and
              other.x + other.w + 5 >= x >= other.x + other.w - 5):
            return True
        return False

    # checks if the enemy and obstacle are overlapping
    def isColliding(self, player, x, y):
        x1, y1, x2, y2 = x, y, x + self.size, y + self.size
        x3, y3, x4, y4 = player.x, player.y, player.x + player.size, player.y + player.size
        if (x2 <= x3 or x4 <= x1):
            return False
        if (y2 <= y3 or y4 <= y1):
            return False
        return True

    # if we found a solution through our pathfinding algorithm, we move in the solution's direction
    def move(self, player, obstacles):
        solution = self.findPath(player, obstacles)
        if solution:                        # Check if a valid path was found
            movingDirection = solution[0]   # Take the first move in the solution, and move
            self.x += movingDirection[0]
            self.y += movingDirection[1]
            self.changeImage(movingDirection[0])
