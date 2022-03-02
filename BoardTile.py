import pygame
import sys
import math


class BoardTile:
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image





    def render(self, screen):

        # print(self.x, self.y)

        screen.blit(self.image, (self.x,self.y))
