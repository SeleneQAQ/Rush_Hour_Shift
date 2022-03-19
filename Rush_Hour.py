import random

import pygame
# import keys
import Car
import time
import init_game
import entityManager
import GameAi


pygame.init()
points = []
points.append((1,2))
points.append((3,4))
print(points[0][0])

width, height = 1080, 600
screen = pygame.display.set_mode((width, height))
white = (255,255,255)
steps = random.randint(1, 5)
run = True
carList = []
board, carList = init_game.init_game()

print(board.shape)
print(board)
print()
print(carList)
print('#################################')
print('#################################')
print('#################################')
# for c in carList:
#     c.printAttributes()

entityManager.generate_board(board)
entityManager.set_carlist(carList)
# entityManager.set_players(player_list)

screen.fill(white)
entityManager.render(screen)
pygame.display.update()
winner = 0

print(board)

count = 0
while(run):
    count += 1
    #pygame.time.delay(100)
    #event_handler()
    # print('inside loop')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()


    # if not keys[pygame.K_o]:

    if winner == 0:
        board, winner, steps = entityManager.update(board, steps)
    # print(board)


    if keys[pygame.K_q]:
        run = False

    # if keys[pygame.K_h]:
    #     entityManager.resetCars()

    entityManager.render(screen)

    if winner != 0:
        myfont = pygame.font.SysFont('Arial', 60)
        textsurface = myfont.render(f'Player {winner} is the winner of this game', False, (255, 255, 255))
        screen.blit(textsurface, ((width/2)-370,(height/2)))

    pygame.display.update()
    screen.fill(white)
    # if count == 4:
    #     run = False
    if winner == 0:
        pygame.time.wait(1200)


pygame.init()


