import BoardTile
import Car
import time
import pygame

board_tiles = []
car_manager = []
player_list = []


tile_width = 50
tile_height = 50

startPos_x = 140
startPos_y = 140



tile_finish_left = pygame.image.load('images/track_tile_finishline.jpg')
tile_finish_left = pygame.transform.scale(tile_finish_left, (50, 50))

tile_finish_right = pygame.image.load('images/track_tile_finishline.jpg')
tile_finish_right = pygame.transform.rotate(tile_finish_right, 180)
tile_finish_right = pygame.transform.scale(tile_finish_right, (50, 50))

tile_regular = pygame.image.load('images/track_tile.jpg')
tile_regular = pygame.transform.scale(tile_regular, (50, 50))

def set_carlist(car_list):
    for car in car_list:
        car_manager.append(car)

def set_players(players):
    for p in players:
        player_list.append(p)

    
        

def generate_board(board):
    row, col = board.shape
    for i in range(row):
        for j in range(col):
            pos_x = j*tile_width + startPos_x
            pos_y = i*tile_height + startPos_y

            if board[i][j] == 'W-1':
                tile_image = tile_finish_left
            elif board[i][j] == 'W1':
                tile_image = tile_finish_right
            else:
                tile_image = tile_regular

            board_tiles.append(BoardTile.BoardTile(pos_x, pos_y, tile_width, tile_height, tile_image))



def render(screen):
    for entity in board_tiles:
        entity.render(screen)

    # print(car_manager)
    # print()
    for entity in car_manager:
        entity.render(screen)
            # print(entity.image)

    for entity in player_list:
        entity.render(screen)
    



