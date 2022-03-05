import BoardTile
import Car
import time
import pygame
import GameAi

board_tiles = []
car_list = []
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

def set_carlist(generated_cars):
    for car in generated_cars:
        car_list.append(car)
    

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



def update(game_board):
    # print(game_board)

    curr_player = GameAi.check_player_turn(player_list)
    print(f'It is {curr_player.number} turn')


    GameAi.update_board(game_board, curr_player, car_list)

    # change whose turn it is
    for player in player_list:
        player.turn = not player.turn
        
        

    return game_board


def render(screen):
    for entity in board_tiles:
        entity.render(screen)

    for entity in car_list:
        entity.render(screen)

    for entity in player_list:
        entity.render(screen)
    



