class QuantiteStockException(Exception):
    def __init__(self,msg="", *args, **kwargs) -> None:
        msg = msg or "montant solde inférieur !"
        super().__init__(msg, *args, **kwargs)
        
