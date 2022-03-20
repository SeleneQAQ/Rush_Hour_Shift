import xlrd
import numpy as np
import Car
import time

table = xlrd.open_workbook('game.xls')
sheet = table.sheet_by_name('Sheet1')
row = sheet.nrows
col = sheet.ncols
def find_AI():
    for i in range(row):
        for j in range(col):
            if sheet.cell(i, j).value == 'AI':
                return [j, i]


def find_YOU():
    for i in range(row):
        for j in range(col):
            if sheet.cell(i, j).value == 'YOU':
                return [j, i]

def find_Car(x):
    for i in range(row):
        for j in range(col):
            if sheet.cell(i, j).value == x:
                x1=j
                y1=i
                inc=1
                carFound = False
                
                # x1,y1 - staring coords of a car
                # x2, y2 - end coords of a car
                
                if i+inc < row:
                    while(sheet.cell(i+inc, j).value == x):
                        x2=j
                        y2=i+inc
                        inc=inc+1
                        carFound = True
                        # print(i+inc, j, row)
                        if i+inc == row:
                            break

                if carFound == False:
                    inc = 1
                    while(sheet.cell(i, j+inc).value ==x):
                        x2=j+inc
                        y2=i
                        inc=inc+1
                        carFound = True
               
                if carFound == False:
                    return False

                if x == -1 or x == 1:
                    finishline = f'W{str(x)}'
                    # return Player.Player(x, x1, y1, x2, y2, finishline)
                    return Car.Car(x, x1, y1, x2, y2, finishline)
                else:
                   return Car.Car(x, x1, y1, x2, y2, finishline=None)
                # return car
    return False


def find_car_from_board(board, x):

    for i in range(row):
        for j in range(col):
            if board[i][j] == str(x):
                x1=j
                y1=i
                inc=1
                carFound = False
                
                # x1,y1 - staring coords of a car
                # x2, y2 - end coords of a car
                if i+inc < row:
                    while(board[i+inc][j] == str(x)):
                        x2=j
                        y2=i+inc
                        inc=inc+1
                        carFound = True
                        # print(i+inc, j, row)
                        if i+inc == row:
                            break

                
                if carFound == False:
                    inc = 1
                    while(board[i][j+inc] == str(x)):
                        x2=j+inc
                        y2=i
                        inc=inc+1
                        carFound = True
                        if j+inc == col:
                            break
               
                if carFound == False:
                    continue

                if x == -1 or x == 1:
                    finishline = f'W{str(x)}'
                    # return Player.Player(x, x1, y1, x2, y2, finishline)
                    return Car.Car(x, x1, y1, x2, y2, finishline)
                else:
                    return Car.Car(x, x1, y1, x2, y2, finishline=None)

    return None

        

# def generate_players():
#     players = [find_Car(-1, True), find_Car(1, True)]
#     return players



def generate_Car_List(amount):
    carList = []
    for i in range(-1, amount):   
        if i == 0:
            continue 
        car = find_Car(i)
        if car == False: #if no car at his number found    
            continue
        else:
            carList.append(car)
            # car.printAttributes()

    return carList

def init_game():
    board = []
    row_board = None
    for i in range(row):
        row_board = sheet.row_values(i)
        for j in range(len(row_board)):
            try:
                row_board[j] = int(row_board[j])
            except ValueError:
                pass

        board.append(row_board)

    board = np.array(board)

    location_AI = find_AI()
    location_You = find_YOU()

    carList = []
    #Assume we have maximum 10 cars
    carList = generate_Car_List(50)

    # Generate the players
    # player_list = generate_players()

    return board, carList


# board = init_game()
