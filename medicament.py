# class representation Medicament

class Medicament():
    def __init__(self, prix, quantite, nommed, designation) -> None:
        self.prix = prix
        self.quantite = quantite
        self.nommed = nommed
        self.designation = designation

    def __str__(self) -> str:
        return f"nom médicament : {self.nommed}, désignation : {self.designation} prix u : {self.prix} et quantite : {self.quantite}"

    def affichage(self):
        print("le medicament est ", self.nommed, " prix U ",
              self.prix, " et quantite ", self.quantite)

    # getters et setters
    @property
    def getQuantite(self):
        return self.quantite

    @property
    def getPrix(self):
        return self.prix

    @property
    def getNommed(self):
        return self.nommed

    @property
    def getDesignation(self):
        return self.designation

    @property
    def setPrix(self, prix):
        self.prix = prix

    @property
    def setDesignation(self, designation):
        self.designation = designation

    @property
    def setNommed(self, nommed):
        self.nommed = nommed

    @property
    def setQuantite(self, quantite):
        self.quantite = quantite
