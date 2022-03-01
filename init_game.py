import xlrd

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
                return [j, i]

def init_game():
    for i in range(row):
        print(sheet.row_values(i))
    location_AI = find_AI()
    location_You = find_YOU()
    location_Car = find_Car(2)
    print(location_You,location_AI,location_Car)


init_game()
