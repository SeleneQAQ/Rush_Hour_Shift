import BoardTile
import Car
import time
import pygame
import GameAi
import Agent
import init_game
import random

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
agent2 = Agent.Agent(-1, 5)


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
            pos_x = j * tile_width + startPos_x
            pos_y = i * tile_height + startPos_y

            if board[i][j] == 'W-1':
                tile_image = tile_finish_left
            elif board[i][j] == 'W1':
                tile_image = tile_finish_right
            else:
                tile_image = tile_regular
            board_tiles.append(BoardTile.BoardTile(pos_x, pos_y, tile_width, tile_height, tile_image))


def checkIfGameIsFinished(game_board):
    if game_board[2][15] == '1':
        return True, 1

    if game_board[3][0] == '-1':
        return True, -1

    return False, 0

def selectAMoveFromAgent(agent, available_moves, cars, game_board):
    
    if agent.number == -1 and agent.type == 5:
        action = GameAi.tree_heuristic(cars, game_board)
    else:
        action = agent.chooseAction(available_moves)

    return action


def update(game_board, steps):
    # print(game_board)
    game_finished, winner = checkIfGameIsFinished(game_board)
    if game_finished:
        return game_board, winner

    curr_player = GameAi.check_player_turn(car_list)
    print()
    print(f'It is {curr_player.number} turn')

    available_moves = GameAi.tree(curr_player.number, car_list, game_board)

    if steps-1 != 0 and curr_player.number == 1:
        print("player 1 left steps:")
        print(steps)
        # action = agent1.chooseAction(available_moves)
        action = selectAMoveFromAgent(agent1, available_moves, car_list, game_board)
        next_board = action['next_board']
        new_car = init_game.find_car_from_board(action['next_board'], action['carNo'])
        action['car'].update(new_car)
        steps -= 1
        return next_board, 0, steps

    if steps-1 != 0 and curr_player.number == -1:
        print("player 2 left steps")
        print(steps)
        # action = agent2.chooseAction(available_moves)
        action = selectAMoveFromAgent(agent2, available_moves, car_list, game_board)
        next_board = action['next_board']
        new_car = init_game.find_car_from_board(action['next_board'], action['carNo'])
        action['car'].update(new_car)
        steps -= 1
        return next_board, 0, steps

    if steps-1 == 0 and curr_player.number == 1:
        print("player 1 left steps")
        print(steps)
        # action = agent1.chooseAction(available_moves)
        action = selectAMoveFromAgent(agent1, available_moves, car_list, game_board)
        next_board = action['next_board']
        new_car = init_game.find_car_from_board(action['next_board'], action['carNo'])
        action['car'].update(new_car)
        steps -= 1
        for player in car_list:
            if player.number == 1 or player.number == -1:
                player.turn = not player.turn
        steps = random.randint(1, 5)
        return next_board, 0, steps
        
    if steps-1 == 0 and curr_player.number == -1:
        print("player 2 left steps")
        print(steps)
        # action = agent2.chooseAction(available_moves)
        action = selectAMoveFromAgent(agent2, available_moves, car_list, game_board)
        next_board = action['next_board']
        new_car = init_game.find_car_from_board(action['next_board'], action['carNo'])
        action['car'].update(new_car)
        steps -= 1
        for player in car_list:
            if player.number == 1 or player.number == -1:
                player.turn = not player.turn
        steps = random.randint(1, 5)
        return next_board, 0, steps
    # print(action)

    # for car in car_list:
    #     if car.number == action['carNo']:
    # print(new_car)

    # change whose turn it is

    return


def render(screen):
    for entity in board_tiles:
        entity.render(screen)

    for entity in car_list:
        entity.render(screen)

    for entity in player_list:
        entity.render(screen)
