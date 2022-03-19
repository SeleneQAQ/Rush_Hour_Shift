import Car
import Player
import numpy as np
import uuid

import init_game

def check_player_turn(players):  # check whos turn is it, players - players list
    for player in players:
        if player.number == 1 or player.number == -1:
            if player.turn == True:
                return player


def find_next_board(game_board, car, new_x, new_y):
    new_board = game_board.copy()

    # clear board
    if car.positionVertical == False:
        if car.x1 < car.x2:
            start = car.x1
            end = car.x2 + 1
        else:
            start = car.x2
            end = car.x1 + 1

        for i in range(start, end):
            new_board[car.y1][i] = 0

    else:
        if car.y1 < car.y2:
            start = car.y1
            end = car.y2 + 1
        else:
            start = car.y2
            end = car.y1 + 1

        for i in range(start, end):
            new_board[i][car.x1] = 0

    # set new position of car
    if car.positionVertical == False:
        if abs(new_x - car.x1) < abs(new_x - car.x2):
            start = new_x
            end = new_x + car.length
        else:
            start = new_x - (car.length - 1)
            end = new_x + 1

        for i in range(start, end):
            new_board[car.y1][i] = car.number
    else:
        if abs(new_y - car.y1) < abs(new_y - car.y2):
            start = new_y
            end = new_y + car.length
        else:
            start = new_y - (car.length - 1)
            end = new_y + 1

        for i in range(start, end):
            new_board[i][car.x1] = car.number

    return new_board


def check_if_obstacles(x, y, game_board, car):
    if x < 0 or y < 0:
        return True, None
        
    if (car.number == 1 and x == len(game_board[0]) - 1) or (car.number == -1 and x == 0):
        next_board = find_next_board(game_board, car, x, y)
        return False, next_board

    try:
        tile_value = int(game_board[y][x])
        if tile_value == 0:
            next_board = find_next_board(game_board, car, x, y)
            return False, next_board
        else:
            return True, None
    except:
        return True, None

def which_car_is_on_the_way(x,y, game_board):
    try:
        tile_value = int(game_board[y][x])
        return tile_value
    except:
        return None

def check_if_car_can_be_moved_from_point(cars, car_number, x, y):
    #x, y - cooridinates of point from which the car has to be moved
    # print('check if car can be moved from points')
    # print(car_number, 'x,y:', x,y)

    for car in cars:
        if car.number == car_number:
            savedCar = car
            break
    x1car, x2car, y1car, y2car = savedCar.x1, savedCar.x2, savedCar.y1, savedCar.y2
    print(x1car, x2car, y1car, y2car)

def find_what_car_moved(cars, game_board):
    for car in cars:
        try:
            tile_value1 = int(game_board[car.y1][car.x1])
            tile_value2 = int(game_board[car.y2][car.x2])
            if not ((tile_value1 == car.number) and (tile_value2 == car.number)):
                return car
        except:
            pass
    return None




def tree_heuristic(cars, game_board):
    validPoints = []
    print()
    print()
    print(game_board)
    print('Inside tree heuristic:')
    # at the beginnnign parents_ID = []; parents_ID.append(';')
    for car in cars:
        # print(car.number)
        if car.number == 1 or car.number == -1:
            if car.turn == True:
                break


    # print(car, car.number)

    #special treatment if player can go forward, it always goes
    # hard coded going forward, it only works for player -1 on the right
    print(f'it\'s time for car number {car.number} to make a move!')
    check, next_board = check_if_obstacles(car.x1-1, car.y1, game_board, car)
    if check == False:
        #maybe even put return validPoints here ? To speed up
        return {'next_board': next_board, 'car': car, 'carNo': car.number}
    else:
        obstacle_no = which_car_is_on_the_way(car.x1-1, car.y1, game_board)

        car_in_way = init_game.find_car_from_board(game_board, obstacle_no)
        # check_if_car_can_be_moved_from_point(cars, obstacle_no, car.x1-1, car.y1)
        #Players were taken care of, Now consider the  cars that are on the way on the way car:


        # Now focus on the other cars, not significant so score = 100
        ## now we want to get all possible moves for the obstacle car
        zero_point = (car.x1-1, car.y1)

        points = car_in_way.move_options(game_board)
        move_list = []
        for p in points:
            move_list.append({'board': game_board, 'point': p, 'car_to_check': car_in_way, 'zero_point': (car.x1-1, car.y1)})


        solution_not_found = True
        lvl = 0

        while solution_not_found:
            lvl += 1
            if lvl == 100:
                solution_not_found = False
                return {'carNo': None}

            move_list2 = []
            for move in move_list:
                # print()
                point = move['point']
                if point[0] < 0 or point[1] < 0:
                    continue

                board = move['board']
                car_to_check = move['car_to_check']
                if 'checked_cars' in move: 
                    checked_cars = move['checked_cars'].copy()
                else:
                    checked_cars = []

                #(point[0], point[1]) - (x,y) coordinate to check the obsatcles on the board
                obstacle, next_board = check_if_obstacles(point[0], point[1], board, car_to_check)

                if ('original_move' in move):
                    if move['original_move'] is None:
                        original_move = next_board
                    else:
                        original_move = move['original_move']
                else:
                    original_move = next_board

                if obstacle:
                    # Use this if obstacle is in way
                    # Check which car is in the way
                    obstacle_no = which_car_is_on_the_way(point[0], point[1], board)

                    if obstacle_no == None:
                        continue

                    # If we are checking a car we have alreadt checked, then stop to avoid going in circles
                    # Also, player -1 can't move car 1 so stop also if that is a checked car
                    if obstacle_no in checked_cars or obstacle_no == 1:
                        continue

                    new_car_in_way = init_game.find_car_from_board(board, obstacle_no)
                    new_collision_points = new_car_in_way.move_options(board)

                    zero_point = point
                    checked_cars.append(car_to_check.number)
                    for p in new_collision_points:
                        move_list2.append({'board': board,
                                           'point': p,
                                           'car_to_check': new_car_in_way,
                                           'zero_point': zero_point,
                                           'original_move': original_move,
                                           'checked_cars': checked_cars})

                else:
                    # Able to move obstacle car
                    zero_point = move['zero_point']

                    if which_car_is_on_the_way(zero_point[0], zero_point[1], next_board) == 0:
                        solution_not_found = not solution_not_found

                        moved_car = find_what_car_moved(cars, original_move)
                        return {'next_board': original_move, 'car': moved_car, 'carNo': moved_car.number}
                    else:
                        points = car_to_check.move_options(next_board)

                        if car_to_check.x1 < car_to_check.x2:
                            x_start = car_to_check.x1
                            x_end = car_to_check.x2
                        else:
                            x_start = car_to_check.x2
                            x_end = car_to_check.x1
                    
                        if car_to_check.y1 < car_to_check.y2:
                            y_start = car_to_check.y1
                            y_end = car_to_check.y2
                        else:
                            y_start = car_to_check.y2
                            y_end = car_to_check.y1

                        for point in points:
                            if car_to_check.positionVertical:
                                if not (y_start <= point[1] and point[1] <= y_end):
                                    move_list2.append({'board': next_board,
                                                       'point': point,
                                                       'car_to_check': car_to_check,
                                                       'zero_point': zero_point,
                                                       'original_move': original_move,
                                                       'checked_cars': checked_cars})

                            if not car_to_check.positionVertical:
                                if not (x_start <= point[0] and point[1] <= x_end):
                                    move_list2.append({'board': next_board,
                                                       'point': point,
                                                       'car_to_check': car_to_check,
                                                       'zero_point': zero_point,
                                                       'original_move': original_move,
                                                       'checked_cars': checked_cars})
                        
            move_list = move_list2.copy()
    
    return {'carNo': None}


def get_possible_moves(player, cars, game_board):
    validPoints = []

    # objects = [player,*cars]

    # Chech which moves are available for each car
    for car in cars:
        if car.number == -player:
            continue
        points = car.move_options(game_board)
        for point in points:
            check, next_board = check_if_obstacles(point[0], point[1], game_board, car)
            if check == False:
                # print(f"Car {car.number}. Move {point}, available")
                validPoints.append(
                    {'carNo': car.number, 'points': point, 'next_board': next_board, 'car': car, 'cars': cars})
            else:
                # print(f"Car {car.number}. Move {point}, NOT available")
                pass
    return validPoints


def state_after_move(point, objectNumber, isPlayer, players, cars):
    if isPlayer == True:
        # check if to move object from the bottom or from the front
        if (point[0] + 1 == players[objectNumber].x1):
            players[objectNumber].x1 = point[0]
            players[objectNumber].y1 = point[1]


def tree(player, cars, game_board):
    
    # player = check_player_turn(players)
    playerMoves = get_possible_moves(player, cars, game_board)
    

    return playerMoves

    # What to do have at least first level of the tree like this: https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python

    # graph = [
    #    player number and pos: all possible moves for player and obstacles
    #    expand all
    #    ]
