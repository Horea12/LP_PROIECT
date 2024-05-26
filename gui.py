import tkinter as tk
from tkinter import messagebox
from game import Game
from board import Board
import threading
import pygame

class MinesweeperGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Minesweeper")
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.start_button = tk.Button(self.frame, text="Start Game", command=self.start_game)
        self.start_button.pack(padx=20, pady=20)

    def start_game(self):
        self.start_button.config(state=tk.DISABLED)
        self.run_game()

    def run_game(self):
        size = (10, 10)
        prob = 0.1
        board = Board(size, prob)
        screen_size = (800, 800)

        # Run the Pygame game loop in a separate thread to prevent blocking the Tkinter GUI
        game_thread = threading.Thread(target=self.run_pygame_game, args=(board, screen_size))
        game_thread.start()

    def run_pygame_game(self, board, screen_size):
        game = Game(board, screen_size)
        game.run()
        self.end_game()

    def end_game(self):
        # Re-enable the start button once the game ends
        self.start_button.config(state=tk.NORMAL)
        # Show a message box to the user
        messagebox.showinfo("Game Over", "Thanks for playing Minesweeper!")

if __name__ == "__main__":
    root = tk.Tk()
    app = MinesweeperGUI(root)
    root.mainloop()