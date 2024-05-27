class Piece:
    def __init__(self, hasBomb):
        self.hasBomb = hasBomb  # Indicator dacă această piesă conține o bombă sau nu
        self.clicked = False  # Indicator dacă piesa a fost făcută clic sau nu
        self.flagged = False  # Indicator dacă piesa este marcată cu un steag sau nu

    def getHasBomb(self):
        return self.hasBomb  # Returnează True dacă piesa conține o bombă, False altfel

    def getClicked(self):
        return self.clicked  # Returnează True dacă piesa a fost făcută clic, False altfel

    def getFlagged(self):
        return self.flagged  # Returnează True dacă piesa este marcată cu un steag, False altfel

    def setNeighbors(self, neighbors):
        self.neighbors = neighbors  # Setează lista de vecini a piesei
        self.setNumAround()  # Calculează numărul de vecini care conțin bombe

    def setNumAround(self):
        self.numAround = 0  # Inițializăm numărul de vecini care conțin bombe
        for piece in self.neighbors:  # Pentru fiecare vecin al piesei
            if piece.getHasBomb():  # Verificăm dacă vecinul conține o bombă
                self.numAround += 1  # Dacă da, incrementăm numărul de vecini care conțin bombe

    def getNumAround(self):
        return self.numAround  # Returnează numărul de vecini care conțin bombe

    def toggleFlag(self):
        self.flagged = not self.flagged  # Comută starea flag-ului piesei între True și False

    def click(self):
        self.clicked = True  # Setează starea piesei ca făcută clic

    def getNeighbors(self):
        return self.neighbors  # Returnează lista de vecini ai piesei