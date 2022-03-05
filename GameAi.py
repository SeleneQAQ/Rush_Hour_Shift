import Car
import Player


def check_player_turn(players): #check whos turn is it, players - players list
    for player in players:
        if player.turn == True:
            return player;
 
def check_if_obstacles(currentObject,x,y, cars):
    if x <=0:
        return True
    if y < 0:
        return True
    # Add the if for exeeding the board dimenstions!!!!!!
       #....
       #....
    for car in cars:
        if car.number == currentObject.number:
            continue # to prevent the current object from comparing to itself
        if car.positionVertical == True:
            if x == car.x1:
                if y >= car.y1 & y <= car.y2:
                    print('obstacle vertical on car')
                    print(car.number)
                    return True
        if car.positionVertical == False:
            if (y == car.y1):
                 if x >= car.x1 & x<= car.x2:
                    print('obstacle horizontal on car')
                    print(car.number)
                    return True
    # no obstacles found:
    return False  

def get_possible_moves(currentObject, points, cars):
    validPoints = []
    print(points)
    for point in points:
        
        #print('check obstacles')
        print('Obstacles coords:')
        print(point)
        check = check_if_obstacles(currentObject, point[0], point[1], cars)
        print('is there an obstacle? :')
        print(check)
        if check == False:
            validPoints.append(point)

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
    
    playerMoves = get_possible_moves(player, player.move_options(), cars)
    init_state = {
        "players" : players,
        "cars" : cars
        }
   
    number = player.number
    treeOneLvl = []
    if playerMoves != None:
        for move in playerMoves:
        
            moveDecision = { "Player" : True,
                            "Name" : number,
                            "MoveLocation" : move,
                            "IsWinningMove" : False
                }
            treeOneLvl.append(moveDecision);
    for car in cars:
        print('carr')
        carMoves = get_possible_moves(car, car.move_options(), cars)
        if carMoves != None:
            for move in carMoves:
                moveDecision = { "Player" : False,
                            "Name" : car.number,
                            "MoveLocation" : move
                            }
                treeOneLvl.append(moveDecision);

    print('TREE level:')
    print(treeOneLvl)
   
    # What to do have at least first level of the tree like this: https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python

    #graph = [
    #    player number and pos: all possible moves for player and obstacles
    #    expand all
    #    ]
