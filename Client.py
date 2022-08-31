# client

class Client():
    def __init__(self, nom, prenom, adresse) -> None:
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse

    def __str__(self) -> str:
        return f" nom du client : {self.nom}, prénom : {self.prenom}, adresse : {self.adresse}, numero securite : {self.numSecSoc}"


class ClientPermanent(Client):
    def __init__(self, nom, prenom, adresse, numSecSoc, montantDecouvert) -> None:
        super().__init__(nom, prenom, adresse)
        self.numSecSoc = numSecSoc
        self.montantDecouvert = montantDecouvert

    def __str__(self) -> str:
        return super().__str__()

    def extraireMontantAchat(self, montant):
        return self.montantDecouvert - montant

    @property
    def montantRestantClient(self):
        return self.montantDecouvert

    def verifierADecouvert(self):
        return self.montantDecouvert < 0
