# Rush Hour Shift

### How to Play

Open command prompt or anaconda prompt in the Rush Hour Shift folder and run the python script 'Rush_Hour.py'
It is best to have the command prompt window and the pygame window side by side when playing.


If a user wants to see different agents play, lines 31 and 32 in entityManager.py needs to be changed. The first number of the players' cars. They should always be 1 and -1. The second number in those lines represents what kind of a agent is created. Numbers represent a different agent:

1 = Human Player

2 = Best First Search (This can only be used on player = -1)

4 = Random agent

5 = Improved Breadth First Search


#### Human player
To move the cars when playing Rush Hour Shift the player types into the command prompt window which car he wants to move, the direction of the car (N,E,W,S) and how far that car should move, respectively and seperated by spaces. 

Example, if the input from the command line is: '4 e 1' car number 4 will move 1 step to the east (right).


#### Game board
If the user is unsatisfied with how the cars are placed on the board, he can open game.xls and change the cars position. Cars 1 should always be in line 3 and car -1 should always be in line 4
