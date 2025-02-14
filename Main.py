"""
Author: Jenny Liao
AndrewID: jliao2,
Section: 1A

Some General Citations for the overall project (specific citations are placed with the code that uses it):
The sprites used to create all scene backgrounds were taken from: https://cainos.itch.io/pixel-art-top-down-basic
The sprites were put together to make tilemaps using Unity: https://unity.com/
Game Music is 'Adventure' by Alexander Nakarada: https://www.chosic.com/download-audio/28027/
The ideas for this game were inspired by the following:
- https://www.youtube.com/watch?v=om59cwR7psI
- https://www.youtube.com/watch?v=QU1pPzEGrqw
- My own past projects: https://github.com/JennyLiaoo
Also, the game name is inspired by a story arc from Omniscient Reader's Viewpoint.
"""

# Import the necessary modules and classes
from cmu_graphics import *
from Player import Player
# importing all scenes and screens
from StartScreen import StartScreen
from Scene1 import Scene1
from Scene2 import Scene2
from Scene3 import Scene3
from Scene4 import Scene4
from Scene5 import Scene5
from Scene6 import Scene6
from endScene import endScene
# imports needed for the music
import os
import pygame


# Function which initializes all application variables when the app starts
def onAppStart(app):
    resetApp(app)


# Resets the game state to its initial state
def resetApp(app):
    # Creates the player who is always centred on the screen
    app.player = Player(app.width / 2 - 25, app.height / 2 - 25)

    # initializes all the scenes and screens with their starting positions
    app.startScreen = StartScreen(app.width // 2 - 5, app.height // 2, app.width + 110, app.height)
    app.scene1 = Scene1(530, 260, app.player)
    app.scene2 = Scene2(460, 530, app.player)
    app.scene3 = Scene3(0, 0, app.player)
    app.scene4 = Scene4(0, 0, app.player)
    app.scene5 = Scene5(0, 0, app.player)
    app.scene6 = Scene6(0, 0, app.player)
    app.endScene = endScene(0, 0, app.player)
    app.scenes = [app.scene1, app.scene2, app.scene3, app.scene4, app.scene5, app.scene6]

    # set the current scene to the first scene, and establish the initial game states
    app.scene = app.scene1
    app.gameStart = False
    app.gameEnd = False

    # Load and play background music
    # Citation: https://www.youtube.com/watch?v=3Yhhzflmxfs
    file = os.path.join('Sounds', 'Adventure.mp3')
    pygame.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)


# Continuously redraws the game screen based on the current game state
def redrawAll(app):
    # if the game is over, all draw the end screen
    if (app.gameEnd):
        app.endScene.redrawAll()
    # if the game hasn't started, only draw the start screen
    elif (app.gameStart == False):
        app.startScreen.redrawAll()
    # This is only drawn if the player is in the game
    elif (app.gameStart and app.gameEnd == False):
        app.scene.redrawAll()
        app.player.redrawAll()
        app.scene.drawUpper()
        drawLabel('Level: ' + str(app.player.lvl), 630, 460, size=30, font='arial', bold=True, fill='white',
                  align='center')
        drawLabel('Exp: ' + str(app.player.exp), 630, 485, size=15, font='arial', bold=True, fill='white',
                  align='center')


# Handles each step of the game logic
def onStep(app):
    # only does something if the game is
    if (app.gameStart and app.gameEnd == False):
        # updates everything that needs to be updated
        app.scene.updatePlayer(app.player)
        checkAllStatueRestorationStatus(app)
        checkPlayerCollisionWithObstacles(app)

        # checks if the player has lost the game
        if (app.scene.player.health <= 0):
            app.endScene.setStatus('lose')
            app.scene = app.endScene
            app.gameEnd = True

        # checks if the player satisfies the condition to win the game
        if (type(app.scene) == Scene1 and app.scene.gameWin and
            500 <= app.scene.x <= 560 and 245 <= app.scene.y <= 275):
            app.player.teleportCounter += 1  # To teleport, the player must stand on the portal for a couple of seconds
            if (app.player.teleportCounter >= app.player.teleportTime):
                app.endScene.setStatus('win')
                app.scene = app.endScene
                app.gameEnd = True


# checks if the scene needs to be changed depending on the player position
def checkSceneChange(app):
    oldScene = app.scene
    oldX, oldY = app.scene.x, app.scene.y
    if (type(app.scene) == Scene1 and app.scene.y <= -190 and 500 <= app.scene.x <= 560 and app.player.lvl >= 4):
        app.scene = app.scene5
        if (app.scene.lastPos == None):
            app.scene.setPos(330, 220)
        else:
            app.scene.restoreScenePos()
    elif (type(app.scene) == Scene1 and app.scene.y > 720 and app.player.lvl >= 1):
        app.scene = app.scene2
        if (app.scene.lastPos == None):
            app.scene.setPos(280, -160)
        else:
            app.scene.restoreScenePos()
    elif (type(app.scene) == Scene1 and app.scene.x <= 0 and app.scene.y <= -140 and app.player.lvl >= 3):
        app.scene = app.scene4
        if (app.scene.lastPos == None):
            app.scene.setPos(340, 370)
        else:
            app.scene.restoreScenePos()
    elif (type(app.scene) == Scene2 and app.scene.x <= -230 and app.player.lvl >= 2):
        app.scene = app.scene3
        if (app.scene.lastPos == None):
            app.scene.setPos(930, 340)
        else:
            app.scene.restoreScenePos()
    elif (type(app.scene) == Scene2 and app.scene.y < -160 and 220 <= app.scene.x <= 340):
        app.scene = app.scene1
        if (app.scene.lastPos == None):
            app.scene.setPos(-100, 720)
        else:
            app.scene.restoreScenePos()
    elif (type(app.scene) == Scene3 and app.scene.x >= 940):
        app.scene = app.scene2
        if (app.scene.lastPos == None):
            app.scene.setPos(-220, -80)
        else:
            app.scene.restoreScenePos()
    elif (type(app.scene) == Scene4 and 370 <= app.scene.y):
        app.scene = app.scene1
        if (app.scene.lastPos == None):
            app.scene.setPos(100, -90)
        else:
            app.scene.restoreScenePos()
    elif (type(app.scene) == Scene5 and app.scene.x <= 340 and app.scene.x > 320 and 240 > app.scene.y > 220):
        app.scene = app.scene1
        if (app.scene.lastPos == None):
            app.scene.setPos(530, -190)
        else:
            app.scene.restoreScenePos()
    elif (type(app.scene) == Scene5 and app.scene.x <= -260 and app.player.lvl >= 5):
        app.scene = app.scene6
        if (app.scene.lastPos == None):
            app.scene.setPos(530, -350)
        else:
            app.scene.restoreScenePos()
    elif (type(app.scene) == Scene6 and app.scene.x >= 530 and app.scene.y <= -240):
        app.scene = app.scene5
        if (app.scene.lastPos == None):
            app.scene.setPos(-170, 370)
        else:
            app.scene.restoreScenePos()
    # stores the previous position, so we can restore the original position later
    if (app.scene != oldScene):
        oldScene.setLastPos(oldX, oldY)


# Undoes the player's movement if it causes them to collide with an obstacle
def checkPlayerCollisionWithObstacles(app):
    for obs in app.scene.obstacles:
        collide = app.player.checkCollisions(obs)  # returns which direction the player collided from
        if (collide == 'bottom'):
            app.scene.add(0, -app.player.speed)
        elif (collide == 'left'):
            app.scene.add(app.player.speed, 0)
        elif (collide == 'top'):
            app.scene.add(0, app.player.speed)
        elif (collide == 'right'):
            app.scene.add(-app.player.speed, 0)


# Checks the restoration status of all statues across all scenes
def checkAllStatueRestorationStatus(app):
    completedStatues = []
    for scene in app.scenes:
        for statue in scene.statues:
            if (statue.completed):
                completedStatues.append(statue.id % 7)  # ensures that the id added remains the same after game restart
    app.scene1.drawGlow(completedStatues)  # Given a restored statue, a pillar representing that statue will light up


# Handles mouse click events
def onMousePress(app, mouseX, mouseY):
    # restarts the game if the 'restart' button is clicked
    if (app.gameEnd):
        if (app.endScene.clickRestart(mouseX, mouseY)):
            resetApp(app)
    # starts the game if the 'start' button is clicked
    if (app.gameStart == False and app.gameEnd == False):
        app.startScreen.checkClick(mouseX, mouseY)
        if (app.startScreen.gameStart):
            app.gameStart = True


# Handles mouse movement events
def onMouseMove(app, mouseX, mouseY):
    # changes the button opacity if the mouse is hovering over the button
    if (app.gameEnd):
        app.endScene.updateButton(mouseX, mouseY)
    if (app.gameStart == False and app.gameEnd == False):
        app.startScreen.onMouseMove(mouseX, mouseY)


# Handles events where multiple keys are held for player movement
def onKeyHold(app, keys):
    # only moves if the game is ongoing
    if (app.gameStart and app.gameEnd == False):
        if ('down' in keys):
            app.scene.add(0, -app.player.speed)
            app.player.changeImage(1)
            app.player.direction = 'front'
        if ('up' in keys):
            app.scene.add(0, app.player.speed)
            app.player.changeImage(0)
            app.player.direction = 'back'
        if ('left' in keys):
            app.scene.add(app.player.speed, 0)
            app.player.changeImage(2)
            app.player.direction = 'left'
        if ('right' in keys):
            app.scene.add(-app.player.speed, 0)
            app.player.changeImage(3)
            app.player.direction = 'right'
        checkSceneChange(app)  # we check for scene changes in case the player has moved to another scene


# handles key press events
def onKeyPress(app, key):
    # If we are still on the start screen...
    if (app.gameStart == False and app.gameEnd == False):
        app.startScreen.onKeyPress(key)
    # If we are in game, click the space bar to attack!
    elif (app.gameStart and app.gameEnd == False):
        if (key == 'space' and app.player.cooldown == False):  # we cannot attack when in attack cooldown
            app.player.hitAnimation(app.scene.enemies)


# runs the app
def main():
    runApp(width=700, height=500)


# starts the game
main()
