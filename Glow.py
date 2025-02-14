"""
Author: Jenny Liao
AndrewID: jliao2,
Section: 1A

Citations:
See Main.py for glow sprite citations
"""
from cmu_graphics import *

# it just glows! (when a statue is restored, a glow is drawn)
class Glow:
    def __init__(self, x, y,w,h, image):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image = image
        self.drawn = False

    # used to update glow position relative to scene position
    def add(self, xAdd, yAdd):
        self.x += xAdd
        self.y += yAdd

    # draws the glow if statue has been restored
    def redrawAll(self):
        if(self.drawn):
            drawImage(self.image,self.x,self.y, width = self.w, height = self.h)
