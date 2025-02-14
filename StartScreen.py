"""
Author: Jenny Liao
AndrewID: jliao2,
Section: 1A

Citations:
Instructions made using PowerPoint
See background image citation in Main.py
"""
from cmu_graphics import *


# this class holds all the information of the start screen
class StartScreen:
    def __init__(self, x, y, w, h):
        self.background = 'Images/mainScreen.png'
        self.gameplayTutorial = ['Images/instructions1.png', 'Images/instructions2.png', 'Images/instructions3.png',
                                 'Images/instructions4.png', 'Images/instructions5.png', 'Images/instructions6.png',
                                 'Images/instructions7.png']
        self.tutorialCounter = 0  # tracks which tutorial slide we are currently on
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.displayingInstructions = False
        self.gameStart = False
        self.buttonOpacity1 = 30
        self.buttonOpacity2 = 30

    # draws the start screen
    def redrawAll(self):
        drawImage(self.background, self.x, self.y, width=self.w, height=self.h, align='center')
        drawLabel("Kaizenix Archipelago", self.x + 10, self.y - 60, size=50, fill='white', opacity=40, align='center',
                  font='Verdana', bold=True, border='white', borderWidth=2)
        drawRect(self.x, self.y + 40, 150, 50, fill='white', opacity=self.buttonOpacity1, borderWidth=2,
                 border='white', align='center')
        drawRect(self.x, self.y + 120, 150, 50, fill='white', opacity=self.buttonOpacity2, borderWidth=2,
                 border='white', align='center')
        drawLabel("Instructions", self.x, self.y + 40, size=15, fill='white', align='center',
                  font='Verdana', borderWidth=0.5, border='white')
        drawLabel("Start", self.x, self.y + 120, size=15, fill='white', align='center',
                  font='Verdana', borderWidth=0.5, border='white')
        self.drawInstructions()

    # checks if the user has clicked on the instructions or start button
    def checkClick(self, mouseX, mouseY):
        if (mouseX >= self.x - 75 and mouseX <= self.x + 75 and mouseY >= self.y + 15 and mouseY <= self.y + 65):
            self.displayingInstructions = True
        elif (mouseX >= self.x - 75 and mouseX <= self.x + 75 and mouseY >= self.y + 95 and mouseY <= self.y + 145):
            self.gameStart = True

    # updates button opacity for mouse hovers
    def onMouseMove(self, mouseX, mouseY):
        if (mouseX >= self.x - 75 and mouseX <= self.x + 75 and mouseY >= self.y + 15 and mouseY <= self.y + 65):
            self.buttonOpacity1 = 50
        else:
            self.buttonOpacity1 = 30
        if (mouseX >= self.x - 75 and mouseX <= self.x + 75 and mouseY >= self.y + 95 and mouseY <= self.y + 145):
            self.buttonOpacity2 = 50
        else:
            self.buttonOpacity2 = 30

    # changes instruction slide based on arrow presses
    def onKeyPress(self, key):
        if (self.displayingInstructions and key == 'right'):
            self.tutorialCounter += 1
        elif (self.displayingInstructions and key == 'left'):
            self.tutorialCounter -= 1
        if (self.tutorialCounter > len(self.gameplayTutorial) - 1 or self.tutorialCounter < 0):
            self.tutorialCounter = 0
            self.displayingInstructions = False

    # draws the current instruction
    def drawInstructions(self):
        if (self.displayingInstructions):
            drawImage(self.gameplayTutorial[self.tutorialCounter], self.x, self.y, width=self.w + 140,
                      height=self.h + 40, align='center')
            drawLabel("<-- Click the left arrow to go back. Click the right arrow to continue. -->", self.x,
                      self.y + 200, size=15, fill='black', align='center')
