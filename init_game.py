import xlrd
import numpy as np
import Car
import Player

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

def find_Car(x, player=False):
    for i in range(row):
        for j in range(col):
            if sheet.cell(i, j).value == x:
                x1=j
                y1=i
                inc=1
                carFound = False
                
                # x1,y1 - staring coords of a car
                # x2, y2 - end coords of a car
                while(sheet.cell(i+inc, j).value ==x):
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

                if player:
                    finishline = f'W{str(x)}'
                    return Player.Player(x, x1, y1, x2, y2, finishline)
                else:
                   return Car.Car(x, x1, y1, x2, y2)
                # return car
    return False

def generate_players():
    players = [find_Car(-1, True), find_Car(1, True)]
    return players



def generate_Car_List(amount):
    carList = []
    for i in range(2, amount):    
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
    carList = generate_Car_List(10)

    # Generate the players
    player_list = generate_players()

    return board, carList, player_list


# board = init_game()
