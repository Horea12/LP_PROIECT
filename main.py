from game import Game
from board import Board
size = (9,9)
board = Board(size)
ScreenSize = (800, 800)
game = Game(board, ScreenSize)
game.run()