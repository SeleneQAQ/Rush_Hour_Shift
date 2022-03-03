import Car
import Player


def check_player_turn(players): #check whos turn is it, players - players list
    for player in players:
        if player.turn == True:
            return player;
 
def check_if_obstacles(x,y, cars):
    if x < 0 | y < 0:
        return False
    # Add the if for exeeding the board dimenstions!!!!!!
       #....
       #....
    for car in cars:
        if car.positionVertical == True:
            if y <= car.y1 & y >= car.y2:
                return True
        if car.positionVertical == False:
             if x >= car.x1 & x<= car.x2:
                return True
    # no obstacles found:
    return False  

def get_possible_moves(points, cars):
    validPoints = []
    for point in points:
        check = check_if_obstacles(point[0], point[1], cars)
        if check == False:
            points.append(point)
    if validPoints:
        return validPoints
    else: return None

def state_after_move(point, objectNumber, isPlayer, players, cars):
    if isPlayer == True:
        #check if to move object from the bottom or from the front
        if ( point[0] + 1 == players[objectNumber].x1 ):
            players[objectNumber].x1 = point[0]
            players[objectNumber].y1 = point[1]

def tree(players, cars): 
    player = check_player_turn(players)
    playerMoves = get_possible_moves(player.move_options(), cars)
    init_state = {
        "players" : players,
        "cars" : cars
        }
    number = player.player
    for move in playerMoves:
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
