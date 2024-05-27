import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import font
from game import Game  # Importăm clasa Game din fișierul game.py
from board import Board  # Importăm clasa Board din fișierul board.py
import threading
import pygame

class MinesweeperGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Minesweeper")  # Setăm titlul ferestrei
        self.root.geometry("1151x690")  # Setăm dimensiunea ferestrei

        # Încărcăm imaginea de fundal pentru pagina de start
        self.bg_image = PhotoImage(file="background.png")

        self.create_widgets()

    def create_widgets(self):
        # Cream un canvas pentru a plasa widget-urile pe el
        self.canvas = tk.Canvas(self.root, width=1151, height=690)
        self.canvas.pack(fill="both", expand=True)

        # Adăugăm imaginea de fundal pe canvas
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        # Cream un frame pentru a plasa butonul de start
        self.frame = tk.Frame(self.canvas, bg="white")
        self.canvas.create_window(470, 580, window=self.frame, anchor="center")  # Centrăm frame-ul

        # Definim o fontă mai mare pentru buton
        large_font = font.Font(size=18)

        # Butonul de start
        self.start_button = tk.Button(self.frame, text="Start", command=self.start_game, width=5, height=1, font=large_font)
        self.start_button.pack(padx=0, pady=0)  # Ajustăm padding-ul

    def start_game(self):
        # Dezactivăm butonul de start când jocul începe
        self.start_button.config(state=tk.DISABLED)
        # Pornim jocul
        self.run_game()

    def run_game(self):
        size = (10, 10)  # Dimensiunea plăcii de joc (10x10)
        prob = 0.1  # Probabilitatea de a avea o mină într-o celulă (10%)
        board = Board(size, prob)  # Creăm o instanță a clasei Board cu dimensiunile și probabilitatea date
        screen_size = (800, 800)  # Dimensiunea ferestrei Pygame

        # Rulăm bucla jocului Pygame într-un fir de execuție separat pentru a nu bloca interfața Tkinter
        game_thread = threading.Thread(target=self.run_pygame_game, args=(board, screen_size))
        game_thread.start()

    def run_pygame_game(self, board, screen_size):
        game = Game(board, screen_size)  # Inițializăm jocul cu placa și dimensiunea ecranului date
        game.run()  # Pornim jocul
        self.end_game()  # Apelăm funcția care se ocupă de încheierea jocului

    def end_game(self):
        # Re-activăm butonul de start când jocul se termină
        self.start_button.config(state=tk.NORMAL)
        # Afișăm un mesaj către utilizator
        messagebox.showinfo("Game Over", "Thanks for playing Minesweeper!")


if __name__ == "__main__":
    root = tk.Tk()  # Inițializăm obiectul Tkinter pentru a crea fereastra
    app = MinesweeperGUI(root)  # Inițializăm aplicația MinesweeperGUI cu fereastra root
    root.mainloop()  # Intrăm în bucla principală a interfeței Tkinter