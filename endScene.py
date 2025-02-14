"""
Author: Jenny Liao
AndrewID: jliao2,
Section: 1A

Citations:
The image of the background is from: https://uk.pinterest.com/pin/790311434638752786/
and from: https://ar.pinterest.com/pin/171136854584452700/
"""
from Scene import Scene
from cmu_graphics import *

# this class holds all the information of the end scene (both win or lose)
class endScene(Scene):
    def __init__(self, x, y, player):
        super().__init__(x, y,700,500, player,0)
        self.backgroundWin = 'Images/GameWin.png'
        self.backgroundLose = 'Images/GameLose.png'
        self.currentBackground = self.backgroundLose
        self.status = None      # game status
        self.opacity = 30

    # changes the game status to win or lose
    def setStatus(self, winOrLose):
        self.status = winOrLose
        if(winOrLose == 'win'):
            self.currentBackground = self.backgroundWin
        else:
            self.currentBackground = self.backgroundLose

    # checks if the player has clicked the restart button
    def clickRestart(self, mouseX, mouseY):
        if (mouseX >= self.x+self.w/2-75 and mouseX <= self.x+self.w/2+75 and mouseY >= self.y+self.h/2+65 and mouseY <= self.y+self.h/2+70+25):
            return True
        return False

    # changes the button opacity based on mouse hover location
    def updateButton(self,mouseX, mouseY):
        if (mouseX >= self.x + self.w / 2 - 75 and mouseX <= self.x + self.w / 2 + 75 and mouseY >= self.y + self.h / 2 + 65 and mouseY <= self.y + self.h / 2 + 70 + 25):
            self.opacity = 50
        else:
            self.opacity = 30

    # this scene has no upper layer
    def drawUpper(self):
        pass

    # draws the background scene
    def redrawAll(self):
        drawImage(self.currentBackground, self.x,self.y, width=self.w,height=self.h)
        if(self.status == 'win'):
            drawLabel('YOU WIN', self.x+self.w/2,self.y+self.h/2-50,size = 50, font = 'Verdana', fill = 'red', bold=True)
        else:
            drawLabel('YOU LOSE', self.x+self.w/2,self.y+self.h/2-50,size = 50, font = 'Verdana', fill = 'white', bold=True)
            drawLabel('Unfortunately, you got lost deep inside the archipelago and could not find your way out',
                      self.x+self.w/2,self.y+self.h/2,size = 14, font = 'Verdana', fill = 'white')
        # restart button
        drawRect(self.x+self.w/2,self.y+self.h/2+70, 150, 50, fill='white', opacity=self.opacity, borderWidth=2,
                 border='white', align='center')
        drawLabel("Return", self.x+self.w/2,self.y+self.h/2+70, size=15, fill='white', align='center',
                  font='Verdana', borderWidth=0.5, border='white', bold = True)