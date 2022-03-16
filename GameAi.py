import Car
import Player
import numpy as np
import uuid

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
    for car in cars:
        if car.number == car_number:
            savedCar = car;
            break;
    x1car = savedCar.x1; x2car = savedCar.x2; y1car = savedCar.y1 ; y2car = savedCar.y2;



def tree_heuristic(cars, game_board, parents_ID):
    validPoints = []
    # at the beginnnign parents_ID = []; parents_ID.append(';')
    for car in cars:
        if car.number == 1 or car.number == -1:
            if car.turn == False:
                continue
            else:
                #special treatment if player can go forward, it always goes
                # hard coded going forward, it only works for player -1 on the right
                check, next_board = check_if_obstacles(car.x1-1, car.y1, game_board, car)
                if check == False:
                    score = 1;
                    id = (str(uuid.uuid4())[:8])
                    validPoints.append({'next_board': next_board, 'priority_score': score, 'Parents_ID': parents_ID, 'own_id': id} )
                    continue #maybe even put return validPoints here ? To speed up
                else:
                    obstacle_no = which_car_is_on_the_way(car.x1-1, car.y1, game_board);
                    check_if_car_can_be_moved_from_point(cars, obstacle_no, car.x1-1, car.y1)
                    #Players were taken care of, Now consider the  cars that are on the way on the way car:

                    pass
        # Now focus on the other cars, not significant so score = 100
        points = car.move_options(game_board)
        for point in points:
            #(point[0], point[1]) - (x,y) coordinate to check the obsatcles on the board

            check, next_board = check_if_obstacles(point[0], point[1], game_board, car)
            if check == False:
                # print(f"Car {car.number}. Move {point}, available")
                validPoints.append(
                    {'carNo': car.number, 'points': point, 'next_board': next_board, 'car': car, 'cars': cars})
            else:
                # print(f"Car {car.number}. Move {point}, NOT available")
                pass
    return validPoints

    pass

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
