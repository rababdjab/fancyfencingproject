class Joueur:
    mouvementspeed = 0
    attakingrange = 0
    blokingtime = 0
    defendingrange = 0
    score = 0
    def __int__(self, id, position):
        self.position = position
        self.id=id
