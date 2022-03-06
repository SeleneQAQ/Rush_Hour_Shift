import numpy as np

class Agent(object):
    def __init__(self, number, type):
        self.number = number
        self.type = type # 1 = human, 2 = BSF, 3 = A*, 4 = Random
        


    def chooseAction(self, available_moves):
        if self.type == 4:
            action = self.chooseActionRandom(available_moves)

        return action



    def chooseActionRandom(self, available_moves):
        new_move = available_moves[np.random.randint(len(available_moves))]
        return new_move
