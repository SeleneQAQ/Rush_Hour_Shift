from copy import copy
from random import choice

from matplotlib.pyplot import step
import numpy as np
from sqlalchemy import true

###############################
# For the graph thing:
# TA said that when choosing an action we only create child nodes from the current position and not go deeper
# Then we have to define a hueristic function which is the one the decides what move to choose
# and mentioned something about minmax algorithm
###############################
import GameAi


class Agent(object):
    def __init__(self, number, type):
        self.number = number
        self.type = type  # 1 = human, 2 = BSF, 3 = A*, 4 = Random

    def chooseAction(self, available_moves):

        if self.type == 1:
            action = self.chooseActionHuman(available_moves)

        if self.type == 2:
            action = self.chooseShortestMoves(available_moves)

        if self.type == 3:
            action = self.chooseActionAStar(available_moves)

        if self.type == 4:
            action = self.chooseActionRandom(available_moves)

        return action

    def chooseActionRandom(self, available_moves):
        new_move = available_moves[np.random.randint(len(available_moves))]
        return new_move

    def chooseShortestMoves(self, available_moves):
        shortest_move = self.calculateDistance(available_moves)
        distance = shortest_move[0]['distance']
        move_list = []
        for i in range(len(shortest_move)):
            next_move = GameAi.get_possible_moves(-1, shortest_move[i]['available_moves']['cars'],
                                                  shortest_move[i]['available_moves']['next_board'])
            next_shortest_move = self.calculateDistance(next_move)
            if distance > next_shortest_move[0]['distance']:
                move_list = []
                distance = next_shortest_move[0]['distance']
                move_list.append(shortest_move[i])
            if distance == next_shortest_move[0]['distance']:
                move_list.append(shortest_move[i])
        random_move = choice(move_list)
        if shortest_move[0]['distance'] < random_move['distance']:
            return shortest_move[0]['available_moves']
        else:
            return random_move['available_moves']

    def calculateDistance(self, available_moves):
        # calculate the distance in each possible world and return with the shortest distance
        subtree = []
        for i in available_moves:
            for j in i['next_board']:
                for k in range(len(j)):
                    if j[k] == '-1':
                        subtree.append({'distance': k, 'available_moves': i})
                        break
        move = sorted(subtree, key=lambda subtree: subtree.__getitem__('distance'))
        return move

    def chooseActionHuman(self, available_moves, steps_left=1):
        next_moves = []
        input_is_valid = False
        car = None
        dir = None
        step_size = None
        while not input_is_valid:
            pass_check = 0
            if steps_left == 1:
                print('You have 1 move left')
            else:
                print(f"You have {steps_left} moves left.")

            raw_line = input(f'Select a car, direction (N,W,S,E) and step size:')
            line = raw_line.split(" ")
            print(line)

            try:
                car = int(line[0])
                for move in available_moves:
                    if car == move['carNo']:
                        pass_check += 1
                        # print('passed car check')
                        break
            except:
                print('This car has no availables moves or is not on the board. Please pick again.')

            # The only available directions are ['N','W','E','S']
            dir = line[1].upper()
            if dir in ['N', 'W', 'E', 'S']:
                # print('passed direction')
                pass_check += 1
            else:
                print('Not an available direction. Try again.')

            try:
                step_size = int(line[2])
                if 0 < step_size and step_size <= steps_left:
                    # print('passed direction')
                    pass_check += 1
                elif step_size <= 0:
                    print('Step size can\'t be <= 0. Try again.')
                elif step_size > steps_left:
                    print(f'Having step size > steps left is not allowed. Try again.')

            except:
                print('Not readable value for step size. Try again.')

            # print('pass_check', pass_check)
            legal_move_found = 0
            if pass_check == 3:

                for move in available_moves:
                    if car != move['carNo']:
                        continue

                    if self.checkIfDirectionIsAllowed(dir, step_size, move):
                        print('Step: Legal move', move['points'])
                        next_moves.append(move)
                        legal_move_found += 1

            if legal_move_found != 1:
                print('Illegal move. Try again')
            else:
                input_is_valid = True

        print('out of while loop', car, dir, step_size)

        return next_moves[0]

    def checkIfDirectionIsAllowed(self, dir, step, move):
        car = move['car']
        points = move['points']
        if car.positionVertical and dir in ['N', 'S']:
            if dir == 'N':
                if car.y1 < car.y2:
                    y_up = car.y1
                else:
                    y_up = car.y2

                if step == 0:
                    if (points[1] < y_up):
                        return True
                else:
                    if (points[1] == y_up - step):
                        return True

            if dir == 'S':
                if car.y1 < car.y2:
                    y_down = car.y2
                else:
                    y_down = car.y1

                if step == 0:
                    if (points[1] > y_down):
                        return True
                else:
                    if (points[1] == y_down + step):
                        return True

            return False
        if not car.positionVertical and dir in ['W', 'E']:
            if dir == 'W':
                if car.x1 < car.x2:
                    x_left = car.x1
                else:
                    x_left = car.x2
                if step == 0:
                    if (points[0] < x_left):
                        return True
                else:
                    if (points[0] == x_left - step):
                        return True

            if dir == 'E':
                if car.x1 < car.x2:
                    x_right = car.x2
                else:
                    x_right = car.x1

                print(points, x_right, step, x_right + step)

                if step == 0:
                    if (points[0] > x_right):
                        return True
                else:
                    if (points[0] == x_right + step):
                        return True

            return False

        return False

    def chooseActionAStar(self, available_moves):
        min_grade = 1000
        move = None

        for m in available_moves:
            # print(m)
            grade = self.heuristic_function(m)
            if grade < min_grade:
                min_grade = grade
                move = m

        return move

    def heuristic_function(self, move):
        board = move['next_board']
        # print(move)

        # for car in move['cars']:
        #     print(car)

        if self.number == 1:
            row = 2
            end = board.shape[1]
            cars_in_way = False
        else:
            row = 3
            end = 0
            cars_in_way = True

        min_dist_from_goal = 100

        move_grade = 0
        player_car_found = False
        for i in range(board.shape[1]):
            try:
                board_value = int(board[row][i])
            except:
                continue
            # print(board_value == self.number)

            if board_value == self.number and not player_car_found:
                player_car_found = not player_car_found
                cars_in_way = not cars_in_way

            if board_value == self.number and abs(end - i) < min_dist_from_goal:
                min_dist_from_goal = abs(end - i)

            if cars_in_way:
                if board_value != self.number and board_value != 0:
                    move_grade += 1

        # The min_dist_from_goal needs to be lowered by one
        min_dist_from_goal -= 1
        move_grade += min_dist_from_goal

        if move['carNo'] != self.number:
            move_grade += 1

        print('car number:', move['carNo'], 'Grade:', move_grade)

        return move_grade
        pass
