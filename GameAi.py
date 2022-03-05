import Car
import Player


def check_player_turn(players): #check whos turn is it, players - players list
    for player in players:
        if player.turn == True:
            return player
 
def check_if_obstacles(x,y, game_board, car):
    if x < 0 or y < 0:
        return True

    if (car.number == 1 and x == len(game_board[0])-1) or (car.number == -1 and x == 0):
        return False  

    try:
        tile_value = int(game_board[y][x])
        if tile_value == 0:
            return False
    except:
        return True
    

    



def get_possible_moves(player, cars, game_board):
    print('get_possible_moves')
    validPoints = []

    objects = [player,*cars]

    # Chech which moves are available for each car
    for obj in objects:
        points = obj.move_options()
        for point in points:
            check = check_if_obstacles(point[0], point[1], game_board, obj)
            if check == False:
                # print(f"Car {obj.number}. Move {point}, available")
                validPoints.append( {'carNo': obj.number, 'points': point})
            else:
                # print(f"Car {obj.number}. Move {point}, NOT available")
                pass


    print(validPoints)


    if validPoints:
        return validPoints
    else:
        return None
    

def state_after_move(point, objectNumber, isPlayer, players, cars):
    if isPlayer == True:
        #check if to move object from the bottom or from the front
        if ( point[0] + 1 == players[objectNumber].x1 ):
            players[objectNumber].x1 = point[0]
            players[objectNumber].y1 = point[1]

def tree(player, cars, game_board): 
    print('tree')
    # player = check_player_turn(players)
    playerMoves = get_possible_moves(player, cars, game_board)

    print('hingað')
    # return
    init_state = {
        "players" : player,
        "cars" : cars
        }

    number = player.number
    for move in playerMoves:
        print(move)
        moveDecision = { "Player" : True,
                        "Name" : number,
                        "MoveLocation" : move,
                        "IsWinningMove" : isWinningMove
            }
   
    # What to do have at least first level of the tree like this: https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python

    #graph = [
    #    player number and pos: all possible moves for player and obstacles
    #    expand all
    #    ]


def update_board(game_board, curr_player, cars):
    move_list = []
    new_board = []

    

    tree(curr_player, cars, game_board)
