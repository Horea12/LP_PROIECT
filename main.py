from game import Game
from board import Board
size = (9,9)
prob = 0.5
board = Board(size, prob)
ScreenSize = (800, 800)
game = Game(board, ScreenSize)
game.run()