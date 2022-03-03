import pygame
import sys
import math
import time
import random

import numpy as np
import torch
from torch.autograd import Variable
from torch import optim


pygame.font.init()

startPos_x = 140
startPos_y = 140

tile_width = 50
tile_height = 50

class Car:
    def __init__(self, carNumber, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.carNumber = carNumber

        self.x = tile_width*self.x1 + startPos_x
        self.y = tile_height*self.y1 + startPos_y
        self.length = abs(x2-x1) + abs(y1-y2) + 1
        self.positionVertical = self.what_position()
        self.image = self.find_image()
        

    def printAttributes(self):
        print('------------------------------------------')
        print('Car number: ' + str(self.carNumber))
        print('start position: (' + str(self.x1) + ", " + str(self.y1) + ") ")
        print('end position: (' + str(self.x2) + ", " + str(self.y2) + ") " )
        print('Length of vehicle:', self.length, 'and is', self.position)
        print('------------------------------------------')

    def what_position(self):
        if self.x1 == self.x2:
            return True
        else:
            return False

    def find_image(self):
        image = None
        if self.length >= 3:
            if random.random() > 0.5:
                image = pygame.image.load('images/truck.png')
            else:
                image = pygame.image.load('images/school-bus.png')
        else:
            if random.random() > 0.5:
                image = pygame.image.load('images/ambulance.png')
            else:
                image = pygame.image.load('images/police-car.png')

        image = pygame.transform.scale(image, (tile_width*self.length,tile_height))

        if self.positionVertical == True:
            if random.random() > 0.5:
                image = pygame.transform.rotate(image, 270)
            else:
                image = pygame.transform.rotate(image, 90)
        else:
            if random.random() > 0.5:
                image = pygame.transform.rotate(image, 180)
        
        return image

        

    def move_options(self):
        if self.positionVertical ==False:
            point1 = (self.x1-1, self.y1)
            point2 = (self.x2+1, self.y2)
            points = []
            points.add(point1)
            points.add(point2)
            return points
        else:
            point1 = (self.x1, self.y1-1)
            point2 = (self.x2+1, self.y2+1)
            points = []
            points.add(point1)
            points.add(point2)
            return points

       
    def moveCar(self, move):
        pass
        # if ()



    def render(self, screen):
        
        screen.blit(self.image, (self.x,self.y))


        













    def rotate_and_center(self, ds, x, y, image, radians):
        degrees = 180/math.pi * radians
        rotated = pygame.transform.rotate(image, -degrees)

        rect = rotated.get_rect()
        ds.blit(rotated, (x - rect.center[0], y - rect.center[1]))


    def rotate_and_centerRect(self, ds, x, y, w, h, radians):
        points = self.pointsToCheck(x, y, w, h, radians)
        pygame.draw.lines(ds, (255,0,255), True, points, 1)

    def drawDistanceToCollision(self, ds, x, y, points, radians):
        for i in range(len(points)):
            pygame.draw.line(ds, (0,255,100), points[i], (x, y), 1)


    
        