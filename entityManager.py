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
            pos_x = j*tile_width + startPos_x
            pos_y = i*tile_height + startPos_y

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


def update(game_board):
    # print(game_board)
    game_finished, winner = checkIfGameIsFinished(game_board)
    if game_finished:
        return game_board, winner

    curr_player = GameAi.check_player_turn(car_list)
    print()
    print(f'It is {curr_player.number} turn')

    #steps = random.randint((1, 5))
    #for i in steps:
    available_moves = GameAi.tree(curr_player.number, car_list, game_board)

    if curr_player.number == 1:
        # action = agent1.chooseAction(available_moves)
        action = available_moves[-1]
    else:
        if agent2.type == 5:
            print('------------------------------')
            action = GameAi.tree_heuristic(car_list, game_board)

            if action['carNo'] is None:
                action = agent2.chooseActionRandom(available_moves)
                # print('I AM PLAYING A RANDOM MOVE RIGHT NOW')
            print()
            print()
            print('Inside Entity Manager:')

            print(action['carNo'])
            print(action['next_board'])
            # test = input('solution found:')

        else:
            action = agent2.chooseAction(available_moves)

    # print('ACTION IS!!!')
    # print(action['carNo'])
    # print('(x1,y1) = ', action['car'].x1, action['car'].y1, '(x2,y2) =', action['car'].x2, action['car'].y2)
    # print(action['next_board'])
    next_board = action['next_board']


    new_car = init_game.find_car_from_board(action['next_board'], action['carNo'])
    # print(new_car)
    # print(action['car'], 'action_car')

    for car in car_list:
        if car.number == action['carNo']:
            # print(car, 'car_list_car')
            car.update(new_car)
    # action['car'].update(new_car)


    # change whose turn it is
    for player in car_list:
        if player.number == 1 or player.number == -1:
            player.turn = not player.turn
         
    return next_board, 0


def render(screen):
    for entity in board_tiles:
        entity.render(screen)

    for entity in car_list:
        entity.render(screen)

    for entity in player_list:
        entity.render(screen)
    



