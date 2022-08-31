# l'ensemble des operations pouvant être effectué
from exceptions.quantiteStockException import QuantiteStockException
from medicament import Medicament


class Operation():
    def __init__(self, typeOp, dateOp) -> None:
        self.typeOp = typeOp
        self.dateOp = dateOp

    def __str__(self) -> str:
        return f" l'operation de type {self.typeOp} effectué le {self.dateOp}"


class Achat(Operation):
    def __init__(self, typeOp, dateOp, quantite, medicament) -> None:
        super().__init__(typeOp, dateOp)
        self.quantite = quantite
        self.medicament = medicament

    def calculMontant(self, quantite, medicament):
        if quantite < medicament.quantite:
            return quantite * medicament.prix
        else:
            raise QuantiteStockException


class Approvisionnement(Operation):
    def __init__(self, typeOp, dateOp) -> None:
        super().__init__(typeOp, dateOp)
        

    def approvisionner(self, quantite, medicament):
        medicament.quantite = medicament.quantite + quantite
        print(medicament)
        


class AjouterMedicament(Operation):
    def __init__(self, typeOp, dateOp) -> None:
        super().__init__(typeOp, dateOp)

    def userDialog(self):
        nomMed = input(" Entrer le nom du médicament: ")
        quantite = int(input(" Entrer la quantité: "))
        prix = int(input(" Entrer le prix unitaire de médicament: "))
        designation = input("Entrer la désignation ")
        return Medicament(prix, quantite, nomMed, designation)
