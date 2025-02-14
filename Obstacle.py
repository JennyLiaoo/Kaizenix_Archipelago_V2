"""
Author: Jenny Liao
AndrewID: jliao2,
Section: 1A
"""
from cmu_graphics import *

# just an old rectanguale obstacle
class Obstacle:

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    # used to update position relative to the scene position
    def add(self, x, y):
        self.x += x
        self.y += y



