
import pygame
import random


startPos_x = 140
startPos_y = 140

tile_width = 50
tile_height = 50



class Player(object):
    def __init__(self, player, x1, y1, x2, y2, finishline):
        self.player = player
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x = tile_width*self.x1 + startPos_x
        self.y = tile_height*self.y1 + startPos_y
        self.length = abs(x2-x1) + abs(y1-y2) + 1
        self.position = 'Horizontal'
        self.image = self.find_image()
        self.finishline = finishline

    
    def printAttributes(self):
        print('------------------------------------------')
        print('PLayer number: ' + str(self.player))
        print('start position: (' + str(self.x1) + ", " + str(self.y1) + ") ")
        print('end position: (' + str(self.x2) + ", " + str(self.y2) + ") " )
        print('Length of vehicle:', self.length)
        print('Finishline is tile with string', self.finishline)
        print('------------------------------------------')


    def find_image(self):
        image = None
        if self.player == 1:            
            image = pygame.image.load('images/red-car.png')
        else:
            image = pygame.image.load('images/yellow-car.png')


        image = pygame.transform.scale(image, (tile_width*self.length,tile_height))

        if self.player == -1:
            image = pygame.transform.rotate(image, 180)
        
        return image
        
   

    def render(self, screen):
        screen.blit(self.image, (self.x,self.y))




