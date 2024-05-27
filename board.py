from piece import Piece  # Importăm clasa Piece din fișierul piece.py
from random import random

class Board:
    def __init__(self, size, prob):
        self.size = size  # Dimensiunea tablei (număr de rânduri și coloane)
        self.prob = prob  # Probabilitatea de a avea o bombă într-o celulă
        self.lost = False  # Indicator dacă jocul s-a pierdut sau nu
        self.won = False   # Indicator dacă jocul s-a câștigat sau nu
        self.numClicked = 0  # Numărul de celule făcute clic
        self.numNonBombs = 0  # Numărul de celule care nu conțin bombe
        self.setBoard()  # Inițializăm tabla de joc

    def setBoard(self):
        self.board = []  # Inițializăm tabla de joc ca o listă goală
        for row in range(self.size[0]):  # Pentru fiecare rând
            row_cells = []  # Inițializăm o listă pentru celulele din rândul curent
            for col in range(self.size[1]):  # Pentru fiecare coloană în rândul curent
                hasBomb = random() < self.prob  # Determinăm dacă celula curentă va conține o bombă
                if not hasBomb:
                    self.numNonBombs += 1  # Creștem numărul de celule care nu conțin bombe
                piece = Piece(hasBomb)  # Creăm o instanță a clasei Piece pentru această celulă
                row_cells.append(piece)  # Adăugăm celula în rândul curent
            self.board.append(row_cells)  # Adăugăm rândul la tabla de joc
        self.setNeighbors()  # Setăm vecinii pentru fiecare celulă

    def setNeighbors(self):
        for row in range(self.size[0]):  # Pentru fiecare rând
            for col in range(self.size[1]):  # Pentru fiecare coloană în rândul curent
                piece = self.getPiece((row, col))  # Obținem referința către celula curentă
                neighbors = self.getListofNeighbors((row, col))  # Obținem lista vecinilor pentru celula curentă
                piece.setNeighbors(neighbors)  # Setăm vecinii pentru celula curentă

    def getListofNeighbors(self, index):
        neighbors = []  # Inițializăm lista vecinilor
        for row in range(index[0] - 1, index[0] + 2):  # Iterăm prin rândurile vecine
            for col in range(index[1] - 1, index[1] + 2):  # Iterăm prin coloanele vecine
                outofBounds = row < 0 or row >= self.size[0] or col < 0 or col >= self.size[1]  # Verificăm dacă celula vecină se află în afara tablei
                same = row == index[0] and col == index[1]  # Verificăm dacă celula vecină este aceeași cu cea curentă
                if same or outofBounds:
                    continue  # Trecem la următoarea iterație dacă celula este aceeași cu cea curentă sau este în afara tablei
                neighbors.append(self.getPiece((row, col)))  # Adăugăm vecinul la lista de vecini
        return neighbors  # Returnăm lista de vecini

    def getSize(self):
        return self.size  # Returnăm dimensiunea tablei

    def getPiece(self, index):
        return self.board[index[0]][index[1]]  # Returnăm celula de la coordonatele date

    def handleClick(self, piece, flag):
        if piece.getClicked() or (not flag and piece.getFlagged()):  # Verificăm dacă celula a fost deja făcută clic sau dacă este deja marcată cu un steag
            return  # Dacă da, ieșim din funcție
        if flag:
            piece.toggleFlag()  # Dacă este activat modul de flag, comutăm starea flag-ului pentru celula curentă
            return  # Ieșim din funcție
        piece.click()  # Facem clic pe celulă
        if piece.getHasBomb():  # Verificăm dacă celula conține o bombă
            self.lost = True  # Dacă da, jocul s-a pierdut
            return  # Ieșim din funcție
        self.numClicked += 1  # Incrementăm numărul de celule făcute clic
        if piece.getNumAround() != 0:  # Dacă celula nu este goală
            return  # Ieșim din funcție
        for neighbor in piece.getNeighbors():  # Pentru fiecare vecin al celulei
            if not neighbor.getHasBomb() and not neighbor.getClicked():  # Dacă vecinul nu conține o bombă și nu a fost făcut clic încă
                self.handleClick(neighbor, False)  # Facem clic pe vecin

    def getLost(self):
        return self.lost  # Returnăm starea jocului (dacă s-a pierdut sau nu)

    def getWon(self):
        return self.numNonBombs == self.numClicked  # Verificăm dacă s-a câștigat jocul