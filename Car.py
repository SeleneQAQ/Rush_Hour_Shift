import pygame
import sys
import math
import time
import random

import numpy as np
import init_game


pygame.font.init()

startPos_x = 140
startPos_y = 140

tile_width = 50
tile_height = 50

class Car:
    def __init__(self, number, x1, y1, x2, y2, finishline=None):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.number = number

        if number == 1:
            self.turn = True  #whos turn is it now
        else: 
            self.turn = False

        self.x = tile_width*self.x1 + startPos_x
        self.y = tile_height*self.y1 + startPos_y
        self.length = abs(x2-x1) + abs(y1-y2) + 1
        self.positionVertical = self.what_position()
        self.image = self.find_image()
        self.finishline = finishline
        

    def printAttributes(self):
        print('------------------------------------------')
        print('Car number: ' + str(self.number))
        print('start position: (' + str(self.x1) + ", " + str(self.y1) + ") ")
        print('end position: (' + str(self.x2) + ", " + str(self.y2) + ") " )
        print('Length of vehicle:', self.length, 'and is', self.positionVertical)
        print('Finishline is tile with string', self.finishline)
        print('------------------------------------------')


    def what_position(self):
        if self.x1 == self.x2:
            return True
        else:
            return False


    def move_options(self, game_board):

        # we need to do this instead of using the self.x1 etc because
        #  that won't work when going deep into the tree
        car_pos = init_game.find_car_from_board(game_board, self.number)

        if (self.positionVertical == True):
            point1 = (car_pos.x1, car_pos.y1-1)
            point2 = (car_pos.x2, car_pos.y2+1)
        else: 
            point1 = (car_pos.x1-1, car_pos.y1)
            point2 = (car_pos.x2+1, car_pos.y2)

        points = []
        points.append(point1)
        points.append(point2)

        return points

    def find_image(self):
        image = None
        if self.number == 1 or self.number == -1:
            if self.number == 1:            
                image = pygame.image.load('images/red-car.png')
            else:
                image = pygame.image.load('images/yellow-car.png')

            image = pygame.transform.scale(image, (tile_width*self.length,tile_height))

            if self.number == -1:
                image = pygame.transform.rotate(image, 180)
        
            return image



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

       
    def update(self, new_car):
        self.x1 = new_car.x1
        self.y1 = new_car.y1
        self.x2 = new_car.x2
        self.y2 = new_car.y2

        self.x = tile_width*new_car.x1 + startPos_x
        self.y = tile_height*new_car.y1 + startPos_y
        


    def render(self, screen):
        screen.blit(self.image, (self.x,self.y))

        myfont = pygame.font.SysFont('Arial', 30)
        textsurface = myfont.render(f'{self.number}', False, (255, 255, 255))
        screen.blit(textsurface, (self.x+5,self.y+5))

        