
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

run = True
carList = []
board, carList, player_list = init_game.init_game()

print(board.shape)
print(board)
# print()
# print(carList)
# for p in player_list:
#     p.printAttributes()

entityManager.generate_board(board)
entityManager.set_carlist(carList)
entityManager.set_players(player_list)
print("enter tree")
GameAi.tree(player_list, carList)

while(run):
    #pygame.time.delay(100)
    #event_handler()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()


    # if not keys[pygame.K_o]:
        # entityManager.update(keys)


    if keys[pygame.K_q]:
        run = False

    # if keys[pygame.K_h]:
    #     entityManager.resetCars()

    entityManager.render(screen)


    pygame.display.update()
    screen.fill(white)



pygame.init()