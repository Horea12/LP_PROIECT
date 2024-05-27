import pygame
import os
from time import sleep

class Game:
    def __init__(self, board, screenSize):
        self.board = board  # Referință către obiectul Board asociat jocului
        self.screenSize = screenSize  # Dimensiunea ecranului de joc
        # Calculăm dimensiunea fiecărei piese din funcție de dimensiunea ecranului și numărul de rânduri și coloane ale tablei
        self.pieceSize = self.screenSize[0] // self.board.getSize()[1], self.screenSize[1] // self.board.getSize()[0]
        self.loadImages()  # Încărcăm imaginile pentru piese

    def run(self):
        pygame.init()  # Inițializăm modulul pygame
        self.screen = pygame.display.set_mode(self.screenSize)  # Inițializăm fereastra de afișare
        running = True  # Indicator pentru starea jocului (în desfășurare sau terminat)
        while running:
            for event in pygame.event.get():  # Iterăm prin toate evenimentele din pygame
                if event.type == pygame.QUIT:  # Verificăm dacă utilizatorul a închis fereastra
                    running = False  # Dacă da, oprim bucla și închidem jocul
                if event.type == pygame.MOUSEBUTTONDOWN:  # Verificăm dacă utilizatorul a făcut clic pe mouse
                    position = pygame.mouse.get_pos()  # Obținem poziția cursorului mouse-ului
                    rightClick = pygame.mouse.get_pressed()[2]  # Verificăm dacă a fost clic dreapta sau stânga
                    self.handleClick(position, rightClick)  # Tratăm evenimentul de clic

            self.draw()  # Desenăm starea curentă a jocului
            pygame.display.flip()  # Actualizăm ecranul
            if self.board.getWon():  # Verificăm dacă jocul a fost câștigat
                sound = pygame.mixer.Sound("win.wav")  # Încărcăm sunetul pentru câștig
                sound.play()  # Redăm sunetul
                sleep(3)  # Așteptăm 3 secunde
                running = False  # Oprim jocul

        pygame.quit()  # Închidem modulul pygame

    def draw(self):
        topLeft = (0, 0)  # Coordonatele de început pentru desenare
        for row in range(self.board.getSize()[0]):  # Iterăm prin fiecare rând al tablei de joc
            for col in range(self.board.getSize()[1]):  # Iterăm prin fiecare coloană în rândul curent
                piece = self.board.getPiece((row, col))  # Obținem referința către piesa curentă
                image = self.getImage(piece)  # Obținem imaginea corespunzătoare piesei
                self.screen.blit(image, topLeft)  # Desenăm imaginea pe ecran la poziția specificată
                topLeft = topLeft[0] + self.pieceSize[0], topLeft[1]  # Actualizăm coordonatele pentru desenare pe următoarea coloană
            topLeft = 0, topLeft[1] + self.pieceSize[1]  # Trecem la următorul rând pentru desenare

    def loadImages(self):
        self.images = {}  # Inițializăm dicționarul pentru imagini
        for fileName in os.listdir("images"):  # Iterăm prin fiecare fișier din directorul "images"
            if not fileName.endswith(".png"):  # Verificăm dacă fișierul este de tip imagine PNG
                continue  # Dacă nu este, trecem la următoarea iterație
            # Încărcăm imaginea din fișier, redimensionăm la dimensiunea piesei și o adăugăm în dicționar
            image = pygame.image.load(os.path.join("images", fileName))
            image = pygame.transform.scale(image, self.pieceSize)
            self.images[fileName.split(".")[0]] = image

    def getImage(self, piece):
        string = None  # Inițializăm string-ul pentru a stoca cheia imaginii în dicționar
        if piece.getClicked():  # Verificăm dacă piesa a fost făcută clic
            if piece.getHasBomb():  # Verificăm dacă piesa conține o bombă
                string = "bomb-at-clicked-block"  # Setăm cheia pentru imaginea cu bombă
            else:
                string = str(piece.getNumAround())  # Setăm cheia pentru imaginea cu numărul de bombe din jurul piesei
        else:
            string = "flag" if piece.getFlagged() else "empty-block"  # Setăm cheia pentru imaginea de steag sau celulă goală
        return self.images[string]  # Returnăm imaginea corespunzătoare cheii din dicționar

    def handleClick(self, position, rightClick):
        if self.board.getLost():  # Verificăm dacă jocul s-a pierdut
            return  # Dacă da, nu permitem alte clicuri
        # Obținem indexul piesei pe care s-a făcut clic
        index = position[1] // self.pieceSize[1], position[0] // self.pieceSize[0]
        piece = self.board.getPiece(index)  # Obținem referința către piesa la indexul dat
        self.board.handleClick(piece, rightClick)  # Tratăm evenimentul de clic în funcție de tipul acestuia