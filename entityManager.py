import BoardTile
import Car
import time
import pygame
import GameAi
import Agent
import init_game

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

agent1 = Agent.Agent(1, 4)
agent2 = Agent.Agent(-1, 4)

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

    curr_player = GameAi.check_player_turn(car_list)
    print(f'It is {curr_player.number} turn')


    available_moves = GameAi.tree(curr_player.number, car_list, game_board)

    if curr_player.number == 1:
        action = agent1.chooseAction(available_moves)
    else:
        action = agent2.chooseAction(available_moves)

    # print(action)
    next_board = action['next_board']

    for car in car_list:
        if car.number == action['carNo']:
            new_car = init_game.find_car_from_board(action['next_board'], action['carNo'])
            car.update(new_car)

    

    # change whose turn it is
    for player in car_list:
        if player.number == 1 or player.number == -1:
            player.turn = not player.turn
         

    return next_board


def render(screen):
    for entity in board_tiles:
        entity.render(screen)

    for entity in car_list:
        entity.render(screen)

    for entity in player_list:
        entity.render(screen)
    



