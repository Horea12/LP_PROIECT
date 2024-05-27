from game import Game  # Importăm clasa Game din fișierul game.py
from board import Board  # Importăm clasa Board din fișierul board.py

# Definim dimensiunea tablei și probabilitatea de a avea o bombă în fiecare celulă
size = (10, 10)
prob = 0.1

# Inițializăm o instanță a clasei Board cu dimensiunea și probabilitatea specificate
board = Board(size, prob)

# Definim dimensiunea ecranului de joc
screenSize = (800, 800)

# Inițializăm o instanță a clasei Game cu tabla și dimensiunea ecranului specificate
game = Game(board, screenSize)

# Pornim jocul
game.run()